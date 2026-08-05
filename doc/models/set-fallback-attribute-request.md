
# Set Fallback Attribute Request

## Structure

`SetFallbackAttributeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Required | - |
| `carrier_name` | `str` | Optional | - |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.set_fallback_attribute_request import SetFallbackAttributeRequest

set_fallback_attribute_request = SetFallbackAttributeRequest(
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
    account_name='0000123456-00001',
    carrier_name='the name of the mobile service provider'
)
```

