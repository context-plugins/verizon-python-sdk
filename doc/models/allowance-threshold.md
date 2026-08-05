
# Allowance Threshold

## Structure

`AllowanceThreshold`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `percentage_50` | `bool` | Optional | - |
| `percentage_75` | `bool` | Optional | - |
| `percentage_90` | `bool` | Optional | - |
| `percentage_100` | `bool` | Optional | - |

## Example

```python
from verizon.models.allowance_threshold import AllowanceThreshold

allowance_threshold = AllowanceThreshold(
    percentage_50=True,
    percentage_75=False,
    percentage_90=True,
    percentage_100=False
)
```

