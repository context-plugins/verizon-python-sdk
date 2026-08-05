
# Dto Patch Device Request

## Structure

`DtoPatchDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `device` | [`ResourceDevice`](../../doc/models/resource-device.md) | Optional | - |
| `resourceidentifier` | [`DtoDeviceResourceIdentifier`](../../doc/models/dto-device-resource-identifier.md) | Optional | Device identifiers, one or more are required |

## Example

```python
import dateutil.parser
import jsonpickle

from verizon.models.dto_device_resource_identifier import DtoDeviceResourceIdentifier
from verizon.models.dto_patch_device_request import DtoPatchDeviceRequest
from verizon.models.resource_device import ResourceDevice

dto_patch_device_request = DtoPatchDeviceRequest(
    accountname='0000123456-00001',
    device=ResourceDevice(
        createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        foreignid='foreignid4',
        lastupdated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        state='state2',
        versionid='versionid8',
        accountclientid='accountclientid2',
        billingaccountid='billingaccountid2',
        chipset='chipset6',
        customdata={
            'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        },
        description='description6'
    ),
    resourceidentifier=DtoDeviceResourceIdentifier(
        deveui='deveui2',
        deviceid='deviceid6',
        esn=86,
        iccid='iccid0',
        imei=2
    )
)
```

