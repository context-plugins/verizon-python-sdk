
# Status List

## Structure

`StatusList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Account name |
| `status` | `str` | Optional | Success or Fail |
| `reason` | `str` | Optional | detailed reason |

## Example

```python
from verizon.models.status_list import StatusList

status_list = StatusList(
    id='1223334444-00001',
    status='Success',
    reason='Success'
)
```

