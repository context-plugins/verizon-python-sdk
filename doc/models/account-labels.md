
# Account Labels

Maximum of 2,000 objects are allowed in the array.

## Structure

`AccountLabels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | - |
| `label` | [`List[DeviceLabels]`](../../doc/models/device-labels.md) | Optional | - |

## Example

```python
from verizon.models.account_labels import AccountLabels
from verizon.models.device_id import DeviceId
from verizon.models.device_labels import DeviceLabels
from verizon.models.device_list import DeviceList

account_labels = AccountLabels(
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    label=[
        DeviceLabels(
            name='name0',
            value='value2'
        ),
        DeviceLabels(
            name='name0',
            value='value2'
        )
    ]
)
```

