
# PWN Profile

## Structure

`PWNProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_id` | `str` | Optional | - |
| `profile_name` | `str` | Optional | - |

## Example

```python
from verizon.models.pwn_profile import PWNProfile

pwn_profile = PWNProfile(
    profile_id='HSS-EsmProfile_Enterprise',
    profile_name='HSS EsmProfile Enterprise'
)
```

