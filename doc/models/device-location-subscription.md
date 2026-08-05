
# Device Location Subscription

## Structure

`DeviceLocationSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `loc_type` | `str` | Optional | Location service license type. |
| `max_allowance` | `str` | Optional | The number of billable location requests allowed per billing cycle. |
| `purchase_time` | `str` | Optional | Location service purchase time. |

## Example

```python
from verizon.models.device_location_subscription import DeviceLocationSubscription

device_location_subscription = DeviceLocationSubscription(
    account_name='2024009649-00001',
    loc_type='TS-LOC-COARSE-CellID-5K',
    max_allowance='5000',
    purchase_time='2017-05-10 06:25:25.171 +0000 UTC'
)
```

