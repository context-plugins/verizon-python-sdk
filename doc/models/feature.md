
# Feature

## Structure

`Feature`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `features` | `str` | Optional | The calling and data features available for the account. **Note:** for Global IoT Orchestrator, the features `eUICC Verizon as Lead` and `Global eSim Billing` will always be present.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example

```python
from verizon.models.feature import Feature

feature = Feature(
    features='features8'
)
```

