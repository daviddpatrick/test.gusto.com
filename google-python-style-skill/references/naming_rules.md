# Naming Rules

## General
- Prefer descriptive names over abbreviations unless the abbreviation is widely understood.
- Names should make the code easier to scan without reading surrounding implementation details.
- Avoid single-letter names outside of very small local scopes.

## Preferred conventions
- Modules: `lowercase_with_underscores`
- Packages: short, lowercase names
- Classes: `CapWords`
- Exceptions: `CapWords`, often with `Error` suffix
- Functions: `lowercase_with_underscores`
- Methods: `lowercase_with_underscores`
- Variables: `lowercase_with_underscores`
- Constants: `UPPER_CASE_WITH_UNDERSCORES`
- Internal/private helpers: prefix with `_` where appropriate

## Examples
Good:
- `user_profile.py`
- `PaymentProcessor`
- `load_user_profile`
- `retry_count`
- `DEFAULT_TIMEOUT_SECONDS`
- `_normalize_headers`

Less clear:
- `Userprofile`
- `DoThing`
- `tmpVal`
- `x1`
- `constValue`

## Review prompts
Ask:
- Does the name reflect purpose, not implementation trivia?
- Would a teammate understand the symbol without extra explanation?
- Is the naming consistent with nearby code?
