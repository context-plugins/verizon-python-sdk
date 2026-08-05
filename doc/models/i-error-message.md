
# I Error Message

Error message.

## Structure

`IErrorMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | [`ErrorResponseCodeEnum`](../../doc/models/error-response-code-enum.md) | Optional | Error Code. |
| `error_message` | `str` | Optional | Details and additional information about the error code. |
| `http_status_code` | [`HttpStatusCodeEnum`](../../doc/models/http-status-code-enum.md) | Optional | HTML error code and description. |
| `detail_error_message` | `str` | Optional | More detail and information about the HTML error code. |

## Example

```python
from verizon.models.error_response_code_enum import ErrorResponseCodeEnum
from verizon.models.http_status_code_enum import HttpStatusCodeEnum
from verizon.models.i_error_message import IErrorMessage

i_error_message = IErrorMessage(
    error_code=ErrorResponseCodeEnum.UNAUTHORIZED,
    error_message='errorMessage4',
    http_status_code=HttpStatusCodeEnum.ENUM_200_OK,
    detail_error_message='detailErrorMessage4'
)
```

