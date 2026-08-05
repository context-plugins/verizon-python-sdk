
# Text Item Content

An item object wrapping a text value.

## Structure

`TextItemContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | Simple text used with ITIS codes. (Text taken from SAE J2540.)<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `500`, *Pattern*: ``^[\w\+\-!()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |

## Example

```python
from verizon.models.text_item_content import TextItemContent

text_item_content = TextItemContent(
    text='text2'
)
```

