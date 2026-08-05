
# ITIS Item Wrapper

A wrapper carrying an ITIS code item.

## Structure

`ITISItemWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`ITISItemContent`](../../doc/models/itis-item-content.md) | Required | An item object wrapping an ITIS code value. |

## Example

```python
from verizon.models.itis_item_content import ITISItemContent
from verizon.models.itis_item_wrapper import ITISItemWrapper

itis_item_wrapper = ITISItemWrapper(
    item=ITISItemContent(
        itis=10
    )
)
```

