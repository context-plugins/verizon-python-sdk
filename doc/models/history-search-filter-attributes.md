
# History Search Filter Attributes

Streaming RF parameters for which you want to retrieve history data.

## Structure

`HistorySearchFilterAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`AttributeIdentifierEnum`](../../doc/models/attribute-identifier-enum.md) | Optional | Attribute identifier. |

## Example

```python
from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.history_search_filter_attributes import HistorySearchFilterAttributes

history_search_filter_attributes = HistorySearchFilterAttributes(
    name=AttributeIdentifierEnum.LINK_QUALITY
)
```

