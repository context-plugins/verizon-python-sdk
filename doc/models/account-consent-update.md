
# Account Consent Update

## Structure

`AccountConsentUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric name of the account, including leading zeros. |
| `all_device_consent` | `int` | Optional | The consent setting to use for all the devices in the account. |

## Example

```python
from verizon.models.account_consent_update import AccountConsentUpdate

account_consent_update = AccountConsentUpdate(
    account_name='0000123456-00001',
    all_device_consent=0
)
```

