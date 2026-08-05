
# Text Item Wrapper

A wrapper carrying a text item.

## Structure

`TextItemWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`TextItemContent`](../../doc/models/text-item-content.md) | Required | An item object wrapping a text value. |

## Example

```python
from verizon.models.text_item_content import TextItemContent
from verizon.models.text_item_wrapper import TextItemWrapper

text_item_wrapper = TextItemWrapper(
    item=TextItemContent(
        text='text2'
    )
)
```

