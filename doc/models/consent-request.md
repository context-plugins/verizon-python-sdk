
# Consent Request

## Structure

`ConsentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier in "##########-#####". |
| `all_device` | `bool` | Optional | Exclude all devices or not. |
| `mtype` | `str` | Optional | The change to make: append or replace. |
| `exclusion` | `List[str]` | Optional | Device ID list. |

## Example

```python
from verizon.models.consent_request import ConsentRequest

consent_request = ConsentRequest(
    account_name='1234567890-00001',
    all_device=False,
    mtype='replace',
    exclusion=[
        '980003420535573',
        '375535024300089',
        'A100003861E585'
    ]
)
```

