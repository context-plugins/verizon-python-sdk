
# Header

The header of the DENM PDU.

## Structure

`Header`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protocol_version` | [`ProtocolVersionEnum`](../../doc/models/protocol-version-enum.md) | Required | The protocol version of the DENM. |
| `message_id` | [`MessageIdEnum`](../../doc/models/message-id-enum.md) | Required | The type of ITIS message (typically 1 for DENM). |
| `station_id` | `int` | Required | The station identifier of the ITS-S. |

## Example

```python
from verizon.models.header import Header
from verizon.models.message_id_enum import MessageIdEnum
from verizon.models.protocol_version_enum import ProtocolVersionEnum

header = Header(
    protocol_version=ProtocolVersionEnum.ENUM_2,
    message_id=MessageIdEnum.ENUM_1,
    station_id=12345
)
```

