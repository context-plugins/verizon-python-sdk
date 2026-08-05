
# Account Details

## Structure

`AccountDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `account_number` | `str` | Optional | The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `organization_name` | `str` | Optional | user defined name of organization<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |
| `is_provisioning_allowed` | `bool` | Optional | Flag set to indicate if account details can be edited or not. Default is "true". |
| `carriers` | [`List[Carrier]`](../../doc/models/carrier.md) | Optional | - |
| `features` | [`List[Feature]`](../../doc/models/feature.md) | Optional | - |
| `service_plans` | [`List[CarrierServicePlan]`](../../doc/models/carrier-service-plan.md) | Optional | - |

## Example

```python
from verizon.models.account_details import AccountDetails
from verizon.models.carrier import Carrier

account_details = AccountDetails(
    account_name='0000123456-00001',
    account_number='0000123456-00001',
    organization_name='organizationName4',
    is_provisioning_allowed=False,
    carriers=[
        Carrier(
            carriers='carriers0'
        ),
        Carrier(
            carriers='carriers0'
        )
    ]
)
```

