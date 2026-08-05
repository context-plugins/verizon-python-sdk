
# Generic Payload

Custom message which is defined by the user and can support "any" message type or format.

**Note:** ETX prefers the j2735 or the j2735_gr encoding and only vendor specific message types are allowed to be published in different message formats.

## Structure

`GenericPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_type` | `str` | Required | The type of message. This can be any of the standard V2X messages specified in the SAE J2735 standard (e.g. BSM, PSM, RSA, TIM, MAP, SPAT, etc.), or it can be a vendor specific message type that is not defined by the standard.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: ``^[a-zA-Z0-9~\+\-!@#$%^&*()\`\[\]{=};"':,.\/<>?\|\s]+$`` |
| `message_format` | `str` | Required | The encoding of the message (e.g. j2735, protobuf, json, Avro, etc.). If the message is encapsulated within a GeoRoutedMsg protocol buffer wrapper, append _gr to the message format (e.g. j2735 => j2735_gr).<br><br>**Note:** ETX prefers the j2735 or the j2735_gr encoding and only vendor specific message types are allowed to be published in different message formats.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: ``^[a-zA-Z0-9~\+\-!@#$%^&*()\`\[\]{=};"':,.\/<>?\|\s]+$`` |
| `payload` | `str` | Required | The base64 encoded message.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `8192`, *Pattern*: `^(?:[a-zA-Z0-9+\/]{4})*(?:\|(?:[a-zA-Z0-9+\/]{3}=)\|(?:[a-zA-Z0-9+\/]{2}==)\|(?:[a-zA-Z0-9+\/]{1}===))$` |

## Example

```python
from verizon.models.generic_payload import GenericPayload

generic_payload = GenericPayload(
    message_type='messageType2',
    message_format='messageFormat4',
    payload='payload8'
)
```

