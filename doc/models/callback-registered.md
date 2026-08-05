
# Callback Registered

Callback listener is Registered.

## Structure

`CallbackRegistered`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The numeric name of the account and must include leading zeroes. |
| `name` | `str` | Required | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. |

## Example

```python
from verizon.models.callback_registered import CallbackRegistered

callback_registered = CallbackRegistered(
    account_name='0000123456-00001',
    name='BullseyeReporting'
)
```

