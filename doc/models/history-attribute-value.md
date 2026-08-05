
# History Attribute Value

Streaming RF parameter for which you want to retrieve history data.

## Structure

`HistoryAttributeValue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`AttributeIdentifierEnum`](../../doc/models/attribute-identifier-enum.md) | Optional | Attribute identifier. |
| `value` | `str` | Optional | Attribute value. |
| `created_on` | `datetime` | Optional | Date and time the request was created. |

## Example

```python
import dateutil.parser

from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.history_attribute_value import HistoryAttributeValue

history_attribute_value = HistoryAttributeValue(
    name=AttributeIdentifierEnum.LINK_QUALITY,
    value='47',
    created_on=dateutil.parser.parse('2022-02-10T16:02:21.406Z')
)
```

