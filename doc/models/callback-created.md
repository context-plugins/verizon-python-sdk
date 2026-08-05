
# Callback Created

## Structure

`CallbackCreated`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The numeric name of the account and must include leading zeroes. |
| `name` | `str` | Required | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. |
| `url` | `str` | Optional | The address of the callback listening service where the ThingSpace Platform will send callback messages for the service type. |

## Example

```python
from verizon.models.callback_created import CallbackCreated

callback_created = CallbackCreated(
    account_name='0000123456-00001',
    name='BullseyeReporting',
    url='https://tsustgtests.mocklab.io/notifications/bullseye'
)
```

