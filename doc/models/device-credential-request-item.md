
# Device Credential Request Item

## Structure

`DeviceCredentialRequestItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Required | 15-digit alphanumeric identifier<br><br>**Constraints**: *Pattern*: `^[A-Za-z0-9]{15}$` |

## Example

```python
from verizon.models.device_credential_request_item import DeviceCredentialRequestItem

device_credential_request_item = DeviceCredentialRequestItem(
    imei='221000008775573'
)
```

