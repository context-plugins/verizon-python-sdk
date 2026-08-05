
# Fota V1 Success Result

A response to a successful request contains a single Boolean value.

## Structure

`FotaV1SuccessResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Optional | True is returned in case of success. |

## Example

```python
from verizon.models.fota_v1_success_result import FotaV1SuccessResult

fota_v1_success_result = FotaV1SuccessResult(
    success=True
)
```

