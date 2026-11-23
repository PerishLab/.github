#!/usr/bin/env python3
"""Governance guard for PerishLab/.github.

Iteration authorization: changes to these checks or to this script require the
user's explicit authorization. An executor must not edit this guard to make a
check pass.

Standard library only. Usage:

    python3 guard/governance.py --root .
    python3 guard/governance.py --selftest

The selftest plants one defect per check and requires the guard to fire on each.
A guard that cannot fail is indistinguishable from no guard.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

AUTHORITY_HEADING = "Authority is divided as follows:"
AUTHORITY_ENTRIES = [
    "`--help`",
    "Cookbook",
    "repository `AGENTS.md`",
    "product Skill",
    "organization-wide policy",
    "judged product source",
    "errors, status, and audit output",
]
BAILIWICK = Path("governance/bailiwick.md")
BAILIWICK_SECTIONS = [
    "# Bailiwick",
    "## Standing",
    "## Facades",
    "## Boundary change",
    "## Gaps",
    "## Authority surfaces",
    "## Words",
    "## Judging",
]
BAILIWICK_CONDITIONS = [
    "Explored question",
    "Landed product",
    "Native records",
    "Non-goals",
    "Exit condition",
]
SKIP = {".git", "node_modules", "target", "dist"}

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP for part in path.parts):
            continue
        yield path


def check_links(root: Path) -> list[str]:
    failures = []
    for path in markdown(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not (path.parent / target).resolve().exists():
                failures.append(
                    f"{path.relative_to(root)}: broken link {match.group(1)}"
                )
    return failures


def authority_block(text: str) -> str | None:
    lines = text.splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.strip() == AUTHORITY_HEADING), None
    )
    if start is None:
        return None
    block = [lines[start]]
    index = start + 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    while index < len(lines) and lines[index].strip():
        block.append(lines[index])
        index += 1
    return "\n".join(block)


def check_authority(root: Path) -> list[str]:
    path = root / "GOVERNANCE.md"
    if not path.is_file():
        return ["GOVERNANCE.md: missing"]
    text = path.read_text(encoding="utf-8")
    block = authority_block(text)
    if block is None:
        return [f"GOVERNANCE.md: {AUTHORITY_HEADING!r} not found"]
    failures = []
    count = text.count(AUTHORITY_HEADING)
    if count != 1:
        failures.append(
            f"GOVERNANCE.md: authority division appears {count} times, expected exactly once"
        )
    for entry in AUTHORITY_ENTRIES:
        if entry not in block:
            failures.append(f"GOVERNANCE.md: authority division missing {entry}")
    return failures


def check_bailiwick(root: Path) -> list[str]:
    path = root / BAILIWICK
    if not path.is_file():
        return [f"{BAILIWICK}: missing"]
    text = path.read_text(encoding="utf-8")
    failures = []
    for section in BAILIWICK_SECTIONS:
        if not re.search(rf"^{re.escape(section)}\s*$", text, re.M):
            failures.append(f"{BAILIWICK}: missing section {section}")
    for condition in BAILIWICK_CONDITIONS:
        if condition not in text:
            failures.append(f"{BAILIWICK}: missing condition {condition}")
    return failures


def run(root: Path) -> list[str]:
    return check_links(root) + check_authority(root) + check_bailiwick(root)


def fixture(root: Path) -> None:
    (root / "governance").mkdir(parents=True)
    entries = "\n".join(f"- {entry};" for entry in AUTHORITY_ENTRIES)
    (root / "GOVERNANCE.md").write_text(
        f"# Governance\n\n## Authority\n\n{AUTHORITY_HEADING}\n\n{entries}\n\nEnd.\n",
        encoding="utf-8",
    )
    document = "\n\n".join(BAILIWICK_SECTIONS) + "\n\n"
    document += "\n\n".join(f"| {name} | meaning |" for name in BAILIWICK_CONDITIONS)
    (root / BAILIWICK).write_text(document + "\n", encoding="utf-8")
    (root / "README.md").write_text("# Readme\n\n[governance](GOVERNANCE.md)\n", encoding="utf-8")


def selftest() -> list[str]:
    problems = []
    mutations = [
        (
            "broken link",
            lambda root: (root / "README.md").write_text(
                "# Readme\n\n[gone](missing.md)\n", encoding="utf-8"
            ),
        ),
        (
            "duplicate authority division",
            lambda root: (root / "GOVERNANCE.md").write_text(
                (root / "GOVERNANCE.md").read_text(encoding="utf-8")
                + "\n"
                + (root / "GOVERNANCE.md").read_text(encoding="utf-8"),
                encoding="utf-8",
            ),
        ),
        (
            "missing authority entry",
            lambda root: (root / "GOVERNANCE.md").write_text(
                (root / "GOVERNANCE.md")
                .read_text(encoding="utf-8")
                .replace("product Skill", "product Brief"),
                encoding="utf-8",
            ),
        ),
        (
            "missing bailiwick section",
            lambda root: (root / BAILIWICK).write_text(
                (root / BAILIWICK).read_text(encoding="utf-8").replace(
                    "## Judging", "## Judgment"
                ),
                encoding="utf-8",
            ),
        ),
        (
            "missing bailiwick condition",
            lambda root: (root / BAILIWICK).write_text(
                (root / BAILIWICK).read_text(encoding="utf-8").replace(
                    "Exit condition", "Ending"
                ),
                encoding="utf-8",
            ),
        ),
    ]
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary) / "base"
        fixture(base)
        clean = run(base)
        if clean:
            problems.append(
                "selftest: pristine fixture already fails: " + "; ".join(clean)
            )
        for index, (name, mutate) in enumerate(mutations):
            case = Path(temporary) / f"case-{index}"
            shutil.copytree(base, case)
            mutate(case)
            if not run(case):
                problems.append(f"selftest: {name} produced no failure")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--selftest", action="store_true")
    arguments = parser.parse_args()
    if arguments.selftest:
        problems = selftest()
        for problem in problems:
            print(problem, file=sys.stderr)
        if problems:
            print(f"selftest failed: {len(problems)} problem(s)", file=sys.stderr)
            return 1
        print("selftest passed: every check fires on its planted defect")
        return 0
    root = arguments.root.resolve()
    failures = run(root)
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        print(f"governance guard failed: {len(failures)} finding(s)", file=sys.stderr)
        return 1
    print("governance guard passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
