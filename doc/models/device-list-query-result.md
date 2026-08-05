
# Device List Query Result

List of devices.

## Structure

`DeviceListQueryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `has_more_data` | `bool` | Optional | True if there are more devices to retrieve. |
| `last_seen_device_id` | `int` | Optional | If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false. |
| `device_list` | [`List[DeviceListQueryItem]`](../../doc/models/device-list-query-item.md) | Optional | The list of devices in the account. |

## Example

```python
from verizon.models.device_list_query_item import DeviceListQueryItem
from verizon.models.device_list_query_result import DeviceListQueryResult

device_list_query_result = DeviceListQueryResult(
    account_name='0242078698-00001',
    has_more_data=True,
    last_seen_device_id=900000000001000,
    device_list=[
        DeviceListQueryItem(
            device_id='900000000000001',
            mdn='0000040881',
            model='Model-A',
            make='Verizon',
            firmware='VerizonFirmwareVersion-01',
            fota_eligible=True,
            license_assigned=True,
            upgrade_time='2018-03-03T16:03:33.000Z'
        ),
        DeviceListQueryItem(
            device_id='900000000000999',
            mdn='0000041879',
            model='Model-A',
            make='Verizon',
            firmware='VerizonFirmwareVersion-01',
            fota_eligible=True,
            license_assigned=True,
            upgrade_time='2018-03-03T16:03:33.000Z'
        ),
        DeviceListQueryItem(
            device_id='900000000001000',
            mdn='0000041880',
            model='Model-A',
            make='Verizon',
            firmware='VerizonFirmwareVersion-01',
            fota_eligible=True,
            license_assigned=True,
            upgrade_time='2018-03-03T16:03:33.000Z'
        )
    ]
)
```

