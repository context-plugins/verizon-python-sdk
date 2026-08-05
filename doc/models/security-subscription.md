
# Security Subscription

Subscription of the device.

## Structure

`SecuritySubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extended_attributes` | [`List[ExtendedAttributes]`](../../doc/models/extended-attributes.md) | Optional | Attributes of the subscription.<br><br>**Constraints**: *Maximum Items*: `5` |
| `license_assigned` | `int` | Optional | The total number of licenses for this license type that are assigned to device SIMs.<br><br>**Constraints**: `>= 0`, `<= 10` |
| `license_available` | `int` | Optional | The total number of licenses for this license type that are available to assign to device SIMs.<br><br>**Constraints**: `>= 0`, `<= 10` |
| `license_purchased` | `int` | Optional | The total number of licenses purchased for the license type.<br><br>**Constraints**: `>= 0`, `<= 10` |
| `license_type` | `str` | Optional | The license type associated with the skuNumber. |
| `sku_number` | `str` | Optional | The skuNumber that identifies the license type. |

## Example

```python
from verizon.models.extended_attributes import ExtendedAttributes
from verizon.models.security_subscription import SecuritySubscription

security_subscription = SecuritySubscription(
    extended_attributes=[
        ExtendedAttributes(
            key='key8',
            value='value0'
        ),
        ExtendedAttributes(
            key='key8',
            value='value0'
        )
    ],
    license_assigned=7,
    license_available=1,
    license_purchased=9,
    license_type='Flexible Bundle',
    sku_number='TS-BUNDLE-KTO-SIMSEC-MRC'
)
```

