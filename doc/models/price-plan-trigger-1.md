
# Price Plan Trigger 1

## Structure

`PricePlanTrigger1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_group_share` | [`AccountGroupShareIndividual1`](../../doc/models/account-group-share-individual-1.md) | Optional | - |
| `account_share` | [`AccountShareFilterCriteria`](../../doc/models/account-share-filter-criteria.md) | Optional | - |
| `condition` | [conditionType](../../doc/models/condition-type-enum.md) \| [conditionObjectCall](../../doc/models/condition-object-call.md) \| None | Optional | This is a container for any-of cases. |
| `change_plan` | `bool` | Optional | a flag to set if the trigger changes service plans, true, or not, false |
| `change_plan_details` | [`ChangePlanDetails`](../../doc/models/change-plan-details.md) | Optional | The service plan code to switch to |
| `pay_as_you_go` | [`PayAsYouGoFilterCriteria`](../../doc/models/pay-as-you-go-filter-criteria.md) | Optional | - |
| `action` | [`Actionobject`](../../doc/models/actionobject.md) | Optional | - |
| `stand_alone` | [`FiltercriteriaObjectCall`](../../doc/models/filtercriteria-object-call.md) | Optional | - |

## Example

```python
from verizon.models.account_group_share_action import AccountGroupShareAction
from verizon.models.account_group_share_condition import AccountGroupShareCondition
from verizon.models.account_group_share_filter import AccountGroupShareFilter
from verizon.models.account_group_share_filter_criteria import AccountGroupShareFilterCriteria
from verizon.models.account_group_share_individual_1 import AccountGroupShareIndividual1
from verizon.models.account_share_filter_criteria import AccountShareFilterCriteria
from verizon.models.account_share_filter_criteria_1 import AccountShareFilterCriteria1
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.condition_action_enum import ConditionActionEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.notify import Notify
from verizon.models.price_plan_trigger_1 import PricePlanTrigger1

price_plan_trigger_1 = PricePlanTrigger1(
    account_group_share=AccountGroupShareIndividual1(
        account_group_share_individual=AccountGroupShareFilterCriteria(
            filter_criteria=AccountGroupShareFilter(
                rate_plan_group_id=202
            ),
            condition=AccountGroupShareCondition(
                action=ConditionActionEnum.NOTIFY
            ),
            action=AccountGroupShareAction(
                notify=Notify(
                    alert_type='alertType8',
                    threshold=[
                        Carriercode1(
                            carrier_code='carrierCode4',
                            percentage=AllowanceThreshold(
                                percentage_50=False,
                                percentage_75=False,
                                percentage_90=False,
                                percentage_100=False
                            )
                        ),
                        Carriercode1(
                            carrier_code='carrierCode4',
                            percentage=AllowanceThreshold(
                                percentage_50=False,
                                percentage_75=False,
                                percentage_90=False,
                                percentage_100=False
                            )
                        ),
                        Carriercode1(
                            carrier_code='carrierCode4',
                            percentage=AllowanceThreshold(
                                percentage_50=False,
                                percentage_75=False,
                                percentage_90=False,
                                percentage_100=False
                            )
                        )
                    ]
                )
            )
        )
    ),
    account_share=AccountShareFilterCriteria(
        filter_criteria=AccountShareFilterCriteria1(
            carrier_service_plan_code='carrierServicePlanCode4',
            account_name_list=[
                'accountNameList7',
                'accountNameList8'
            ]
        )
    ),
    condition=ConditionTypeEnum.USAGEALLOWANCE,
    change_plan=True,
    change_plan_details=ChangePlanDetails(
        to_carrier_service_plan_code='toCarrierServicePlanCode2'
    )
)
```

