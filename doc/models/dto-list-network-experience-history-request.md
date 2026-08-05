
# Dto List Network Experience History Request

## Structure

`DtoListNetworkExperienceHistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `filter` | [`DtoFilter`](../../doc/models/dto-filter.md) | Optional | - |

## Example

```python
from verizon.models.dto_filter import DtoFilter
from verizon.models.dto_list_network_experience_history_request import DtoListNetworkExperienceHistoryRequest

dto_list_network_experience_history_request = DtoListNetworkExperienceHistoryRequest(
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

