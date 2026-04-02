# Examples

## Example 1: naming and docstring cleanup

Before:
```python
class usermanager:
    def GetUserName(self, id):
        return self.db.fetch(id)
```

After:
```python
class UserManager:
    """Provides access to user records."""

    def get_user_name(self, user_id: str) -> str:
        """Returns the display name for a user.

        Args:
            user_id: Unique identifier for the user.

        Returns:
            The user's display name.
        """
        return self.db.fetch(user_id)
```

## Example 2: imports and constants

Before:
```python
from mymodule import *
import requests, os

Timeout = 30
```

After:
```python
import os

import requests

from mymodule import ApiClient

TIMEOUT_SECONDS = 30
```

## Example 3: comment quality

Before:
```python
# Increment i by 1
i += 1
```

After:
```python
# Advance to the next retry attempt.
i += 1
```

## Example 4: simplify branching

Before:
```python
def is_ready(status, retries, force):
    if force == True:
        return True
    else:
        if status == "ok":
            if retries < 3:
                return True
    return False
```

After:
```python
def is_ready(status: str, retries: int, force: bool) -> bool:
    """Returns whether work can proceed."""
    if force:
        return True
    return status == "ok" and retries < 3
```
