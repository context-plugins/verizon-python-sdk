
# Device Software Upgrade

Array of software upgrade objects with the specified status.

## Structure

`DeviceSoftwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device identifier. |
| `id` | `str` | Required | Upgrade identifier. |
| `account_name` | `str` | Required | Account identifier. |
| `software_name` | `str` | Optional | Software name. |
| `start_date` | `date` | Required | Software upgrade start date. |
| `status` | `str` | Required | Software upgrade status. |
| `reason` | `str` | Required | Software upgrade result reason. |

## Example

```python
import dateutil.parser

from verizon.models.device_software_upgrade import DeviceSoftwareUpgrade

device_software_upgrade = DeviceSoftwareUpgrade(
    device_id='990013907835573',
    id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
    account_name='0402196254-00001',
    start_date=dateutil.parser.parse('2018-03-05').date(),
    status='UpgradeSuccess',
    reason='success',
    software_name='FOTA_Verizon_Model-A_02To03_HF'
)
```

