
# Firmware Upgrade Request

Details of the firmware upgrade request.

## Structure

`FirmwareUpgradeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier in "##########-#####". |
| `firmware_name` | `str` | Required | The name of the firmware image that will be used for the upgrade, from a GET /firmware response. |
| `firmware_to` | `str` | Required | The name of the firmware version that will be on the devices after a successful upgrade. |
| `start_date` | `date` | Required | The date that the upgrade begins. |
| `end_date` | `date` | Required | The date that the upgrade ends. |
| `device_list` | `List[str]` | Required | The IMEIs of the devices. |

## Example

```python
import dateutil.parser

from verizon.models.firmware_upgrade_request import FirmwareUpgradeRequest

firmware_upgrade_request = FirmwareUpgradeRequest(
    account_name='0402196254-00001',
    firmware_name='FOTA_Verizon_Model-A_01To02_HF',
    firmware_to='VerizonFirmwareVersion-02',
    start_date=dateutil.parser.parse('2018-04-01').date(),
    end_date=dateutil.parser.parse('2018-04-05').date(),
    device_list=[
        '990003425730535',
        '990000473475989',
        '990005733420535',
        '990000347475989',
        '990007303425535',
        '990007590473489'
    ]
)
```

