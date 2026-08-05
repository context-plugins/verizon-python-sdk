
# Security Subscription Result

Response for a subscription request.

## Structure

`SecuritySubscriptionResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of a billing account. |
| `subscription_list` | [`List[SecuritySubscription]`](../../doc/models/security-subscription.md) | Optional | The list of SKU numbers and counts for each license type specified in the request.<br><br>**Constraints**: *Maximum Items*: `5` |

## Example

```python
from verizon.models.extended_attributes import ExtendedAttributes
from verizon.models.security_subscription import SecuritySubscription
from verizon.models.security_subscription_result import SecuritySubscriptionResult

security_subscription_result = SecuritySubscriptionResult(
    account_name='000012345600001',
    subscription_list=[
        SecuritySubscription(
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
    ]
)
```

