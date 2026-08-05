
# Api Response Code

ResponseCode and/or a message indicating success or failure of the request.

## Structure

`ApiResponseCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_code` | [`ResponseCodeEnum`](../../doc/models/response-code-enum.md) | Required | Possible response codes. |
| `message` | `str` | Required | More details about the responseCode received. |

## Example

```python
from verizon.models.api_response_code import ApiResponseCode
from verizon.models.response_code_enum import ResponseCodeEnum

api_response_code = ApiResponseCode(
    response_code=ResponseCodeEnum.INVALID_ACCESS,
    message='message6'
)
```

