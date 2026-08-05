
# Device Level Update Trigger Request

## Structure

`DeviceLevelUpdateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned UUID of the trigger |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`DataTrigger2`](../../doc/models/data-trigger-2.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |
| `active` | [`ActiveEnum`](../../doc/models/active-enum.md) | Optional | A flag to indicate of the trigger is active, true, or not, false |

## Example

```python
from verizon.models.active_enum import ActiveEnum
from verizon.models.comparitor_enum import ComparitorEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger_2 import DataTrigger2
from verizon.models.device_group_filter import DeviceGroupFilter
from verizon.models.device_group_filter_criteria import DeviceGroupFilterCriteria
from verizon.models.device_level_update_trigger_request import DeviceLevelUpdateTriggerRequest
from verizon.models.threshold_unit_enum import ThresholdUnitEnum
from verizon.models.trigger_category_enum import TriggerCategoryEnum

device_level_update_trigger_request = DeviceLevelUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.ACCOUNTUSAGE,
    data_trigger=DataTrigger2(
        device_group=DeviceGroupFilterCriteria(
            filter_criteria=DeviceGroupFilter(
                device_group_name='deviceGroupName4',
                individual_or_combined='IndividualOrCombined4',
                account_name='accountName0'
            )
        ),
        condition_type=ConditionTypeEnum.AGING,
        comparitor=ComparitorEnum.EQ,
        threshold=222,
        threshold_unit=ThresholdUnitEnum.MB
    ),
    active=ActiveEnum.TRUE
)
```

