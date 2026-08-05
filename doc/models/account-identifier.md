
# Account Identifier

The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`.

## Structure

`AccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billingaccountid` | `str` | Optional | - |

## Example

```python
from verizon.models.account_identifier import AccountIdentifier

account_identifier = AccountIdentifier(
    billingaccountid='0000000000-00001'
)
```

