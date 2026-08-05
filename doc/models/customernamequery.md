
# Customernamequery

## Structure

`Customernamequery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | [`List[CustomerName]`](../../doc/models/customer-name.md) | Optional | **Constraints**: *Maximum Items*: `5` |

## Example

```python
from verizon.models.customer_name import CustomerName
from verizon.models.customernamequery import Customernamequery

customernamequery = Customernamequery(
    customer_name=[
        CustomerName(
            first_name='firstName4',
            last_name='lastName4',
            title='title4',
            middle_name='middleName8',
            suffix='suffix0'
        ),
        CustomerName(
            first_name='firstName4',
            last_name='lastName4',
            title='title4',
            middle_name='middleName8',
            suffix='suffix0'
        )
    ]
)
```

