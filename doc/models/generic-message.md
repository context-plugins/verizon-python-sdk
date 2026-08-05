
# Generic Message

A message carrying a generic (custom) V2X payload.

## Structure

`GenericMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `generic` | [`GenericPayload`](../../doc/models/generic-payload.md) | Required | Custom message which is defined by the user and can support "any" message type or format.<br><br>**Note:** ETX prefers the j2735 or the j2735_gr encoding and only vendor specific message types are allowed to be published in different message formats. |

## Example

```python
from verizon.models.generic_message import GenericMessage
from verizon.models.generic_payload import GenericPayload

generic_message = GenericMessage(
    generic=GenericPayload(
        message_type='messageType4',
        message_format='messageFormat6',
        payload='payload0'
    )
)
```

