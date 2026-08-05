
# Delete Subscription Request

The subscription to delete.

## Structure

`DeleteSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountidentifier` | [`AccountIdentifier`](../../doc/models/account-identifier.md) | Optional | The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`. |
| `resourceidentifier` | [`ResourceIdentifier`](../../doc/models/resource-identifier.md) | Optional | The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}. |

## Example

```python
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.delete_subscription_request import DeleteSubscriptionRequest
from verizon.models.resource_identifier import ResourceIdentifier

delete_subscription_request = DeleteSubscriptionRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='1223334444-00001'
    ),
    resourceidentifier=ResourceIdentifier(
        id='f8b112df-739c-6236-f059-106c67bafd99',
        imei='imei2'
    )
)
```

