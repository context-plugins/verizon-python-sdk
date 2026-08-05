
# Dto Bulk Update

## Structure

`DtoBulkUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `resourceidentifiers` | [`List[TheIDresourceandDeviceID]`](../../doc/models/the-i-dresourceand-device-id.md) | Optional | - |
| `smartalert` | [`BulkUpdateSmartalert`](../../doc/models/bulk-update-smartalert.md) | Optional | - |

## Example

```python
from verizon.models.bulk_update_smartalert import BulkUpdateSmartalert
from verizon.models.dto_bulk_update import DtoBulkUpdate
from verizon.models.the_i_dresourceand_device_id import TheIDresourceandDeviceID

dto_bulk_update = DtoBulkUpdate(
    accountname='0000123456-00001',
    resourceidentifiers=[
        TheIDresourceandDeviceID(
            id='ee70a869-eeee-ffff-gggg-07c14c31f96e',
            deviceid='deviceid4'
        ),
        TheIDresourceandDeviceID(
            id='id4',
            deviceid='131501ff-eeee-ffff-gggg-647d19179a12'
        )
    ],
    smartalert=BulkUpdateSmartalert(
        name='name0'
    )
)
```

