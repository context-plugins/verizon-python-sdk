
# Account Consent Create

## Structure

`AccountConsentCreate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[Any]` | Optional | An array of device identifiers |
| `account_name` | `str` | Optional | The numeric name of the account, including leading zeros. |

## Example

```python
import jsonpickle

from verizon.models.account_consent_create import AccountConsentCreate

account_consent_create = AccountConsentCreate(
    device_list=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    account_name='0000123456-00001'
)
```

