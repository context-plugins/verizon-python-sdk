
# Distribution Schedule

The distribution schedule parameters for broadcast messages.

## Structure

`DistributionSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `repeat_period` | `int` | Required | The period (in seconds) that the message needs to be repeatedly send out.<br><br>**Constraints**: `>= 5`, `<= 3600` |
| `duration` | `int` | Required | The amount of time (in minutes) while the messages needs to be sent out.<br><br>**Constraints**: `>= 1`, `<= 32000` |
| `start_time` | `datetime` | Optional | The time (in UTC) when the message transmission should be started. |

## Example

```python
import dateutil.parser

from verizon.models.distribution_schedule import DistributionSchedule

distribution_schedule = DistributionSchedule(
    repeat_period=66,
    duration=64,
    start_time=dateutil.parser.parse('2042-07-21T17:32:28Z')
)
```

