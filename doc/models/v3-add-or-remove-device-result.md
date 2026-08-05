
# V3 Add or Remove Device Result

Add or remove devices to existing upgrade information.

## Structure

`V3AddOrRemoveDeviceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `campaign_id` | `str` | Required | Campaign identifier. |
| `device_list` | [`List[V3DeviceListItem]`](../../doc/models/v3-device-list-item.md) | Required | Array of devices changed. |

## Example

```python
from verizon.models.v3_add_or_remove_device_result import V3AddOrRemoveDeviceResult
from verizon.models.v3_device_list_item import V3DeviceListItem

v3_add_or_remove_device_result = V3AddOrRemoveDeviceResult(
    account_name='0000123456-00001',
    campaign_id='f858b8c4-2153-11ec-8c44-aeb16d1aa652',
    device_list=[
        V3DeviceListItem(
            device_id='15-digit IMEI',
            status='AddDeviceSucceed',
            reason='Device added Successfully'
        )
    ]
)
```

