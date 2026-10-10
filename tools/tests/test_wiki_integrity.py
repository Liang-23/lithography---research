from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))

from wiki_integrity import extract_markdown_links, extract_wikilinks, run  # noqa: E402


class WikiIntegrityTests(unittest.TestCase):
    def test_code_examples_are_not_links(self) -> None:
        text = (
            "Live [[Real Note]], embedded ![[diagram.png]], and `[[Inline Example]]`\n"
            "```md\n[[Fenced Example]]\n```"
        )
        self.assertEqual(extract_wikilinks(text), ["Real Note"])

    def test_ordinary_markdown_link_extraction_ignores_images_and_code(self) -> None:
        text = "Live [note](../other.md), ![image](image.png), and `[code](hidden.md)`."
        self.assertEqual(extract_markdown_links(text), ["../other.md"])

    def test_alias_heading_and_display_links_resolve(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wiki = root / "wiki"
            concepts = wiki / "concepts"
            concepts.mkdir(parents=True)
            (wiki / "index.md").write_text(
                "# Index\n\n[[overview|Overview]]\n[[Canonical Note]]\n", encoding="utf-8"
            )
            (wiki / "log.md").write_text("# Log\n\nNo sources yet.\n", encoding="utf-8")
            (wiki / "overview.md").write_text(
                "---\ntitle: Overview\ntype: synthesis\nauthority_class: derived\ncanonical_refs: [CORE]\n---\n"
                "# Overview\n\nA sufficiently detailed explanation linking [[Alias Name#Section|Readable]].\n",
                encoding="utf-8",
            )
            (concepts / "Canonical Note.md").write_text(
                "---\ntitle: Canonical Note\naliases: [Alias Name]\ntype: concept\nauthority_class: derived\ncanonical_refs: [CORE]\n---\n"
                "# Canonical Note\n\nA sufficiently detailed concept explanation linking back to [[overview]].\n",
                encoding="utf-8",
            )
            report = run("health", root)
            self.assertEqual(report["summary"]["errors"], 0)
            self.assertEqual(report["summary"]["wikilinks"], 4)
            self.assertFalse((root / "graph.json").exists())

    def test_broken_link_is_structural_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wiki = root / "wiki"
            wiki.mkdir()
            (wiki / "index.md").write_text("# Index\n\n[[overview]]\n", encoding="utf-8")
            (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
            (wiki / "overview.md").write_text(
                "---\ntitle: Overview\ntype: synthesis\nauthority_class: derived\ncanonical_refs: [CORE]\n---\n"
                "# Overview\n\nA detailed explanation that points to [[Missing Note]].\n",
                encoding="utf-8",
            )
            report = run("health", root)
            codes = {issue["code"] for issue in report["issues"]}
            self.assertIn("BROKEN_WIKILINK", codes)
            self.assertGreater(report["summary"]["errors"], 0)

    def test_cross_layer_markdown_edge_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wiki = root / "wiki"
            background = root / "01_Background"
            wiki.mkdir()
            background.mkdir()
            (background / "BG.md").write_text("# Background\n", encoding="utf-8")
            (wiki / "index.md").write_text("# Index\n\n[[overview]]\n", encoding="utf-8")
            (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
            (wiki / "overview.md").write_text(
                "---\ntitle: Overview\ntype: synthesis\nauthority_class: derived\ncanonical_refs: [CORE]\n---\n"
                "# Overview\n\nA detailed explanation with [raw Background](../01_Background/BG.md).\n",
                encoding="utf-8",
            )
            report = run("health", root)
            codes = {issue["code"] for issue in report["issues"]}
            self.assertIn("CROSS_LAYER_GRAPH_EDGE", codes)

    def test_inbound_canonical_markdown_edge_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wiki = root / "wiki"
            background = root / "01_Background"
            wiki.mkdir()
            background.mkdir()
            (wiki / "index.md").write_text("# Index\n\n[[overview]]\n", encoding="utf-8")
            (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
            (wiki / "overview.md").write_text(
                "---\ntitle: Overview\ntype: synthesis\nauthority_class: derived\ncanonical_refs: [CORE]\n---\n"
                "# Overview\n\nA sufficiently detailed human-readable explanation.\n",
                encoding="utf-8",
            )
            (background / "BG.md").write_text(
                "# Background\n\nDo not expose the [human Wiki](../wiki/overview.md).\n",
                encoding="utf-8",
            )
            report = run("health", root)
            codes = {issue["code"] for issue in report["issues"]}
            self.assertIn("CROSS_LAYER_GRAPH_EDGE", codes)

    def test_unscoped_obsidian_graph_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wiki = root / "wiki"
            obsidian = root / ".obsidian"
            wiki.mkdir()
            obsidian.mkdir()
            (obsidian / "graph.json").write_text('{"search": ""}\n', encoding="utf-8")
            (wiki / "index.md").write_text("# Index\n\n[[overview]]\n", encoding="utf-8")
            (wiki / "log.md").write_text("# Log\n", encoding="utf-8")
            (wiki / "overview.md").write_text(
                "---\ntitle: Overview\ntype: synthesis\nauthority_class: derived\ncanonical_refs: [CORE]\n---\n"
                "# Overview\n\nA sufficiently detailed human-readable explanation.\n",
                encoding="utf-8",
            )
            report = run("health", root)
            codes = {issue["code"] for issue in report["issues"]}
            self.assertIn("UNSCOPED_HUMAN_GRAPH", codes)


if __name__ == "__main__":
    unittest.main()
