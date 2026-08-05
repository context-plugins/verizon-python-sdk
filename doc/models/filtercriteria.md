
# Filtercriteria

## Structure

`Filtercriteria`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`List[ReadySimServicePlan]`](../../doc/models/ready-sim-service-plan.md) | Optional | - |

## Example

```python
from verizon.models.filtercriteria import Filtercriteria
from verizon.models.ready_sim_service_plan import ReadySimServicePlan

filtercriteria = Filtercriteria(
    filter_criteria=[
        ReadySimServicePlan(
            service_plan='servicePlan4'
        )
    ]
)
```

