
# Associate Label Request

## Structure

`AssociateLabelRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. An account name is usually numeric, and must include any leading zeros. |
| `labels` | [`AccountLabels`](../../doc/models/account-labels.md) | Required | Maximum of 2,000 objects are allowed in the array. |

## Example

```python
from verizon.models.account_labels import AccountLabels
from verizon.models.associate_label_request import AssociateLabelRequest
from verizon.models.device_id import DeviceId
from verizon.models.device_labels import DeviceLabels
from verizon.models.device_list import DeviceList

associate_label_request = AssociateLabelRequest(
    account_name='1223334444-00001',
    labels=AccountLabels(
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
            ),
            DeviceLabels(
                name='name0',
                value='value2'
            )
        ]
    )
)
```

