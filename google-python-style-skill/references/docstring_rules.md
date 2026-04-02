# Docstring Rules

## What should have docstrings
Usually document public:
- modules
- classes
- functions
- methods

Private helpers may omit docstrings if they are short and obvious, but add them when behavior is not immediately clear.

## Style
- Start with a short summary sentence.
- Prefer a direct description of behavior.
- Add sections only when they help the reader.
- Keep wording aligned with actual behavior.

## Common Google-style sections
### Args:
Describe each parameter and any important constraints.

### Returns:
Describe the return value and shape when useful.

### Raises:
Describe significant exceptions callers should know about.

### Yields:
Use for generators.

## Function example
```python
def get_user(user_id: str) -> dict[str, str]:
    """Fetches a user record by ID.

    Args:
        user_id: Unique identifier for the user.

    Returns:
        A dictionary containing the user record.

    Raises:
        KeyError: If the user does not exist.
    """
```

## Class example
```python
class PaymentProcessor:
    """Handles payment authorization and capture operations."""
```

## Review prompts
Ask:
- Does the summary tell the reader what the object does?
- Are arguments and return values explained where needed?
- Does the docstring match the actual behavior?
- Is anything important missing or misleading?
