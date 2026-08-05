
# Search Device Event History Request

Search Device By Property resource definition.

## Structure

`SearchDeviceEventHistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountidentifier` | [`AccountIdentifier`](../../doc/models/account-identifier.md) | Required | The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`. |
| `selection` | `Dict[str, str]` | Optional | A comma-separated list of properties and comparator values to match against subscriptions in the ThingSpace account. See Working with Query Filters for more information. If the request does not include `$selection`, the response will include all subscriptions to which the requesting user has access. |
| `resourceidentifier` | [`ResourceIdentifier`](../../doc/models/resource-identifier.md) | Required | The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}. |
| `limitnumber` | `int` | Optional | The maximum number of events to include in the response. |
| `page` | `str` | Optional | The maximum number of events to include in the response. |

## Example

```python
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.resource_identifier import ResourceIdentifier
from verizon.models.search_device_event_history_request import SearchDeviceEventHistoryRequest

search_device_event_history_request = SearchDeviceEventHistoryRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='0000000000-00001'
    ),
    resourceidentifier=ResourceIdentifier(
        id='2e61a17d-8fd1-6816-e995-e4c2528bf535',
        imei='imei2'
    ),
    selection={
        'addressscheme': 'streamawsiot'
    },
    limitnumber=2,
    page='$page8'
)
```

