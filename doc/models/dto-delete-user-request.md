
# Dto Delete User Request

## Structure

`DtoDeleteUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |

## Example

```python
from verizon.models.dto_delete_user_request import DtoDeleteUserRequest

dto_delete_user_request = DtoDeleteUserRequest(
    accountname='0000123456-00001',
    id='id0'
)
```

