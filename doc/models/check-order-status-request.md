
# Check Order Status Request

The request body identifies the devices to upload.

## Structure

`CheckOrderStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. An account name is usually numeric, and must include any leading zeros. |
| `order_request_id` | `str` | Optional | The request id from the activation order. |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | The devices to upload, specified by device IDs in a format matching uploadType. |

## Example

```python
from verizon.models.check_order_status_request import CheckOrderStatusRequest
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList

check_order_status_request = CheckOrderStatusRequest(
    account_name='1223334444-00001',
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
    order_request_id='f55fea16-3664-4a32-ae9d-c0cbe3eedf1d'
)
```

