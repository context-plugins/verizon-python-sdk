
# Device Upload Request

## Structure

`DeviceUploadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | - |
| `email_address` | `str` | Required | - |
| `device_sku` | `str` | Required | - |
| `upload_type` | `str` | Required | - |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.device_upload_request import DeviceUploadRequest

device_upload_request = DeviceUploadRequest(
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
    email_address='bob@mycompany.com',
    device_sku='VZW123456',
    upload_type='IMEI'
)
```

