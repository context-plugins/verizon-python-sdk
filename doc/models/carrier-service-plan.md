
# Carrier Service Plan

## Structure

`CarrierServicePlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the service plan<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |
| `code` | `str` | Optional | The inventory name or system name of the service plan<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |
| `size_kb` | `str` | Optional | The ammount of space the service plan will occupy on the Subscriber Information Module (SIM)<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |
| `carrier_service_plan_code` | `str` | Optional | The billing record ID. This can be numeric, alpha or alphanumeric.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example

```python
from verizon.models.carrier_service_plan import CarrierServicePlan

carrier_service_plan = CarrierServicePlan(
    name='name8',
    code='code6',
    size_kb='sizeKb2',
    carrier_service_plan_code='carrierServicePlanCode6'
)
```

