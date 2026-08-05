
# Sensitivity Parameters

Details for sensitivity parameters.

## Structure

`SensitivityParameters`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `abnormal_max_value` | `float` | Optional | The maximum value of the threshold in the units being measured. |
| `enable_abnormal` | `bool` | Optional | If abnormal values are being monitored.<br />true - Monitor for abnormal values<br />false - Do not monitor for abnormal values. |
| `enable_very_abnormal` | `bool` | Optional | If very abnormal values are being monitored.<br />true - Monitor for very abnormal values<br />false - Do not monitor for very abnormal values. |
| `very_abnormal_max_value` | `float` | Optional | The maximum value of the threshold in the units being measured. |

## Example

```python
from verizon.models.sensitivity_parameters import SensitivityParameters

sensitivity_parameters = SensitivityParameters(
    abnormal_max_value=1.1,
    enable_abnormal=True,
    enable_very_abnormal=True,
    very_abnormal_max_value=0.55
)
```

