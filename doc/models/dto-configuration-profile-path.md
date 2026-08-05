
# Dto Configuration Profile Path

## Structure

`DtoConfigurationProfilePath`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric account name, which must include leading zeros |
| `resourceidentifier` | [`DtoResourceidentifier`](../../doc/models/dto-resourceidentifier.md) | Optional | - |
| `profile` | [`DtoProfile`](../../doc/models/dto-profile.md) | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.dto_configuration_profile_path import DtoConfigurationProfilePath
from verizon.models.dto_profile import DtoProfile
from verizon.models.dto_resourceidentifier import DtoResourceidentifier

dto_configuration_profile_path = DtoConfigurationProfilePath(
    account_name='0000123456-00001',
    resourceidentifier=DtoResourceidentifier(
        id='id4'
    ),
    profile=DtoProfile(
        kind='kind8',
        version='version6',
        modelid='modelid4',
        name='name0',
        configuration=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    )
)
```

