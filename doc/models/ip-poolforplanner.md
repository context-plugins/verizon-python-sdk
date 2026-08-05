
# IP Poolforplanner

## Structure

`IPPoolforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_default_pool` | `bool` | Optional | - |
| `pool_name` | `str` | Optional | - |
| `pool_type` | `str` | Optional | - |

## Example

```python
from verizon.models.ip_poolforplanner import IPPoolforplanner

ip_poolforplanner = IPPoolforplanner(
    is_default_pool=False,
    pool_name='poolName2',
    pool_type='poolType6'
)
```

