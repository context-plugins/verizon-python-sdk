
# Active Anomaly Indicator

Whether the anomaly detection is active or not.

## Structure

`ActiveAnomalyIndicator`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | Indicates anomaly detection is active<br />True - Anomaly detection is active.<br />False - Anomaly detection is not active. |

## Example

```python
from verizon.models.active_anomaly_indicator import ActiveAnomalyIndicator

active_anomaly_indicator = ActiveAnomalyIndicator(
    active=True
)
```

