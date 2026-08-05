
# History Search Limit Time

The time period for which a request should retrieve data, beginning with the limitTime.startOn and proceeding with the limitTime.duration.

## Structure

`HistorySearchLimitTime`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_on` | `datetime` | Optional | The starting date-time for this request. |
| `duration` | [`NumericalData`](../../doc/models/numerical-data.md) | Optional | Describes value and unit of time. |

## Example

```python
import dateutil.parser

from verizon.models.history_search_limit_time import HistorySearchLimitTime
from verizon.models.numerical_data import NumericalData
from verizon.models.numerical_data_unit_enum import NumericalDataUnitEnum

history_search_limit_time = HistorySearchLimitTime(
    start_on=dateutil.parser.parse('2019-08-29T00:47:59.240Z'),
    duration=NumericalData(
        value=5,
        unit=NumericalDataUnitEnum.SECOND
    )
)
```

