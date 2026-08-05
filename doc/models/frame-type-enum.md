
# Frame Type Enum

The frameType data element provides the type of message to follow in the rest of the message frame structure. The following frame types are supported:

- unknown
- advisory
- roadSignage
- commercialSignage

## Enumeration

`FrameTypeEnum`

## Fields

| Name |
|  --- |
| `UNKNOWN` |
| `ADVISORY` |
| `ROADSIGNAGE` |
| `COMMERCIALSIGNAGE` |

## Example

```python
from verizon.models.frame_type_enum import FrameTypeEnum

frame_type = FrameTypeEnum.ROADSIGNAGE
```

