
# Dto Configuration Profile

## Structure

`DtoConfigurationProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `profiles` | [`List[DtoProfile]`](../../doc/models/dto-profile.md) | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.dto_configuration_profile import DtoConfigurationProfile
from verizon.models.dto_profile import DtoProfile

dto_configuration_profile = DtoConfigurationProfile(
    accountname='0000123456-00001',
    profiles=[
        DtoProfile(
            kind='kind6',
            version='version4',
            modelid='modelid2',
            name='name8',
            configuration=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ),
        DtoProfile(
            kind='kind6',
            version='version4',
            modelid='modelid2',
            name='name8',
            configuration=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        )
    ]
)
```

