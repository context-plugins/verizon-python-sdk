
# Callback Registration Result

## Structure

`CallbackRegistrationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Optional | The name of the account that registered the callback URL. |
| `name` | [`CallbackServiceNameEnum`](../../doc/models/callback-service-name-enum.md) | Optional | The name of the callback service. |

## Example

```python
from verizon.models.callback_registration_result import CallbackRegistrationResult
from verizon.models.callback_service_name_enum import CallbackServiceNameEnum

callback_registration_result = CallbackRegistrationResult(
    account='0212312345-00001',
    name=CallbackServiceNameEnum.LOCATION
)
```

