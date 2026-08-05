
# Response to Usage Query

## Structure

`ResponseToUsageQuery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hasmoredata` | `bool` | Optional | - |
| `device_id` | [`ReadySimDeviceId`](../../doc/models/ready-sim-device-id.md) | Optional | - |
| `usage_history` | [`List[UsageHistory]`](../../doc/models/usage-history.md) | Optional | - |

## Example

```python
from verizon.models.ready_sim_device_id import ReadySimDeviceId
from verizon.models.response_to_usage_query import ResponseToUsageQuery
from verizon.models.usage_history import UsageHistory

response_to_usage_query = ResponseToUsageQuery(
    hasmoredata=False,
    device_id=ReadySimDeviceId(
        kind='kind8',
        id='id0'
    ),
    usage_history=[
        UsageHistory(
            bytes_used=76,
            serviceplan='serviceplan2',
            sms_used=176,
            mo_sms=230,
            mt_sms=18
        ),
        UsageHistory(
            bytes_used=76,
            serviceplan='serviceplan2',
            sms_used=176,
            mo_sms=230,
            mt_sms=18
        )
    ]
)
```

