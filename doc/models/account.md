
# Account

Returns information about a specified account.

## Structure

`Account`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of the account. |
| `account_number` | `str` | Optional | The billing number of the account. |
| `organization_name` | `str` | Optional | The name of the organization that the account is part of. |
| `is_provisioning_allowed` | `bool` | Optional | True if devices can be added to the account and activated with a single request. False if devices must be added to the account before they can be activated. |
| `carriers` | `List[str]` | Optional | The names of all carriers for the account. |
| `features` | `List[str]` | Optional | The names of features that are enabled for the account. |
| `i_p_pools` | [`List[IPPool]`](../../doc/models/ip-pool.md) | Optional | Array of IP pools that are available to the account. |
| `service_plans` | [`List[ServicePlan]`](../../doc/models/service-plan.md) | Optional | Array of service plans that are available to the account. |

## Example

```python
from verizon.models.account import Account
from verizon.models.ip_pool import IPPool
from verizon.models.service_plan import ServicePlan

account = Account(
    account_name='Chintan_CPNStaticBulk',
    account_number='1234567890-77777',
    organization_name='ChintanCPNBulk',
    is_provisioning_allowed=True,
    carriers=[
        'Verizon Wireless'
    ],
    features=[
        'Static IP',
        'Dynamic IP',
        'Customer PN'
    ],
    i_p_pools=[
        IPPool(
            pool_name='ACMESTATIC001',
            pool_type='Static IP',
            is_default_pool=True
        ),
        IPPool(
            pool_name='ACMEDYNAMIC001',
            pool_type='Dynamic IP',
            is_default_pool=False
        )
    ],
    service_plans=[
        ServicePlan(
            carrier_service_plan_code='',
            code='92876',
            extended_attributes=[],
            name='',
            size_kb=1
        ),
        ServicePlan(
            carrier_service_plan_code='',
            code='92876',
            extended_attributes=[],
            name='',
            size_kb=1
        )
    ]
)
```

