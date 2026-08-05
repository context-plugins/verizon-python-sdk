
# M5 G Bi Address

## Structure

`M5gBiAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `zip` | `str` | Optional | - |
| `zip_4` | `str` | Optional | - |
| `phone` | `str` | Optional | - |
| `phone_type` | `str` | Optional | - |
| `email_address` | `str` | Optional | - |

## Example

```python
from verizon.models.m_5g_bi_address import M5gBiAddress

m_5g_bi_address = M5gBiAddress(
    address_line_1='number and street',
    city='city',
    state='2-letter state ID (conforms to ISO 3166-2)',
    zip='5-digit zip code',
    zip_4='the +4 digits used for zip codes',
    phone='a 10-digit phone number',
    phone_type='W',
    email_address='email@emailaddress.com'
)
```

