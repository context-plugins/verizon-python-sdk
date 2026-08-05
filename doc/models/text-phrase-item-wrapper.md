
# Text Phrase Item Wrapper

A wrapper carrying a text phrase item.

## Structure

`TextPhraseItemWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`TextPhraseItemContent`](../../doc/models/text-phrase-item-content.md) | Required | An item object wrapping a text phrase value. |

## Example

```python
from verizon.models.text_phrase_item_content import TextPhraseItemContent
from verizon.models.text_phrase_item_wrapper import TextPhraseItemWrapper

text_phrase_item_wrapper = TextPhraseItemWrapper(
    item=TextPhraseItemContent(
        text='text2'
    )
)
```

