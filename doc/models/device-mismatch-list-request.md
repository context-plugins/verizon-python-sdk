
# Device Mismatch List Request

Request to list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time frame.

## Structure

`DeviceMismatchListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`DateFilter`](../../doc/models/date-filter.md) | Required | Filter out the dates. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | A list of specific devices that you want to check, specified by ICCID or MDN. |
| `account_name` | `str` | Optional | The account that you want to search for mismatched devices. If you don't specify an accountName, the search includes all devices to which you have access. |
| `group_name` | `str` | Optional | The name of a device group, to only include devices in that group. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.date_filter import DateFilter
from verizon.models.device_id import DeviceId
from verizon.models.device_mismatch_list_request import DeviceMismatchListRequest

device_mismatch_list_request = DeviceMismatchListRequest(
    filter=DateFilter(
        earliest='2020-05-01T15:00:00-08:00Z',
        latest='2020-07-30T15:00:00-08:00Z'
    ),
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='8914800000080078',
                    kind='ICCID'
                ),
                DeviceId(
                    id='5096300587',
                    kind='MDN'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    account_name='0342077109-00001',
    group_name='groupName8'
)
```

