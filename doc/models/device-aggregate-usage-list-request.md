
# Device Aggregate Usage List Request

Request to list device aggregate usage.

## Structure

`DeviceAggregateUsageListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `str` | Required | The beginning of the reporting period. The startTime cannot be more than 6 months before the current date. |
| `end_time` | `str` | Required | The end of the reporting period. The endTime date must be within on month of the startTime date. |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | One or more devices for which you want aggregate data, specified by device ID. |
| `account_name` | `str` | Optional | The name of a billing account. |
| `group_name` | `str` | Optional | The name of a device group, if you want to only include devices in that group. |
| `label` | [`List[Label]`](../../doc/models/label.md) | Optional | **Constraints**: *Maximum Items*: `50` |

## Example

```python
from verizon.models.device_aggregate_usage_list_request import DeviceAggregateUsageListRequest
from verizon.models.device_id import DeviceId
from verizon.models.label import Label

device_aggregate_usage_list_request = DeviceAggregateUsageListRequest(
    start_time='2021-08-01T00:00:00-06:00',
    end_time='2021-08-30T00:00:00-06:00',
    device_ids=[
        DeviceId(
            id='84258000000891490087',
            kind='ICCID'
        )
    ],
    account_name='9992330389-00001',
    group_name='groupName8',
    label=[
        Label(
            name='name0',
            value='value2'
        )
    ]
)
```

