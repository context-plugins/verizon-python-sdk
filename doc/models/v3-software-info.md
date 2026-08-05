
# V3 Software Info

Software information.

## Structure

`V3SoftwareInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Software name. |
| `version` | `str` | Required | Software version. |
| `upgrade_time` | `str` | Required | Upgrade time. |

## Example

```python
from verizon.models.v3_software_info import V3SoftwareInfo

v3_software_info = V3SoftwareInfo(
    name='VZ_MDM_IOT',
    version='0.14',
    upgrade_time='2012-04-23T18:25:43.511Z'
)
```

