
# Labels List

## Structure

`LabelsList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | List[[DeviceLabels](../../doc/models/device-labels.md)] \| None | Optional | This is List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.device_labels import DeviceLabels
from verizon.models.labels_list import LabelsList

labels_list = LabelsList(
    device_ids=[
        DeviceLabels(
            name='name6',
            value='value8'
        )
    ]
)
```

