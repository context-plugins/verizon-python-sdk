
# IP Pool

IP pool that is available to the account.

## Structure

`IPPool`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pool_name` | `str` | Optional | The name of the IP pool. |
| `pool_type` | `str` | Optional | The type of IP pool, such as “Static IP” or “Dynamic IP.” |
| `is_default_pool` | `bool` | Optional | True if this is the default IP pool for the account. |

## Example

```python
from verizon.models.ip_pool import IPPool

ip_pool = IPPool(
    pool_name='ACMESTATIC001',
    pool_type='Static IP',
    is_default_pool=True
)
```

