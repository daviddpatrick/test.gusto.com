from __future__ import annotations

import ast
import pathlib
import re
import sys
from dataclasses import dataclass


SNAKE_CASE = re.compile(r"^[a-z_][a-z0-9_]*$")
CAP_WORDS = re.compile(r"^[A-Z][A-Za-z0-9]+$")
UPPER_CASE = re.compile(r"^[A-Z][A-Z0-9_]*$")


@dataclass
class Issue:
    path: str
    line: int
    kind: str
    message: str


def check_file(path: pathlib.Path) -> list[Issue]:
    issues: list[Issue] = []
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except Exception as exc:
        return [Issue(str(path), 1, "parse_error", f"Could not parse file: {exc}")]

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not SNAKE_CASE.match(node.name):
                issues.append(
                    Issue(
                        str(path),
                        node.lineno,
                        "naming",
                        f"Function '{node.name}' should be snake_case",
                    )
                )
            if ast.get_docstring(node) is None and not node.name.startswith("_"):
                issues.append(
                    Issue(
                        str(path),
                        node.lineno,
                        "docstring",
                        f"Public function '{node.name}' is missing a docstring",
                    )
                )

        elif isinstance(node, ast.ClassDef):
            if not CAP_WORDS.match(node.name):
                issues.append(
                    Issue(
                        str(path),
                        node.lineno,
                        "naming",
                        f"Class '{node.name}' should use CapWords",
                    )
                )
            if ast.get_docstring(node) is None and not node.name.startswith("_"):
                issues.append(
                    Issue(
                        str(path),
                        node.lineno,
                        "docstring",
                        f"Public class '{node.name}' is missing a docstring",
                    )
                )

        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id
                    if name.isupper() and not UPPER_CASE.match(name):
                        issues.append(
                            Issue(
                                str(path),
                                node.lineno,
                                "naming",
                                f"Constant '{name}' should be UPPER_CASE_WITH_UNDERSCORES",
                            )
                        )

        elif isinstance(node, ast.ImportFrom):
            if any(alias.name == "*" for alias in node.names):
                issues.append(
                    Issue(
                        str(path),
                        node.lineno,
                        "imports",
                        "Avoid wildcard imports",
                    )
                )

    return issues


def iter_py_files(root: pathlib.Path):
    if root.is_file() and root.suffix == ".py":
        yield root
        return

    for path in root.rglob("*.py"):
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        yield path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/check_google_style.py <path>")
        return 2

    root = pathlib.Path(sys.argv[1])
    all_issues: list[Issue] = []

    for py_file in iter_py_files(root):
        all_issues.extend(check_file(py_file))

    for issue in sorted(all_issues, key=lambda x: (x.path, x.line, x.kind)):
        print(f"{issue.path}:{issue.line}: {issue.kind}: {issue.message}")

    return 1 if all_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
