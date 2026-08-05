
# Retrieve Monitors Request

## Structure

`RetrieveMonitorsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | The devices for which you want to restore service, specified by device identifier. |
| `monitor_type` | `str` | Optional | The name of a billing account. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.device_id import DeviceId
from verizon.models.retrieve_monitors_request import RetrieveMonitorsRequest

retrieve_monitors_request = RetrieveMonitorsRequest(
    account_name='0868924207-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='89148000000800139708',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    monitor_type='monitorType'
)
```

