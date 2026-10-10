"""Deterministic integrity checks for the Obsidian Markdown Wiki.

This module validates Markdown notes and ``[[wikilinks]]`` directly. It never
generates a graph, reads a relationship registry, or writes graph artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import unquote


WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s*-\s+(.*?)\s*$")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
TRACEABILITY_FIELDS = (
    "canonical_refs",
    "source_ids",
    "data_ids",
    "evidence_ids",
    "physics_constraint_ids",
    "hypothesis_ids",
    "method_ids",
    "experiment_ids",
    "decision_ids",
)
CONTENT_TYPES = {"source", "entity", "concept", "synthesis"}
ADMIN_NAMES = {"index.md", "log.md"}
HUMAN_GRAPH_FILTER = "path:wiki -file:index -file:log"


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    path: str | None = None
    target: str | None = None


@dataclass
class Note:
    path: Path
    relative: str
    relative_no_suffix: str
    stem: str
    title: str
    aliases: list[str]
    note_type: str
    metadata: dict[str, object]
    text: str
    body: str
    links: list[str]


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_inline_list(value: str) -> list[str]:
    inner = value.strip()[1:-1].strip()
    if not inner:
        return []
    return [_strip_quotes(part.strip()) for part in inner.split(",") if part.strip()]


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """Parse the simple scalar/list YAML subset used by Wiki frontmatter."""

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {"__malformed__": "missing closing delimiter"}, ""

    metadata: dict[str, object] = {}
    index = 1
    while index < end:
        match = FIELD_RE.match(lines[index])
        if not match:
            index += 1
            continue
        key, raw_value = match.groups()
        raw_value = raw_value.strip()
        if raw_value.startswith("[") and raw_value.endswith("]"):
            metadata[key] = _parse_inline_list(raw_value)
            index += 1
            continue
        if raw_value:
            lowered = raw_value.lower()
            if lowered in {"true", "false"}:
                metadata[key] = lowered == "true"
            elif lowered in {"null", "none", "~"}:
                metadata[key] = None
            else:
                metadata[key] = _strip_quotes(raw_value)
            index += 1
            continue

        values: list[str] = []
        cursor = index + 1
        while cursor < end:
            item_match = LIST_ITEM_RE.match(lines[cursor])
            if not item_match:
                break
            values.append(_strip_quotes(item_match.group(1)))
            cursor += 1
        metadata[key] = values if values else None
        index = cursor

    return metadata, "\n".join(lines[end + 1 :])


def strip_code(text: str) -> str:
    """Remove fenced and inline code while preserving line structure."""

    output: list[str] = []
    active_fence: str | None = None
    for line in text.splitlines():
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)
            if active_fence is None:
                active_fence = marker[0]
            elif marker[0] == active_fence:
                active_fence = None
            output.append("")
            continue
        if active_fence is not None:
            output.append("")
            continue
        output.append(re.sub(r"`+[^`\n]*`+", "", line))
    return "\n".join(output)


def extract_wikilinks(text: str) -> list[str]:
    clean = strip_code(text)
    return [match.group(1).strip() for match in WIKILINK_RE.finditer(clean)]


def extract_markdown_links(text: str) -> list[str]:
    """Extract ordinary Markdown link destinations, excluding images and code."""

    clean = strip_code(text)
    return [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(clean)]


def markdown_link_target(raw_target: str) -> str:
    """Remove Markdown angle brackets, optional titles, anchors, and query strings."""

    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = re.sub(r"\s+(?:\"[^\"]*\"|'[^']*')\s*$", "", target)
    target = unquote(target.strip())
    return target.split("#", 1)[0].split("?", 1)[0].strip()


def is_external_target(target: str) -> bool:
    """Return true for URI targets while treating Windows drive paths as local."""

    if re.match(r"^[A-Za-z]:[\\/]", target):
        return False
    return bool(re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target)) or target.startswith("//")


def normalize_key(value: str) -> str:
    value = unquote(value).replace("\\", "/").strip()
    if value.lower().endswith(".md"):
        value = value[:-3]
    value = re.sub(r"^\./", "", value)
    value = re.sub(r"/+", "/", value).strip("/")
    return value.casefold()


def link_target(raw_link: str) -> str:
    target = raw_link.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    target = target.split("^", 1)[0].strip()
    return target


def _metadata_list(metadata: dict[str, object], key: str) -> list[str]:
    value = metadata.get(key)
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


class WikiIntegrity:
    def __init__(self, project_root: Path, wiki_root: Path | None = None) -> None:
        self.project_root = project_root.resolve()
        self.wiki_root = (wiki_root or self.project_root / "wiki").resolve()
        self.notes: list[Note] = []
        self.issues: list[Issue] = []
        self.links_resolved = 0
        self.links_total = 0
        self.markdown_links_total = 0
        self.incoming: dict[str, int] = defaultdict(int)
        self.outgoing: dict[str, int] = defaultdict(int)
        self.resolved_edges: list[tuple[str, str]] = []
        self._path_keys: dict[str, list[Note]] = defaultdict(list)
        self._stem_keys: dict[str, list[Note]] = defaultdict(list)
        self._alias_keys: dict[str, list[Note]] = defaultdict(list)

    def issue(
        self,
        severity: str,
        code: str,
        message: str,
        path: str | None = None,
        target: str | None = None,
    ) -> None:
        self.issues.append(Issue(severity, code, message, path, target))

    def load(self) -> None:
        if not self.wiki_root.is_dir():
            self.issue("error", "MISSING_WIKI", "Wiki directory does not exist", str(self.wiki_root))
            return
        for path in sorted(self.wiki_root.rglob("*.md"), key=lambda item: item.as_posix().casefold()):
            try:
                text = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError) as exc:
                self.issue("error", "UNREADABLE_NOTE", str(exc), self._display(path))
                continue
            metadata, body = parse_frontmatter(text)
            relative = path.relative_to(self.wiki_root).as_posix()
            if "__malformed__" in metadata:
                self.issue("error", "MALFORMED_FRONTMATTER", str(metadata["__malformed__"]), relative)
            title = str(metadata.get("title") or "").strip()
            if not title:
                h1 = H1_RE.search(body)
                title = h1.group(1).strip() if h1 else path.stem
            note = Note(
                path=path,
                relative=relative,
                relative_no_suffix=PurePosixPath(relative).with_suffix("").as_posix(),
                stem=path.stem,
                title=title,
                aliases=_metadata_list(metadata, "aliases"),
                note_type=str(metadata.get("type") or "").strip(),
                metadata=metadata,
                text=text,
                body=body,
                links=extract_wikilinks(body),
            )
            self.notes.append(note)

        for note in self.notes:
            self._path_keys[normalize_key(note.relative_no_suffix)].append(note)
            self._stem_keys[normalize_key(note.stem)].append(note)
            for alias in note.aliases:
                self._alias_keys[normalize_key(alias)].append(note)

    def _display(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(self.project_root).as_posix()
        except ValueError:
            return str(path)

    def resolve(self, source: Note, raw_link: str) -> list[Note]:
        target = link_target(raw_link)
        if not target:
            return []
        normalized = normalize_key(target)
        if normalized.startswith("wiki/"):
            normalized = normalized[5:]

        candidates: list[Note] = []

        def add(items: Iterable[Note]) -> None:
            for item in items:
                if item not in candidates:
                    candidates.append(item)

        add(self._path_keys.get(normalized, []))
        if "/" in target or target.startswith("."):
            source_parent = PurePosixPath(source.relative_no_suffix).parent
            combined = (source_parent / target).as_posix()
            # Collapse relative path components without touching the filesystem.
            parts: list[str] = []
            for part in PurePosixPath(combined).parts:
                if part in {"", "."}:
                    continue
                if part == "..":
                    if parts:
                        parts.pop()
                    continue
                parts.append(part)
            add(self._path_keys.get(normalize_key("/".join(parts)), []))

        target_stem = PurePosixPath(normalized).name
        add(self._stem_keys.get(target_stem, []))
        add(self._alias_keys.get(normalized, []))
        return candidates

    def run_health(self) -> dict[str, object]:
        self.load()
        self._check_graph_scope()
        if not self.notes:
            if not any(issue.code == "MISSING_WIKI" for issue in self.issues):
                self.issue("error", "EMPTY_WIKI", "Wiki contains no Markdown notes")
            return self.report("health")

        self._check_notes()
        self._check_links()
        self._check_cross_plane_edges()
        self._check_index()
        self._check_log_coverage()
        return self.report("health")

    def run_lint(self) -> dict[str, object]:
        self.run_health()
        self._check_duplicate_names()
        self._check_network_quality()
        self._check_stale_sources()
        return self.report("lint")

    def _check_notes(self) -> None:
        for note in self.notes:
            visible = strip_code(note.body)
            visible = re.sub(r"^#+\s+.*$", "", visible, flags=re.MULTILINE)
            visible = re.sub(r"\s+", " ", visible).strip()
            if not visible:
                self.issue("error", "EMPTY_NOTE", "Note has no content beyond metadata/headings", note.relative)
            elif len(visible) < 120 and note.path.name not in ADMIN_NAMES:
                self.issue("warning", "SPARSE_NOTE", "Note has very little explanatory content", note.relative)

            if note.note_type in CONTENT_TYPES:
                authority = str(note.metadata.get("authority_class") or "").strip()
                if authority != "derived":
                    self.issue(
                        "error",
                        "INVALID_WIKI_AUTHORITY",
                        "Content note must declare authority_class: derived",
                        note.relative,
                    )
                trace_values = [item for key in TRACEABILITY_FIELDS for item in _metadata_list(note.metadata, key)]
                source_file = str(note.metadata.get("source_file") or "").strip()
                if not trace_values and not source_file:
                    self.issue(
                        "error",
                        "MISSING_TRACEABILITY",
                        "Content note has no canonical path, Governance ID, or source_file traceability",
                        note.relative,
                    )
                if note.note_type == "source":
                    if not _metadata_list(note.metadata, "source_ids"):
                        self.issue("error", "MISSING_SOURCE_ID", "Source note needs a registered SRC-ID", note.relative)
                    if not source_file:
                        self.issue("error", "MISSING_SOURCE_FILE", "Source note needs source_file", note.relative)
                    else:
                        source_path = (self.project_root / source_file).resolve()
                        try:
                            source_path.relative_to(self.project_root)
                        except ValueError:
                            self.issue("error", "SOURCE_OUTSIDE_PROJECT", "source_file escapes the project", note.relative)
                        else:
                            if not source_path.is_file():
                                self.issue("error", "BROKEN_SOURCE_FILE", "source_file does not exist", note.relative, source_file)

    def _check_links(self) -> None:
        for note in self.notes:
            for raw_link in note.links:
                self.links_total += 1
                target = link_target(raw_link)
                candidates = self.resolve(note, raw_link)
                if not candidates:
                    self.issue("error", "BROKEN_WIKILINK", "Wikilink does not resolve", note.relative, target)
                    continue
                if len(candidates) > 1:
                    paths = ", ".join(candidate.relative for candidate in candidates)
                    self.issue(
                        "error",
                        "AMBIGUOUS_WIKILINK",
                        f"Wikilink resolves to multiple notes: {paths}",
                        note.relative,
                        target,
                    )
                    continue
                resolved = candidates[0]
                self.links_resolved += 1
                self.outgoing[note.relative] += 1
                self.incoming[resolved.relative] += 1
                self.resolved_edges.append((note.relative, resolved.relative))

    def _local_markdown_target(self, source_path: Path, raw_target: str) -> Path | None:
        target = markdown_link_target(raw_target)
        if not target or target.startswith("#") or is_external_target(target):
            return None
        candidate = Path(target)
        if not candidate.is_absolute():
            candidate = source_path.parent / candidate
        candidate = candidate.resolve()
        if candidate.suffix == "" and candidate.with_suffix(".md").is_file():
            candidate = candidate.with_suffix(".md")
        return candidate

    @staticmethod
    def _is_within(path: Path, root: Path) -> bool:
        try:
            path.resolve().relative_to(root.resolve())
        except ValueError:
            return False
        return True

    def _check_graph_scope(self) -> None:
        obsidian_root = self.project_root / ".obsidian"
        if not obsidian_root.is_dir():
            return
        graph_path = obsidian_root / "graph.json"
        if not graph_path.is_file():
            self.issue(
                "error",
                "MISSING_HUMAN_GRAPH_CONFIG",
                "Obsidian is configured for this project but .obsidian/graph.json is missing",
                self._display(graph_path),
            )
            return
        try:
            graph_config = json.loads(graph_path.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            self.issue("error", "INVALID_HUMAN_GRAPH_CONFIG", str(exc), self._display(graph_path))
            return
        search = str(graph_config.get("search") or "").strip()
        if search != HUMAN_GRAPH_FILTER:
            self.issue(
                "error",
                "UNSCOPED_HUMAN_GRAPH",
                f"Global Graph search must be exactly '{HUMAN_GRAPH_FILTER}'",
                self._display(graph_path),
                search or "<empty>",
            )

    def _check_cross_plane_edges(self) -> None:
        """Reject graph-producing Markdown edges across the canonical/Wiki boundary."""

        for note in self.notes:
            for raw_target in extract_markdown_links(note.body):
                self.markdown_links_total += 1
                candidate = self._local_markdown_target(note.path, raw_target)
                if candidate is None:
                    continue
                if candidate.suffix.casefold() == ".md" and not self._is_within(candidate, self.wiki_root):
                    self.issue(
                        "error",
                        "CROSS_LAYER_GRAPH_EDGE",
                        "Wiki Markdown link resolves outside wiki/; use a non-clickable Governance ID or path",
                        note.relative,
                        self._display(candidate),
                    )

        ignored_roots = {".git", ".obsidian", "wiki"}
        for path in sorted(self.project_root.rglob("*.md"), key=lambda item: item.as_posix().casefold()):
            try:
                relative_parts = path.resolve().relative_to(self.project_root).parts
            except ValueError:
                continue
            if relative_parts and relative_parts[0] in ignored_roots:
                continue
            try:
                text = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError):
                continue

            for raw_target in extract_markdown_links(text):
                candidate = self._local_markdown_target(path, raw_target)
                if candidate is not None and candidate.suffix.casefold() == ".md" and self._is_within(
                    candidate, self.wiki_root
                ):
                    self.issue(
                        "error",
                        "CROSS_LAYER_GRAPH_EDGE",
                        "Canonical Markdown link resolves into wiki/; use a non-clickable path instead",
                        self._display(path),
                        self._display(candidate),
                    )

            for raw_link in extract_wikilinks(text):
                target = link_target(raw_link)
                normalized = normalize_key(target)
                candidates: list[Note] = []
                if normalized.startswith("wiki/"):
                    candidates.extend(self._path_keys.get(normalized[5:], []))
                else:
                    candidates.extend(self._path_keys.get(normalized, []))
                    candidates.extend(self._stem_keys.get(PurePosixPath(normalized).name, []))
                    candidates.extend(self._alias_keys.get(normalized, []))
                if candidates:
                    self.issue(
                        "error",
                        "CROSS_LAYER_GRAPH_EDGE",
                        "Canonical wikilink resolves into wiki/; use a non-clickable path instead",
                        self._display(path),
                        target,
                    )

    def _check_index(self) -> None:
        index = next((note for note in self.notes if note.relative.casefold() == "index.md"), None)
        if index is None:
            self.issue("error", "MISSING_INDEX", "wiki/index.md does not exist")
            return
        indexed: set[str] = set()
        for raw_link in index.links:
            candidates = self.resolve(index, raw_link)
            if len(candidates) == 1:
                indexed.add(candidates[0].relative)
        required = {
            note.relative
            for note in self.notes
            if note.relative == "overview.md"
            or PurePosixPath(note.relative).parts[0] in {"sources", "entities", "concepts", "syntheses"}
        }
        for missing in sorted(required - indexed):
            self.issue("error", "UNINDEXED_PAGE", "Content page is missing from wiki/index.md", missing)

    def _check_log_coverage(self) -> None:
        log = next((note for note in self.notes if note.relative.casefold() == "log.md"), None)
        if log is None:
            self.issue("error", "MISSING_LOG", "wiki/log.md does not exist")
            return
        ingest_lines = [
            line.casefold()
            for line in log.body.splitlines()
            if re.match(r"^##\s+\[\d{4}-\d{2}-\d{2}\]\s+ingest\s+\|", line, flags=re.IGNORECASE)
        ]
        for note in self.notes:
            if note.note_type != "source" and not note.relative.startswith("sources/"):
                continue
            needles = {note.title.casefold(), note.stem.casefold()}
            if not any(any(needle in line for needle in needles) for line in ingest_lines):
                self.issue("error", "MISSING_INGEST_LOG", "Source note lacks a matching ingest log entry", note.relative)

    def _check_duplicate_names(self) -> None:
        name_map: dict[str, set[str]] = defaultdict(set)
        for note in self.notes:
            if note.note_type not in {"concept", "entity"}:
                continue
            for name in [note.title, *note.aliases]:
                name_map[normalize_key(name)].add(note.relative)
        for name, paths in sorted(name_map.items()):
            if len(paths) > 1:
                self.issue(
                    "warning",
                    "DUPLICATE_TITLE_OR_ALIAS",
                    f"Name/alias is shared by: {', '.join(sorted(paths))}",
                    target=name,
                )

    def _check_network_quality(self) -> None:
        for note in self.notes:
            if note.path.name in ADMIN_NAMES:
                continue
            if note.note_type not in CONTENT_TYPES:
                continue
            degree = self.incoming.get(note.relative, 0) + self.outgoing.get(note.relative, 0)
            if degree == 0:
                self.issue("warning", "ORPHAN_NOTE", "Content note has no resolved incoming or outgoing wikilinks", note.relative)
            if note.note_type in {"concept", "entity", "source"} and self.outgoing.get(note.relative, 0) == 0:
                self.issue("warning", "UNDER_LINKED_NOTE", "Important note has no outgoing contextual wikilink", note.relative)
            visible = re.sub(r"\s+", " ", strip_code(note.body)).strip()
            if note.note_type == "concept" and len(visible) < 300 and degree < 2:
                self.issue(
                    "warning",
                    "POSSIBLE_OVER_FRAGMENTATION",
                    "Small, weakly connected concept may not have independent retrieval value",
                    note.relative,
                )

    def _check_stale_sources(self) -> None:
        for note in self.notes:
            if note.note_type != "source":
                continue
            source_file = str(note.metadata.get("source_file") or "").strip()
            if not source_file:
                continue
            source_path = (self.project_root / source_file).resolve()
            if source_path.is_file() and source_path.stat().st_mtime > note.path.stat().st_mtime + 1:
                self.issue("warning", "STALE_SOURCE_NOTE", "Source file is newer than its Wiki note", note.relative, source_file)

    def report(self, mode: str) -> dict[str, object]:
        errors = sum(issue.severity == "error" for issue in self.issues)
        warnings = sum(issue.severity == "warning" for issue in self.issues)
        report: dict[str, object] = {
            "mode": mode,
            "wiki_root": self._display(self.wiki_root),
            "summary": {
                "notes": len(self.notes),
                "wikilinks": self.links_total,
                "resolved_wikilinks": self.links_resolved,
                "markdown_links": self.markdown_links_total,
                "errors": errors,
                "warnings": warnings,
            },
            "issues": [asdict(issue) for issue in self.issues],
        }
        if mode == "lint":
            report["manual_semantic_review"] = [
                "Contradictory derived explanations across notes",
                "Synonymous or duplicate concepts not detectable from titles/aliases alone",
                "Missing concept/entity pages for repeatedly important ideas",
                "Over-fragmentation or over-linking that requires domain judgment",
                "Stale Overview synthesis and unresolved data gaps",
                "Language, terminology, quotation, formula, path, and code preservation",
                "Semantic projection completeness: copied or link-only canonical material is not ingestion",
                "Machine-grade reconstructions and Human Audit bases exist canonically rather than only in Wiki",
            ]
        return report


def markdown_report(report: dict[str, object]) -> str:
    summary = report["summary"]
    assert isinstance(summary, dict)
    lines = [
        f"# Wiki {str(report['mode']).title()} Report",
        "",
        f"- Notes: {summary['notes']}",
        f"- Wikilinks: {summary['wikilinks']}",
        f"- Resolved wikilinks: {summary['resolved_wikilinks']}",
        f"- Ordinary Markdown links in Wiki bodies: {summary['markdown_links']}",
        f"- Errors: {summary['errors']}",
        f"- Warnings: {summary['warnings']}",
        "",
        "## Issues",
        "",
    ]
    issues = report.get("issues", [])
    assert isinstance(issues, list)
    if not issues:
        lines.append("No deterministic issues found.")
    else:
        for raw in issues:
            assert isinstance(raw, dict)
            location = f" — `{raw['path']}`" if raw.get("path") else ""
            target = f" -> `{raw['target']}`" if raw.get("target") else ""
            lines.append(
                f"- **{str(raw['severity']).upper()} {raw['code']}**{location}{target}: {raw['message']}"
            )
    manual = report.get("manual_semantic_review")
    if isinstance(manual, list):
        lines.extend(["", "## Manual semantic review", ""])
        lines.extend(f"- {item}" for item in manual)
    lines.extend(
        [
            "",
            "This report was computed directly from Markdown links and Obsidian's native scope setting; it did not generate a visual Graph.",
            "",
        ]
    )
    return "\n".join(lines)


def run(mode: str, project_root: Path, wiki_root: Path | None = None) -> dict[str, object]:
    checker = WikiIntegrity(project_root, wiki_root)
    return checker.run_lint() if mode == "lint" else checker.run_health()


def cli(mode: str, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"Run Markdown-native Wiki {mode} checks")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Project root")
    parser.add_argument("--wiki", type=Path, help="Wiki directory (defaults to <root>/wiki)")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown")
    default_report = f"wiki/{mode}-report.md"
    parser.add_argument(
        "--save",
        nargs="?",
        const=default_report,
        metavar="PATH",
        help=f"Save the report (default: {default_report})",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    wiki_root = args.wiki.resolve() if args.wiki else None
    report = run(mode, root, wiki_root)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) if args.json else markdown_report(report)
    print(rendered)

    if args.save:
        destination = Path(args.save)
        if not destination.is_absolute():
            destination = root / destination
        destination = destination.resolve()
        try:
            destination.relative_to(root)
        except ValueError:
            parser.error("--save path must stay inside the project root")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.suffix.casefold() == ".json":
            saved = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        else:
            saved = markdown_report(report)
        destination.write_text(saved, encoding="utf-8")

    summary = report.get("summary", {})
    return 1 if isinstance(summary, dict) and int(summary.get("errors", 0)) else 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(cli("health"))
