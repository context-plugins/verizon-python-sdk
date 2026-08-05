
# Session Reset Password Result

Response to a new, randomly generated password for the current username.

## Structure

`SessionResetPasswordResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_password` | `str` | Optional | The new password for the username. |

## Example

```python
from verizon.models.session_reset_password_result import SessionResetPasswordResult

session_reset_password_result = SessionResetPasswordResult(
    new_password='Wh0a1545a84d'
)
```

