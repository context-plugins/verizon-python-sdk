
# Exit Service Content

DataFrame content variant carrying exit service information.

## Structure

`ExitServiceContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exit_service` | List[[ITISItemWrapper](../../doc/models/itis-item-wrapper.md) \| [TextPhraseItemWrapper](../../doc/models/text-phrase-item-wrapper.md)] | Required | A data frame to allow sequences of ITIS codes, short text strings, and numerical values to be expressed in the normal ITIS vocabulary method and pattern. Note that the allowed text strings are more limited than the normal ITIS format in order to conserve bandwidth.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `16` |

## Example

```python
from verizon.models.exit_service_content import ExitServiceContent
from verizon.models.itis_item_content import ITISItemContent
from verizon.models.itis_item_wrapper import ITISItemWrapper

exit_service_content = ExitServiceContent(
    exit_service=[
        ITISItemWrapper(
            item=ITISItemContent(
                itis=10
            )
        ),
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

