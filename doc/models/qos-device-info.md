
# Qos Device Info

## Structure

`QosDeviceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`QosDeviceId`](../../doc/models/qos-device-id.md) | Required | - |
| `device_i_pv_6_addr` | `str` | Optional | - |
| `flow_info` | [`List[FlowInfo]`](../../doc/models/flow-info.md) | Required | - |

## Example

```python
from verizon.models.flow_info import FlowInfo
from verizon.models.qos_device_id import QosDeviceId
from verizon.models.qos_device_info import QosDeviceInfo

qos_device_info = QosDeviceInfo(
    device_id=QosDeviceId(
        id='10-digit phone number',
        kind='mdn'
    ),
    flow_info=[
        FlowInfo(
            flow_server='[IPv6 address]:port',
            flow_device='[IPv6 address]:port',
            flow_direction='UPLINK',
            flow_protocol='UDP',
            qci_option='Premium'
        )
    ],
    device_i_pv_6_addr='IPv6 address'
)
```

