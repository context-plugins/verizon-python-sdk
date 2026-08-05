
# Carrier

## Structure

`Carrier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carriers` | `str` | Optional | The list of carriers with active or available profiles<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example

```python
from verizon.models.carrier import Carrier

carrier = Carrier(
    carriers='carriers6'
)
```

