
# Session Reset Password Request

Request to a new, randomly generated password for the current username.

## Structure

`SessionResetPasswordRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `old_password` | `str` | Required | The current password for the username. |

## Example

```python
from verizon.models.session_reset_password_request import SessionResetPasswordRequest

session_reset_password_request = SessionResetPasswordRequest(
    old_password='grflbk'
)
```

