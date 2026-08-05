
# Awareness Distance Enum

Specifies how far the event is relevant to.

## Enumeration

`AwarenessDistanceEnum`

## Fields

| Name |
|  --- |
| `LESSTHAN50M` |
| `LESSTHAN100M` |
| `LESSTHAN200M` |
| `LESSTHAN500M` |
| `LESSTHAN1000M` |
| `LESSTHAN5KM` |
| `LESSTHAN10KM` |
| `OVER10KM` |

## Example

```python
from verizon.models.awareness_distance_enum import AwarenessDistanceEnum

awareness_distance = AwarenessDistanceEnum.LESSTHAN50M
```

