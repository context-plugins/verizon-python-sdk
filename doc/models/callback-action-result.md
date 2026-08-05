
# Callback Action Result

Response to a callback action.

## Structure

`CallbackActionResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of the billing account. |
| `service_name` | `str` | Optional | The name of the callback service that was registered/deregistered. |

## Example

```python
from verizon.models.callback_action_result import CallbackActionResult

callback_action_result = CallbackActionResult(
    account_name='122333444-00002',
    service_name='CarrierService'
)
```

