
# Query Subscription Request

Fields and values to match.

## Structure

`QuerySubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountidentifier` | [`AccountIdentifier`](../../doc/models/account-identifier.md) | Optional | The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`. |
| `selection` | `Dict[str, str]` | Optional | A comma-separated list of properties and comparator values to match against subscriptions in the ThingSpace account. See Working with Query Filters for more information. If the request does not include `$selection`, the response will include all subscriptions to which the requesting user has access. |
| `resourceidentifier` | [`ResourceIdentifier`](../../doc/models/resource-identifier.md) | Optional | The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}. |

## Example

```python
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.query_subscription_request import QuerySubscriptionRequest
from verizon.models.resource_identifier import ResourceIdentifier

query_subscription_request = QuerySubscriptionRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='1223334444-00001'
    ),
    selection={
        'key0': '$selection7',
        'key1': '$selection8',
        'key2': '$selection9'
    },
    resourceidentifier=ResourceIdentifier(
        id='dd1682d3-2d80-cefc-f3ee-25154800beff',
        imei='imei2'
    )
)
```

