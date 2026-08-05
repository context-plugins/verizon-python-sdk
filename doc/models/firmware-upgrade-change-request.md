
# Firmware Upgrade Change Request

List of devices to add or remove.

## Structure

`FirmwareUpgradeChangeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`FirmwareTypeListEnum`](../../doc/models/firmware-type-list-enum.md) | Required | Possible values are `append` or `remove` |
| `device_list` | `List[str]` | Required | The IMEIs of the devices. |

## Example

```python
from verizon.models.firmware_type_list_enum import FirmwareTypeListEnum
from verizon.models.firmware_upgrade_change_request import FirmwareUpgradeChangeRequest

firmware_upgrade_change_request = FirmwareUpgradeChangeRequest(
    mtype=FirmwareTypeListEnum.APPEND,
    device_list=[
        '15-digit IMEI',
        '15-digit IMEI'
    ]
)
```

