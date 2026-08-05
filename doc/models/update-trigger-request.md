
# Update Trigger Request

## Structure

`UpdateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `active` | `bool` | Optional | - |
| `anomaly_trigger_request` | [`AnomalyTriggerRequest`](../../doc/models/anomaly-trigger-request.md) | Optional | The details of the UsageAnomaly trigger. |
| `cycle_type` | [`CycleTypeEnum`](../../doc/models/cycle-type-enum.md) | Optional | - |
| `data_trigger_request` | [`DataTriggerRequest`](../../doc/models/data-trigger-request.md) | Optional | - |
| `group_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `promo_alert_trigger_request` | [`PromoAlertTriggerRequest`](../../doc/models/promo-alert-trigger-request.md) | Optional | - |
| `session_trigger_request` | [`SessionTriggerRequest`](../../doc/models/session-trigger-request.md) | Optional | - |
| `sms_trigger_request` | [`SMSTriggerRequest`](../../doc/models/sms-trigger-request.md) | Optional | - |
| `trigger_category` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `trigger_id` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `trigger_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.cycle_type_enum import CycleTypeEnum
from verizon.models.data_trigger_request import DataTriggerRequest
from verizon.models.update_trigger_request import UpdateTriggerRequest

update_trigger_request = UpdateTriggerRequest(
    account_name='accountName2',
    active=False,
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    ),
    cycle_type=CycleTypeEnum.CYCLEONE,
    data_trigger_request=DataTriggerRequest(
        comparator='comparator2',
        threshold=100,
        threshold_unit='thresholdUnit6'
    )
)
```

