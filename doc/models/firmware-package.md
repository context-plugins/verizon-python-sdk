
# Firmware Package

Available firmware.

## Structure

`FirmwarePackage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `firmware_name` | `str` | Required | Firmware name. |
| `firmware_from` | `str` | Required | Firmware from version. |
| `firmware_to` | `str` | Required | Firmware to version. |
| `launch_date` | `datetime` | Required | Firmware launch date. |
| `release_note` | `str` | Required | Firmware release note. |
| `model` | `str` | Required | Firmware applicable device model. |
| `make` | `str` | Required | Firmware applicable device make. |
| `protocol` | [`CampaignMetaInfoProtocolEnum`](../../doc/models/campaign-meta-info-protocol-enum.md) | Required | Firmware protocol. Valid values include: LWM2M, OMD-DM.<br><br>**Default**: `"LWM2M"` |

## Example

```python
import dateutil.parser

from verizon.models.campaign_meta_info_protocol_enum import CampaignMetaInfoProtocolEnum
from verizon.models.firmware_package import FirmwarePackage

firmware_package = FirmwarePackage(
    firmware_name='VerizonSmartCommunities_LCO-277C4N_BG96MAR04A04M1G_BG96MAR04A04M1G_BETA0130B',
    firmware_from='BG96MAR04A04M1G',
    firmware_to='BG96MAR04A04M1G_BETA0130B',
    launch_date=dateutil.parser.parse('2012-04-23T18:25:43.511Z'),
    release_note='',
    model='LCO-277C4N',
    make='Verizon Smart Communities',
    protocol=CampaignMetaInfoProtocolEnum.LW_M2M
)
```

