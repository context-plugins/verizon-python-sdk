
# Software Package

Software package information.

## Structure

`SoftwarePackage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `software_name` | `str` | Required | Software name. |
| `launch_date` | `date` | Required | Software launch date. |
| `release_note` | `str` | Optional | Software release note reserved for future use. |
| `model` | `str` | Required | Software applicable device model. |
| `make` | `str` | Required | Software applicable device make. |
| `distribution_type` | `str` | Required | LWM2M, OMD-DM or HTTP. |
| `device_platform_id` | `str` | Required | The platform (Android, iOS, etc.) that the software can be applied to. |

## Example

```python
import dateutil.parser

from verizon.models.software_package import SoftwarePackage

software_package = SoftwarePackage(
    software_name='FOTA_Verizon_Model-A_02To03_HF',
    launch_date=dateutil.parser.parse('2020-08-31').date(),
    model='Model-A',
    make='Verizon',
    distribution_type='HTTP',
    device_platform_id='IoT',
    release_note=''
)
```

