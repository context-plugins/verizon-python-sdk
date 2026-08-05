
# Create Trigger Request

## Structure

`CreateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `anomaly_trigger_request` | [`AnomalyTriggerRequest`](../../doc/models/anomaly-trigger-request.md) | Optional | The details of the UsageAnomaly trigger. |
| `data_trigger_request` | [`DataTriggerRequest`](../../doc/models/data-trigger-request.md) | Optional | - |
| `group_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `session_trigger_request` | [`SessionTriggerRequest`](../../doc/models/session-trigger-request.md) | Optional | - |
| `sms_trigger_request` | [`SMSTriggerRequest`](../../doc/models/sms-trigger-request.md) | Optional | - |
| `trigger_category` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `trigger_cycle` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.create_trigger_request import CreateTriggerRequest
from verizon.models.data_trigger_request import DataTriggerRequest

create_trigger_request = CreateTriggerRequest(
    account_name='accountName6',
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    ),
    data_trigger_request=DataTriggerRequest(
        comparator='comparator2',
        threshold=100,
        threshold_unit='thresholdUnit6'
    ),
    group_name='groupName8',
    name='name2'
)
```

