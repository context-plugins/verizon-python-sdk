
# Dto List User Request

## Structure

`DtoListUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `filter` | [`DtoFilter`](../../doc/models/dto-filter.md) | Optional | - |

## Example

```python
from verizon.models.dto_filter import DtoFilter
from verizon.models.dto_list_user_request import DtoListUserRequest

dto_list_user_request = DtoListUserRequest(
    accountname='0000123456-00001',
    filter=DtoFilter(
        expand='$expand0',
        limitnumber=100,
        nopagination=False,
        page='$page0',
        pagenumber=64
    )
)
```

