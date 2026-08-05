
# Observation Request

Used to define callbacks including the device identity, the attribute names, corresponding attribute values and the date/timestamp of when the observation was made.

## Structure

`ObservationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier in "##########-#####". |
| `devices` | [`List[Device]`](../../doc/models/device.md) | Required | List of devices. |
| `attributes` | [`List[ObservationRequestAttribute]`](../../doc/models/observation-request-attribute.md) | Required | Attributes are streaming RF parameters that you want to observe. |
| `frequency` | [`NumericalData`](../../doc/models/numerical-data.md) | Optional | Describes value and unit of time. |
| `duration` | [`NumericalData`](../../doc/models/numerical-data.md) | Optional | Describes value and unit of time. |

## Example

```python
from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.device import Device
from verizon.models.numerical_data import NumericalData
from verizon.models.observation_request import ObservationRequest
from verizon.models.observation_request_attribute import ObservationRequestAttribute

observation_request = ObservationRequest(
    account_name='0000123456-00001',
    devices=[
        Device(
            id='864508030026238',
            kind='IMEI'
        )
    ],
    attributes=[
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.RADIO_SIGNAL_STRENGTH
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.LINK_QUALITY
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.NETWORK_BEARER
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.CELL_ID
        )
    ],
    frequency=NumericalData(),
    duration=NumericalData()
)
```

