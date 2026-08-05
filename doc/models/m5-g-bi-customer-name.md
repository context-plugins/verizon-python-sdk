
# M5 G Bi Customer Name

## Structure

`M5gBiCustomerName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `middle_name` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `suffex` | `str` | Optional | - |

## Example

```python
from verizon.models.m_5g_bi_customer_name import M5gBiCustomerName

m_5g_bi_customer_name = M5gBiCustomerName(
    first_name='First name',
    last_name='Surname or Last Name',
    middle_name='middle name or initial',
    title='Mr. or Ms.',
    suffex='Dr or Esq'
)
```

