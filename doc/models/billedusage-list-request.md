
# Billedusage List Request

Information required to associate a usage segmentation label with a device to retrieve billing.

## Structure

`BilledusageListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `labels` | [`LabelsList`](../../doc/models/labels-list.md) | Optional | - |
| `device_ids` | [`List[DeviceList]`](../../doc/models/device-list.md) | Optional | - |
| `billing_cycle` | [`BillingCycle`](../../doc/models/billing-cycle.md) | Optional | - |

## Example

```python
from verizon.models.billedusage_list_request import BilledusageListRequest
from verizon.models.billing_cycle import BillingCycle
from verizon.models.device_id import DeviceId
from verizon.models.device_labels import DeviceLabels
from verizon.models.device_list import DeviceList
from verizon.models.labels_list import LabelsList

billedusage_list_request = BilledusageListRequest(
    account_name='9231221278-99990',
    labels=LabelsList(
        device_ids=[
            DeviceLabels(
                name='name6',
                value='value8'
            )
        ]
    ),
    device_ids=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                ),
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        ),
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                ),
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    billing_cycle=BillingCycle(
        year='year6',
        month='month4'
    )
)
```

