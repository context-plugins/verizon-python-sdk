
# Text Phrase Item Content

An item object wrapping a text phrase value.

## Structure

`TextPhraseItemContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | Text phrase provides very short sections of text interspersed between the ITIS codes to create phrases. In general, this is used for expressing proper nouns, such as street names reflecting local expressions that do not appear in the ITIS tables.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16`, *Pattern*: ``^[\w\+\-!()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |

## Example

```python
from verizon.models.text_phrase_item_content import TextPhraseItemContent

text_phrase_item_content = TextPhraseItemContent(
    text='text2'
)
```

