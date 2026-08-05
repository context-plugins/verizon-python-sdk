
# Anomaly Detection Trigger

Trigger for anomaly detection.

## Structure

`AnomalyDetectionTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | Trigger ID to identify the request in a callback. |

## Example

```python
from verizon.models.anomaly_detection_trigger import AnomalyDetectionTrigger

anomaly_detection_trigger = AnomalyDetectionTrigger(
    trigger_id='595f5c44-c31c-4552-8670-020a1545a84d'
)
```

