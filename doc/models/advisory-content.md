
# Advisory Content

DataFrame content variant carrying advisory ITIS codes.

## Structure

`AdvisoryContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `advisory` | List[[ITISItemWrapper](../../doc/models/itis-item-wrapper.md) \| [TextItemWrapper](../../doc/models/text-item-wrapper.md)] | Required | The use of ITIS codes interspersed with free text. The complete set of ITIS codes can be found in Volume Two of the SAE J2540 standard.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `100` |

## Example

```python
from verizon.models.advisory_content import AdvisoryContent
from verizon.models.itis_item_content import ITISItemContent
from verizon.models.itis_item_wrapper import ITISItemWrapper

advisory_content = AdvisoryContent(
    advisory=[
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

