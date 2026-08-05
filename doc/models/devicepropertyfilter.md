
# Devicepropertyfilter

## Structure

`Devicepropertyfilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `selection` | [`Devicepropertyselection`](../../doc/models/devicepropertyselection.md) | Optional | - |
| `querytotalcount` | `bool` | Optional | - |

## Example

```python
from verizon.models.devicepropertyfilter import Devicepropertyfilter
from verizon.models.devicepropertyselection import Devicepropertyselection

devicepropertyfilter = Devicepropertyfilter(
    selection=Devicepropertyselection(
        modelid='modelid0'
    ),
    querytotalcount=True
)
```

