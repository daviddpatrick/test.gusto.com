---
name: google-python-style
description: Apply the Google Python Style Guide when writing, reviewing, refactoring, or documenting Python code. Use for naming, imports, docstrings, typing, structure, readability, and style-guide compliance.
---

# Google Python Style Skill

Use this skill when:
- the task involves Python code
- the user asks for style cleanup, linting, refactoring, review feedback, or docstring improvements
- the repository or team wants Google-style Python conventions

## Goal
Bring Python code and documentation into alignment with the Google Python Style Guide while preserving behavior unless the user explicitly asks for deeper refactoring.

## Behavior
When using this skill:
1. Prefer small, readable, low-risk edits.
2. Preserve behavior unless the user explicitly asks for refactoring.
3. Explain style fixes in terms of readability, maintainability, consistency, and correctness.
4. When reviewing code, identify:
   - naming issues
   - import ordering or grouping issues
   - docstring issues
   - typing issues
   - overly complex constructs
   - formatting or structure issues
5. When rewriting code:
   - keep public APIs stable unless asked otherwise
   - add or improve docstrings in Google style
   - use clear names
   - avoid unnecessary cleverness
   - prefer explicit code over ambiguous shortcuts

## Review checklist
Check for:
- descriptive names for modules, classes, functions, variables, and constants
- CapWords for classes
- snake_case for functions, methods, variables, and module names
- UPPER_CASE_WITH_UNDERSCORES for constants
- clear import grouping and no unused or wildcard imports
- public classes, methods, and functions with meaningful docstrings
- concise comments that explain why, not what, unless clarification is needed
- readable control flow and manageable function size
- type hints where they improve clarity and maintenance
- no accidental behavior changes while fixing style

## Priority references
Read these local references as needed:
- `references/google_py_style_summary.md`
- `references/naming_rules.md`
- `references/docstring_rules.md`
- `references/examples.md`

## Suggested workflow
1. Read the target Python file or package.
2. Identify the highest-confidence style violations first.
3. Make minimal edits.
4. Re-check imports, names, and docstrings.
5. Summarize what changed and why.

## Optional checker
You may run:
- `python tools/check_google_style.py <path>`

Use the checker to produce a lightweight rule-based review, then make fixes directly in source files.

## Notes
- Treat the local references as a practical working summary of the Google Python Style Guide.
- If a repository has its own formatter, linter, or established conventions, follow user intent and repository constraints.
- When style guidance conflicts with existing project requirements, call out the tradeoff rather than forcing a rewrite.
