
# Fota V3 Subscription

Information for licenses applied to devices.

## Structure

`FotaV3Subscription`

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
from verizon.models.fota_v3_subscription import FotaV3Subscription

fota_v3_subscription = FotaV3Subscription(
    account_name='0000123456-000001',
    purchase_type='TS-HFOTA-EVNT,TS-HFOTA-MRC',
    license_count=500,
    license_used_count=400,
    update_time='2020-09-17T21:11:32.170Z'
)
```

