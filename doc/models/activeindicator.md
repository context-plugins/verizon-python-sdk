
# Activeindicator

## Structure

`Activeindicator`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | [`ActiveEnum`](../../doc/models/active-enum.md) | Optional | A flag to indicate of the trigger is active, true, or not, false |

## Example

```python
from verizon.models.active_enum import ActiveEnum
from verizon.models.activeindicator import Activeindicator

activeindicator = Activeindicator(
    active=ActiveEnum.TRUE
)
```

