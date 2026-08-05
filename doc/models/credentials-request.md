
# Credentials Request

## Structure

`CredentialsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ecpd` | `str` | Required | Enterprise Customer Profile ID |
| `account_number` | `str` | Required | Billing Account Number |
| `items` | [`List[DeviceCredentialRequestItem]`](../../doc/models/device-credential-request-item.md) | Required | List of devices (1-50 items)<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `50` |

## Example

```python
from verizon.models.credentials_request import CredentialsRequest
from verizon.models.device_credential_request_item import DeviceCredentialRequestItem

credentials_request = CredentialsRequest(
    ecpd='3161585',
    account_number='0844021539-00001',
    items=[
        DeviceCredentialRequestItem(
            imei='221000008775573'
        )
    ]
)
```

