
# Dto Filter

## Structure

`DtoFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expand` | `str` | Optional | Use to provide device details for alerts specific to a device |
| `limitnumber` | `int` | Optional | Limit the number of results returned<br><br>**Constraints**: `>= 0`, `<= 100` |
| `nopagination` | `bool` | Optional | A flag set to show if pagination requested (false) or not (true) |
| `page` | `str` | Optional | - |
| `pagenumber` | `int` | Optional | **Constraints**: `>= 0`, `<= 100` |
| `projection` | `List[str]` | Optional | Limits the fields of the device that the user is interested in rather than all of the fields<br><br>**Constraints**: *Maximum Items*: `100` |
| `selection` | `Dict[str, Any]` | Optional | Filters results based on user defined criteria |

## Example

```python
from verizon.models.dto_filter import DtoFilter

dto_filter = DtoFilter(
    expand='device detail(s)',
    limitnumber=100,
    nopagination=True,
    page='The number of pages',
    pagenumber=100
)
```

