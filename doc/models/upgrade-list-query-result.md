
# Upgrade List Query Result

Upgrade information.

## Structure

`UpgradeListQueryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_flag` | `bool` | Optional | True if there are more devices to retrieve. |
| `last_seen_upgrade_id` | `int` | Optional | If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false. |
| `report_list` | [`List[FirmwareUpgrade]`](../../doc/models/firmware-upgrade.md) | Optional | Array of upgrade objects with the specified status. |

## Example

```python
from verizon.models.firmware_upgrade import FirmwareUpgrade
from verizon.models.firmware_upgrade_device_list_item import FirmwareUpgradeDeviceListItem
from verizon.models.upgrade_list_query_result import UpgradeListQueryResult

upgrade_list_query_result = UpgradeListQueryResult(
    has_more_flag=False,
    last_seen_upgrade_id=4,
    report_list=[
        FirmwareUpgrade(
            id='3ac8c863-bde7-4f41-878e-dd5473e973bb',
            account_name='0242078689-00001',
            firmware_name='FOTA_Verizon_Model-A_01To02_HF',
            firmware_to='VerizonFirmwareVersion-02',
            start_date='2018-04-01',
            status='Queued',
            device_list=[
                FirmwareUpgradeDeviceListItem(
                    device_id='900000000000002',
                    status='Device Accepted',
                    result_reason='success'
                ),
                FirmwareUpgradeDeviceListItem(
                    device_id='900000000000003',
                    status='Device Accepted',
                    result_reason='success'
                )
            ]
        ),
        FirmwareUpgrade(
            id='efb8206b-2e88-4fdb-886d-31d8e87cd95f',
            account_name='0242078689-00001',
            firmware_name='FOTA_Verizon_Model-A_01To02_HF',
            firmware_to='VerizonFirmwareVersion-02',
            start_date='2018-04-01T16:03:00.000Z',
            status='Queued',
            device_list=[
                FirmwareUpgradeDeviceListItem(
                    device_id='900000000000008',
                    status='Device Accepted',
                    result_reason='success'
                )
            ]
        )
    ]
)
```

