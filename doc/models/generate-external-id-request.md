
# Generate External ID Request

Authenticating account ID.

## Structure

`GenerateExternalIDRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountidentifier` | [`AccountIdentifier`](../../doc/models/account-identifier.md) | Optional | The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`. |

## Example

```python
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.generate_external_id_request import GenerateExternalIDRequest

generate_external_id_request = GenerateExternalIDRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='0000000000-00001'
    )
)
```

