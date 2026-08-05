
# Change Configuration Request

The request body identifies the device and the values to set.

## Structure

`ChangeConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountidentifier` | [`AccountIdentifier`](../../doc/models/account-identifier.md) | Optional | The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`. |
| `resourceidentifier` | [`ResourceIdentifier`](../../doc/models/resource-identifier.md) | Optional | The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}. |
| `configuration` | [`Configuration`](../../doc/models/configuration.md) | Optional | List of the field names and values to set. |

## Example

```python
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.change_configuration_request import ChangeConfigurationRequest
from verizon.models.configuration import Configuration
from verizon.models.resource_identifier import ResourceIdentifier

change_configuration_request = ChangeConfigurationRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='1223334444-00001'
    ),
    resourceidentifier=ResourceIdentifier(
        id='f8b112df-739c-6236-f059-106c67bafd99',
        imei='imei2'
    ),
    configuration=Configuration(
        frequency='Low'
    )
)
```

