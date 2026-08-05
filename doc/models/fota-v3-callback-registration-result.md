
# Fota V3 Callback Registration Result

Callback registration information.

## Structure

`FotaV3CallbackRegistrationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Callback URL. |

## Example

```python
from verizon.models.fota_v3_callback_registration_result import FotaV3CallbackRegistrationResult

fota_v3_callback_registration_result = FotaV3CallbackRegistrationResult(
    url='https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'
)
```

