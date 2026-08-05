
# Consent Delete Request

## Structure

`ConsentDeleteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier. |
| `device_list` | `List[str]` | Optional | Device ID list. |

## Example

```python
from verizon.models.consent_delete_request import ConsentDeleteRequest

consent_delete_request = ConsentDeleteRequest(
    account_name='MyAccount-1',
    device_list=[
        'deviceList6',
        'deviceList7'
    ]
)
```

