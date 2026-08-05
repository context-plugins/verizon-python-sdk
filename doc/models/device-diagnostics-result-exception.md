
# Device Diagnostics Result Exception

All error messages are returned in this format. Error codes and messages are listed on the Error Codes page, along with explanations and suggestions for corrective actions.

## Structure

`DeviceDiagnosticsResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | Simple error code. |
| `error_message` | `str` | Required | Detailed error message. |

## Example

```python
try:
    # make the API call
except DeviceDiagnosticsResultException as e:
    print(e)
except APIException as e:
    print(e)
```

