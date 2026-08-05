
# Firmware IMEI

A list of IMEIs for devices to be synchronized between ThingSpace and the FOTA server.

## Structure

`FirmwareIMEI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[str]` | Required | Device IMEI list.<br><br>**Constraints**: *Maximum Items*: `1000` |

## Example

```python
from verizon.models.firmware_imei import FirmwareIMEI

firmware_imei = FirmwareIMEI(
    device_list=[
        '15-digit IMEI'
    ]
)
```

