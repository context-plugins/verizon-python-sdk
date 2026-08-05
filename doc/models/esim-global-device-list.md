
# ESIM Global Device List

## Structure

`ESIMGlobalDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric name of the account. |
| `provisioning_status_filter` | [`ProvisioningStatusFilterEnum`](../../doc/models/provisioning-status-filter-enum.md) | Optional | The last status of the device as a list filter. |
| `profile_status_filter` | [`ProfileStatusFilterEnum`](../../doc/models/profile-status-filter-enum.md) | Optional | The last status of the device's profile as a filter. |
| `carrier_name_filter` | `str` | Optional | The cellular service provider. |
| `device_filter` | List[[eSIMDeviceId](../../doc/models/esim-device-id.md) \| [DeviceId2](../../doc/models/device-id-2.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example

```python
from verizon.models.esim_device_id import ESIMDeviceId
from verizon.models.esim_global_device_list import ESIMGlobalDeviceList
from verizon.models.profile_status_filter_enum import ProfileStatusFilterEnum
from verizon.models.provisioning_status_filter_enum import ProvisioningStatusFilterEnum

e_sim_global_device_list = ESIMGlobalDeviceList(
    account_name='0000123456-00001',
    provisioning_status_filter=ProvisioningStatusFilterEnum.DEACTIVE,
    profile_status_filter=ProfileStatusFilterEnum.DELETE,
    carrier_name_filter='VerizonWireless',
    device_filter=[
        ESIMDeviceId(
            id='id4',
            kind='kind2'
        ),
        ESIMDeviceId(
            id='id4',
            kind='kind2'
        )
    ]
)
```

