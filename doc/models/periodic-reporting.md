
# Periodic Reporting

The units and values of the time interval for the sensor to send a report

## Structure

`PeriodicReporting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | [`UnitEnum`](../../doc/models/unit-enum.md) | Optional | - |
| `hours` | `int` | Optional | whole numbers from 0 to 24 |
| `minutes` | `int` | Optional | whole numbers from 0 to 59 |

## Example

```python
from verizon.models.periodic_reporting import PeriodicReporting
from verizon.models.unit_enum import UnitEnum

periodic_reporting = PeriodicReporting(
    unit=UnitEnum.MINUTES,
    hours=0,
    minutes=12
)
```

