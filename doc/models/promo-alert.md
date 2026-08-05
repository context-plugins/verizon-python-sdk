
# Promo Alert

## Structure

`PromoAlert`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`List[ReadySimServicePlan]`](../../doc/models/ready-sim-service-plan.md) | Optional | - |
| `condition` | [`List[Keyschunk2]`](../../doc/models/keyschunk-2.md) | Optional | - |
| `enable_promo_exp` | `bool` | Optional | - |

## Example

```python
from verizon.models.keyschunk_2 import Keyschunk2
from verizon.models.promo_alert import PromoAlert
from verizon.models.ready_sim_service_plan import ReadySimServicePlan

promo_alert = PromoAlert(
    filter_criteria=[
        ReadySimServicePlan(
            service_plan='servicePlan4'
        ),
        ReadySimServicePlan(
            service_plan='servicePlan4'
        ),
        ReadySimServicePlan(
            service_plan='servicePlan4'
        )
    ],
    condition=[
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        ),
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        ),
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        )
    ],
    enable_promo_exp=True
)
```

