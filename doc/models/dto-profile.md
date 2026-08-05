
# Dto Profile

## Structure

`DtoProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Optional | profile kind |
| `version` | `str` | Optional | The resource version |
| `modelid` | `str` | Optional | device model id |
| `name` | `str` | Optional | profile name |
| `configuration` | `Any` | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.dto_profile import DtoProfile

dto_profile = DtoProfile(
    kind='the kind of profile being created',
    version='1.0',
    modelid='00000000-0000-0000-0000-000000000019',
    name='Demo Entry sensor 1730928792',
    configuration=jsonpickle.decode('{"randomInt":21,"resportingInterval":24}')
)
```

