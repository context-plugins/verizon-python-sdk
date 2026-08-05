
# V3 Add or Remove Device Request

Devices to add or remove from existing software upgrade information.

## Structure

`V3AddOrRemoveDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Operation either 'append' or 'remove' |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.v3_add_or_remove_device_request import V3AddOrRemoveDeviceRequest

v3_add_or_remove_device_request = V3AddOrRemoveDeviceRequest(
    mtype='remove',
    device_list=[
        '15-digit IMEI'
    ]
)
```

