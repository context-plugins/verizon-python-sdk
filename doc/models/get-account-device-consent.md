
# Get Account Device Consent

## Structure

`GetAccountDeviceConsent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[Any]` | Optional | An array of device identifiers |
| `account_name` | `str` | Optional | The numeric name of the account, including leading zeros. |
| `all_device_consent` | `int` | Optional | If consent is set at the account level, this value will show the consent level. |

## Example

```python
import jsonpickle

from verizon.models.get_account_device_consent import GetAccountDeviceConsent

get_account_device_consent = GetAccountDeviceConsent(
    device_list=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    account_name='0000123456-00001',
    all_device_consent=1
)
```

