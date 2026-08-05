
# The I Dresourceand Device ID

## Structure

`TheIDresourceandDeviceID`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `deviceid` | `str` | Optional | This is a UUID value of the device created when the device is onboarded |

## Example

```python
from verizon.models.the_i_dresourceand_device_id import TheIDresourceandDeviceID

the_i_dresourceand_device_id = TheIDresourceandDeviceID(
    id='id0',
    deviceid='The UUID of the device'
)
```

