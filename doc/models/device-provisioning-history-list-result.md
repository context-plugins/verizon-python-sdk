
# Device Provisioning History List Result

Response to return the provisioning history of a specified device during a specified time period.

## Structure

`DeviceProvisioningHistoryListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. |
| `provisioning_history` | [`List[ProvisioningHistory]`](../../doc/models/provisioning-history.md) | Optional | The provisioning history of a specified device during a specified time period. |

## Example

```python
from verizon.models.device_provisioning_history_list_result import DeviceProvisioningHistoryListResult
from verizon.models.provisioning_history import ProvisioningHistory

device_provisioning_history_list_result = DeviceProvisioningHistoryListResult(
    has_more_data=False,
    provisioning_history=[
        ProvisioningHistory(
            occurred_at='2015-12-17T13:56:13-05:00',
            status='Success',
            event_by='Harry Potter',
            event_type='Activation Confirmed',
            mdn='',
            msisdn='15086303371',
            service_plan='Tablet5GB',
            extended_attributes=[]
        )
    ]
)
```

