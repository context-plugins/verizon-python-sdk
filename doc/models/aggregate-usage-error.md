
# Aggregate Usage Error

Error reported by a device.

## Structure

`AggregateUsageError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Optional | The International Mobile Equipment Identifier of the device. |
| `error_message` | `str` | Optional | A general error message. |
| `error_response` | [`IErrorMessage`](../../doc/models/i-error-message.md) | Optional | Error message. |

## Example

```python
from verizon.models.aggregate_usage_error import AggregateUsageError
from verizon.models.error_response_code_enum import ErrorResponseCodeEnum
from verizon.models.http_status_code_enum import HttpStatusCodeEnum
from verizon.models.i_error_message import IErrorMessage

aggregate_usage_error = AggregateUsageError(
    imei='15-digit IMEI',
    error_message='errorMessage4',
    error_response=IErrorMessage(
        error_code=ErrorResponseCodeEnum.INVALID_PARAMETER,
        error_message='errorMessage4',
        http_status_code=HttpStatusCodeEnum.ENUM_423_LOCKED,
        detail_error_message='detailErrorMessage6'
    )
)
```

