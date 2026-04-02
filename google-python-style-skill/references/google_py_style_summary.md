# Google Python Style Summary

## Core principles
- Favor readability over cleverness.
- Keep code explicit and maintainable.
- Prefer consistency across a codebase.
- Make changes that are easy to review and low risk.

## Imports
- Put imports at the top of the file.
- Group imports in a consistent order:
  1. standard library
  2. third-party packages
  3. local application imports
- Avoid unused imports.
- Avoid wildcard imports.
- Prefer absolute imports when practical.

## Naming
- Use descriptive names that reflect purpose.
- Classes: `CapWords`
- Exceptions: `CapWords` and often end with `Error`
- Functions and methods: `lowercase_with_underscores`
- Variables: `lowercase_with_underscores`
- Constants: `UPPER_CASE_WITH_UNDERSCORES`
- Internal helpers: leading underscore when appropriate

## Docstrings
- Public modules, functions, classes, and methods should usually have docstrings.
- Start with a short summary sentence.
- Use Google-style sections when helpful:
  - `Args:`
  - `Returns:`
  - `Raises:`
  - `Yields:`
- Keep docstrings accurate and concise.
- Update docstrings when behavior changes.

## Comments
- Prefer self-explanatory code first.
- Use comments to explain intent, tradeoffs, assumptions, or non-obvious behavior.
- Remove stale comments.
- Avoid comments that merely restate the code.

## Typing
- Use type annotations when they improve clarity and maintenance.
- Keep annotations readable and not overly noisy.
- Prefer clarity over maximal type-system cleverness.

## Structure
- Prefer simple control flow.
- Avoid deeply nested logic when possible.
- Break large functions into coherent helpers.
- Keep responsibilities focused.

## Error handling
- Raise specific exceptions when practical.
- Avoid swallowing exceptions silently.
- Preserve useful context in error messages.

## Reviews
When reviewing code, flag:
- unclear names
- missing or weak docstrings
- import clutter
- wildcard imports
- long or deeply nested functions
- mixed responsibilities
- stale comments
- hard-to-read conditionals
- style-only rewrites that risk behavior changes
