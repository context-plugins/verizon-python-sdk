
# Change PWN Device Ipaddress Response

Response to change PWN device ip address.

## Structure

`ChangePWNDeviceIpaddressResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | A unique string that associates the request with the results that are sent via a callback service. |

## Example

```python
from verizon.models.change_pwn_device_ipaddress_response import ChangePWNDeviceIpaddressResponse

change_pwn_device_ipaddress_response = ChangePWNDeviceIpaddressResponse(
    request_id='24da9f9a-d110-4a54-86b4-93fb76aab83c'
)
```

