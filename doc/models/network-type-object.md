
# Network Type Object

Network type.

## Structure

`NetworkTypeObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_type` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.network_type_object import NetworkTypeObject

network_type_object = NetworkTypeObject(
    network_type='LTE'
)
```

