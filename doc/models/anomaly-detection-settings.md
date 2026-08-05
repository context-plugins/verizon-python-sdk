
# Anomaly Detection Settings

Settings for anomaly detection.

## Structure

`AnomalyDetectionSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Indicates if the account name used has anomaly detection.<br />Success - The account has anomaly detection.<br />Failure - The account does not have anomaly detection. |
| `sensitivity_parameter` | [`SensitivityParameters`](../../doc/models/sensitivity-parameters.md) | Optional | Details for sensitivity parameters. |
| `status` | `str` | Optional | Indicates if anomaly detection is active on the account<br />Active - Anomaly detection is active<br />Disabled- Anomaly detection is not active. |

## Example

```python
from verizon.models.anomaly_detection_settings import AnomalyDetectionSettings
from verizon.models.sensitivity_parameters import SensitivityParameters

anomaly_detection_settings = AnomalyDetectionSettings(
    account_name='Success',
    sensitivity_parameter=SensitivityParameters(
        abnormal_max_value=1.1,
        enable_abnormal=True,
        enable_very_abnormal=True,
        very_abnormal_max_value=0.55
    ),
    status='Active'
)
```

