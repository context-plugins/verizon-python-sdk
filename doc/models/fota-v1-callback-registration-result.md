
# Fota V1 Callback Registration Result

Registered callback account name and service name.

## Structure

`FotaV1CallbackRegistrationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of the billing account for which callback messages will be sent. |
| `service_name` | `str` | Optional | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. This will be 'Fota' for the Software Management Services callback. |

## Example

```python
from verizon.models.fota_v1_callback_registration_result import FotaV1CallbackRegistrationResult

fota_v1_callback_registration_result = FotaV1CallbackRegistrationResult(
    account_name='0204563412-00001',
    service_name='Fota'
)
```

