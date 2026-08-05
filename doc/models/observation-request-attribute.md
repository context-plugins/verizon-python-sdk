
# Observation Request Attribute

Streaming RF parameter that you want to observe.

## Structure

`ObservationRequestAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`AttributeIdentifierEnum`](../../doc/models/attribute-identifier-enum.md) | Optional | Attribute identifier. |

## Example

```python
from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.observation_request_attribute import ObservationRequestAttribute

observation_request_attribute = ObservationRequestAttribute(
    name=AttributeIdentifierEnum.RADIO_SIGNAL_STRENGTH
)
```

