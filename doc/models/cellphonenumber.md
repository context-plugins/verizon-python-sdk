
# Cellphonenumber

## Structure

`Cellphonenumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Optional | - |
| `carrier` | `str` | Optional | - |

## Example

```python
from verizon.models.cellphonenumber import Cellphonenumber

cellphonenumber = Cellphonenumber(
    number='10-digit mobile number',
    carrier='mobile service provider'
)
```

