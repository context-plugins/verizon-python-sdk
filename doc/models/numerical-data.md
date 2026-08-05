
# Numerical Data

Describes value and unit of time.

## Structure

`NumericalData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `int` | Optional | Numerical value. |
| `unit` | [`NumericalDataUnitEnum`](../../doc/models/numerical-data-unit-enum.md) | Optional | Unit of time. |

## Example

```python
from verizon.models.numerical_data import NumericalData
from verizon.models.numerical_data_unit_enum import NumericalDataUnitEnum

numerical_data = NumericalData(
    value=5,
    unit=NumericalDataUnitEnum.SECOND
)
```

