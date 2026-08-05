
# Change PWN Device State Response

Response to change PWN device state

## Structure

`ChangePWNDeviceStateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | A unique string that associates the request with the results that are sent via a callback service. |

## Example

```python
from verizon.models.change_pwn_device_state_response import ChangePWNDeviceStateResponse

change_pwn_device_state_response = ChangePWNDeviceStateResponse(
    request_id='24da9f9a-d110-4a54-86b4-93fb76aab83c'
)
```

