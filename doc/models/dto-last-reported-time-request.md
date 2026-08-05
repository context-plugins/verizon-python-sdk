
# Dto Last Reported Time Request

## Structure

`DtoLastReportedTimeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `resourceidentifier` | [`DtoDeviceResourceIdentifier`](../../doc/models/dto-device-resource-identifier.md) | Optional | Device identifiers, one or more are required |

## Example

```python
from verizon.models.dto_device_resource_identifier import DtoDeviceResourceIdentifier
from verizon.models.dto_last_reported_time_request import DtoLastReportedTimeRequest

dto_last_reported_time_request = DtoLastReportedTimeRequest(
    accountname='0000123456-00001',
    resourceidentifier=DtoDeviceResourceIdentifier(
        deveui='deveui2',
        deviceid='deviceid6',
        esn=86,
        iccid='iccid0',
        imei=2
    )
)
```

