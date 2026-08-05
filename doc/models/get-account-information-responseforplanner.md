
# Get Account Information Responseforplanner

## Structure

`GetAccountInformationResponseforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `account_number` | `str` | Optional | The numeric name of the account, including leading zeros. |
| `carriers` | `List[str]` | Optional | The list of carrier names with profiles.<br><br>**Constraints**: *Maximum Items*: `5` |
| `features` | `List[str]` | Optional | a list of features associated with the resident profiles.<br><br>**Constraints**: *Maximum Items*: `50` |
| `ip_pools` | [`List[IPPoolforplanner]`](../../doc/models/ip-poolforplanner.md) | Optional | **Constraints**: *Maximum Items*: `50` |
| `is_provisioning_allowed` | `bool` | Optional | A flag indicating if provisioning is allowed (true) or provisioning is locked (false). |
| `organization_name` | `str` | Optional | The user assigned organization name. |
| `service_plans` | [`List[ServicePlanResponseforplanner]`](../../doc/models/service-plan-responseforplanner.md) | Optional | A list of service plans associated with the resident profiles.<br><br>**Constraints**: *Maximum Items*: `10` |

## Example

```python
from verizon.models.get_account_information_responseforplanner import GetAccountInformationResponseforplanner
from verizon.models.ip_poolforplanner import IPPoolforplanner

get_account_information_responseforplanner = GetAccountInformationResponseforplanner(
    account_name='accountName4',
    account_number='0000123456-00001',
    carriers=[
        'carriers6',
        'carriers7'
    ],
    features=[
        'features1',
        'features2'
    ],
    ip_pools=[
        IPPoolforplanner(
            is_default_pool=False,
            pool_name='poolName2',
            pool_type='poolType6'
        ),
        IPPoolforplanner(
            is_default_pool=False,
            pool_name='poolName2',
            pool_type='poolType6'
        )
    ]
)
```

