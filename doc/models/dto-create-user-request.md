
# Dto Create User Request

## Structure

`DtoCreateUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `user` | [`DtoUserDTO`](../../doc/models/dto-user-dto.md) | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.dto_create_user_request import DtoCreateUserRequest
from verizon.models.dto_user_dto import DtoUserDTO

dto_create_user_request = DtoCreateUserRequest(
    accountname='0000123456-00001',
    user=DtoUserDTO(
        email='email6',
        firstname='firstname8',
        lastname='lastname6',
        mdn='mdn8',
        customdata={
            'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'key1': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'key2': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    )
)
```

