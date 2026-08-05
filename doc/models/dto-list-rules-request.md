
# Dto List Rules Request

## Structure

`DtoListRulesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `filter` | [`DtoFilter`](../../doc/models/dto-filter.md) | Optional | - |
| `resourceidentifier` | [`DtoResourceidentifier`](../../doc/models/dto-resourceidentifier.md) | Optional | - |

## Example

```python
from verizon.models.dto_filter import DtoFilter
from verizon.models.dto_list_rules_request import DtoListRulesRequest
from verizon.models.dto_resourceidentifier import DtoResourceidentifier

dto_list_rules_request = DtoListRulesRequest(
    accountname='0000123456-00001',
    filter=DtoFilter(
        expand='$expand0',
        limitnumber=100,
        nopagination=False,
        page='$page0',
        pagenumber=64
    ),
    resourceidentifier=DtoResourceidentifier(
        id='id4'
    )
)
```

