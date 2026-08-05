
# Get Device List with Profiles Request

## Structure

`GetDeviceListWithProfilesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9\-]{3,32}$` |
| `provisioning_status_filter` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `profile_status_filter` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `carrier_name_filter` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `device_filter` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `50` |

## Example

```python
from verizon.models.get_device_list_with_profiles_request import GetDeviceListWithProfilesRequest
from verizon.models.gio_device_id import GIODeviceId

get_device_list_with_profiles_request = GetDeviceListWithProfilesRequest(
    account_name='0000123456-00001',
    provisioning_status_filter='ACTIVE',
    profile_status_filter='UNKNOWN',
    carrier_name_filter='carrierNameFilter8',
    device_filter=[
        GIODeviceId(
            kind='kind2',
            id='id4'
        ),
        GIODeviceId(
            kind='kind2',
            id='id4'
        )
    ]
)
```

