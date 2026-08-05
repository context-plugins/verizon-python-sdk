
# Attribute Setting

Describes an attribute being observed and the frequency with which the attribute is being observed.

## Structure

`AttributeSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`AttributeIdentifierEnum`](../../doc/models/attribute-identifier-enum.md) | Optional | Attribute identifier. |
| `value` | `str` | Optional | Attribute value. |
| `created_on` | `datetime` | Optional | Date and time request was created. |
| `is_observable` | `bool` | Optional | Is the attribute observable? |
| `is_observing` | `bool` | Optional | Is the attribute being observed? |
| `frequency` | [`NumericalData`](../../doc/models/numerical-data.md) | Optional | Describes value and unit of time. |

## Example

```python
import dateutil.parser

from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.attribute_setting import AttributeSetting
from verizon.models.numerical_data import NumericalData
from verizon.models.numerical_data_unit_enum import NumericalDataUnitEnum

attribute_setting = AttributeSetting(
    name=AttributeIdentifierEnum.MANUFACTURER,
    value='string',
    created_on=dateutil.parser.parse('2019-09-07T23:08:03.532Z'),
    is_observable=True,
    is_observing=True,
    frequency=NumericalData(
        value=5,
        unit=NumericalDataUnitEnum.SECOND
    )
)
```

