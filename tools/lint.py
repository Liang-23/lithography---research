"""Markdown-native Wiki network lint; never a Graph renderer."""

from __future__ import annotations

import sys

from wiki_integrity import cli


if __name__ == "__main__":
    sys.exit(cli("lint"))
