
# Device Usage List Result

Response to return the daily network data usage of a single device during a specified time period.

## Structure

`DeviceUsageListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. |
| `usage_history` | [`List[Usage]`](../../doc/models/usage.md) | Optional | Placeholder. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.device_usage_list_result import DeviceUsageListResult
from verizon.models.usage import Usage

device_usage_list_result = DeviceUsageListResult(
    has_more_data=False,
    usage_history=[
        Usage(
            bytes_used=4096,
            extended_attributes=[
                CustomFields(
                    key='MoSms',
                    value='0'
                )
            ],
            service_plan='servicePlan0',
            sms_used=0,
            source='Raw Usage',
            timestamp='2020-12-01T00:00:00Z'
        )
    ]
)
```

