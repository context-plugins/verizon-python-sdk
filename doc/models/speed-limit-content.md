
# Speed Limit Content

DataFrame content variant carrying speed limit information.

## Structure

`SpeedLimitContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `speed_limit` | List[[ITISItemWrapper](../../doc/models/itis-item-wrapper.md) \| [TextPhraseItemWrapper](../../doc/models/text-phrase-item-wrapper.md)] | Required | A data frame to allow sequences of ITIS codes, short text strings, and numerical values to be expressed in the normal ITIS vocabulary method and pattern. Note that the allowed text strings are more limited than the normal ITIS format in order to conserve bandwidth.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `16` |

## Example

```python
from verizon.models.itis_item_content import ITISItemContent
from verizon.models.itis_item_wrapper import ITISItemWrapper
from verizon.models.speed_limit_content import SpeedLimitContent

speed_limit_content = SpeedLimitContent(
    speed_limit=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        ),
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        )
    ]
)
```

