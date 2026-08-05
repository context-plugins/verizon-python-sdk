
# V1 Account Subscription

Account subscription information.

## Structure

`V1AccountSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `purchase_type` | `str` | Optional | Subscription models used by the account. |
| `license_count` | `int` | Optional | Number of monthly licenses in an MRC subscription. |
| `license_used_count` | `int` | Optional | Number of licenses currently assigned to devices. |
| `update_time` | `str` | Optional | The date and time of when the subscription was last updated. |

## Example

```python
from verizon.models.v1_account_subscription import V1AccountSubscription

v1_account_subscription = V1AccountSubscription(
    account_name='0402196254-00001',
    purchase_type='TS-HFOTA-EVNT,TS-HFOTA-MRC',
    license_count=9000,
    license_used_count=1000,
    update_time='2018-03-02T16:03:06.000Z'
)
```

