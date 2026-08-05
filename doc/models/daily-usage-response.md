
# Daily Usage Response

## Structure

`DailyUsageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | A flag set to indicate if there is more than one page of data returned by the query (true) or if only one page of data returned (false) |
| `device_id` | [`GIODeviceId`](../../doc/models/gio-device-id.md) | Optional | - |
| `usage_history` | [`List[DailyUsageHistory]`](../../doc/models/daily-usage-history.md) | Optional | - |

## Example

```python
from verizon.models.daily_usage_history import DailyUsageHistory
from verizon.models.daily_usage_response import DailyUsageResponse
from verizon.models.extended_attribute import ExtendedAttribute
from verizon.models.gio_device_id import GIODeviceId

daily_usage_response = DailyUsageResponse(
    has_more_data=False,
    device_id=GIODeviceId(
        kind='kind8',
        id='id0'
    ),
    usage_history=[
        DailyUsageHistory(
            bytes_used='bytesUsed2',
            extended_attributes=[
                ExtendedAttribute(
                    key='key8',
                    value='value0'
                ),
                ExtendedAttribute(
                    key='key8',
                    value='value0'
                ),
                ExtendedAttribute(
                    key='key8',
                    value='value0'
                )
            ],
            service_plan='servicePlan0',
            sms_used='smsUsed6',
            source='source4'
        ),
        DailyUsageHistory(
            bytes_used='bytesUsed2',
            extended_attributes=[
                ExtendedAttribute(
                    key='key8',
                    value='value0'
                ),
                ExtendedAttribute(
                    key='key8',
                    value='value0'
                ),
                ExtendedAttribute(
                    key='key8',
                    value='value0'
                )
            ],
            service_plan='servicePlan0',
            sms_used='smsUsed6',
            source='source4'
        )
    ]
)
```

