
# V2 Software Info

Software information.

## Structure

`V2SoftwareInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Software name. |
| `version` | `str` | Required | Software version. |
| `upgrade_time` | `str` | Required | Upgrade time. |

## Example

```python
from verizon.models.v2_software_info import V2SoftwareInfo

v2_software_info = V2SoftwareInfo(
    name='FOTA_Verizon_Model-A_02To03_HF',
    version='3',
    upgrade_time='2020-09-08T19:00:51.541Z'
)
```

