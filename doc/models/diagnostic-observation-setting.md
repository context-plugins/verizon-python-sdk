
# Diagnostic Observation Setting

Diagnostic observation settings and attributes for a device.

## Structure

`DiagnosticObservationSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of the billing account for which callback messages will be sent. Format: "##########-#####". |
| `device` | [`Device`](../../doc/models/device.md) | Optional | Identifies a particular IoT device. |
| `attributes` | [`List[AttributeSetting]`](../../doc/models/attribute-setting.md) | Optional | Streaming RF parameters for which you want to retrieve diagnostic settings. |

## Example

```python
import dateutil.parser

from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.attribute_setting import AttributeSetting
from verizon.models.device import Device
from verizon.models.diagnostic_observation_setting import DiagnosticObservationSetting
from verizon.models.numerical_data import NumericalData
from verizon.models.numerical_data_unit_enum import NumericalDataUnitEnum

diagnostic_observation_setting = DiagnosticObservationSetting(
    account_name='string',
    device=Device(
        id='864508030026238',
        kind='IMEI'
    ),
    attributes=[
        AttributeSetting(
            name=AttributeIdentifierEnum.MANUFACTURER,
            value='string',
            created_on=dateutil.parser.parse('2019-09-07T23:08:03.532Z'),
            is_observable=True,
            is_observing=True,
            frequency=NumericalData(
                value=5,
                unit=NumericalDataUnitEnum.SECOND
            )
        )
    ]
)
```

