
# Asphalt or Tar

Indicates the surface of the roadway is asphalt or tar.

## Structure

`AsphaltOrTar`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type7Enum`](../../doc/models/type-7-enum.md) | Optional | Indicates the type of asphalt or tar. |

## Example

```python
from verizon.models.asphalt_or_tar import AsphaltOrTar
from verizon.models.type_7_enum import Type7Enum

asphalt_or_tar = AsphaltOrTar(
    mtype=Type7Enum.NEWSHARP
)
```

