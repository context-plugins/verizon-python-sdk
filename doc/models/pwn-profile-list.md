
# PWN Profile List

## Structure

`PWNProfileList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profiles` | [`List[PWNProfile]`](../../doc/models/pwn-profile.md) | Optional | - |

## Example

```python
from verizon.models.pwn_profile import PWNProfile
from verizon.models.pwn_profile_list import PWNProfileList

pwn_profile_list = PWNProfileList(
    profiles=[
        PWNProfile(
            profile_id='HSS-EsmProfile_Enterprise',
            profile_name='HSS EsmProfile Enterprise'
        )
    ]
)
```

