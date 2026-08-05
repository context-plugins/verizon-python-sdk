
# Device Extended Diagnostics Request

Request for obtaining device extended diagnostics.

## Structure

`DeviceExtendedDiagnosticsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The Verizon billing account that the device belongs to. An account name is usually numeric, and must include any leading zeros. |
| `device_list` | [`List[DeviceId]`](../../doc/models/device-id.md) | Required | The device for which you want diagnostic information, specified by the device's MDN. |

## Example

```python
from verizon.models.device_extended_diagnostics_request import DeviceExtendedDiagnosticsRequest
from verizon.models.device_id import DeviceId

device_extended_diagnostics_request = DeviceExtendedDiagnosticsRequest(
    account_name='1223334444-00001',
    device_list=[
        DeviceId(
            id='10-digit MDN',
            kind='mdn'
        )
    ]
)
```

