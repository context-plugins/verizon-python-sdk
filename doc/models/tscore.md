
# Tscore

## Structure

`Tscore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profileid` | `str` | Optional | the UUID of the profile |
| `profileversionid` | `str` | Optional | the UUID of the profile version |

## Example

```python
from verizon.models.tscore import Tscore

tscore = Tscore(
    profileid='the UUID of the profile',
    profileversionid='the UUID of the profile version'
)
```

