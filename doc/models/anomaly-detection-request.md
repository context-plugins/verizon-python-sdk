
# Anomaly Detection Request

Anomaly detection request.

## Structure

`AnomalyDetectionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of a billing account. An account name is usually numeric, and must include any leading zeros.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `request_type` | `str` | Optional | The type of request being made. anomaly is the request to activate anomaly detection. |
| `sensitivity_parameter` | [`SensitivityParameters`](../../doc/models/sensitivity-parameters.md) | Optional | Details for sensitivity parameters. |

## Example

```python
from verizon.models.anomaly_detection_request import AnomalyDetectionRequest
from verizon.models.sensitivity_parameters import SensitivityParameters

anomaly_detection_request = AnomalyDetectionRequest(
    account_name='0000123456-00001',
    request_type='anomaly',
    sensitivity_parameter=SensitivityParameters(
        abnormal_max_value=1.1,
        enable_abnormal=True,
        enable_very_abnormal=True,
        very_abnormal_max_value=0.55
    )
)
```

