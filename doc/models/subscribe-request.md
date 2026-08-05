
# Subscribe Request

## Structure

`SubscribeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_info` | [`List[QosDeviceInfo]`](../../doc/models/qos-device-info.md) | Required | - |

## Example

```python
from verizon.models.flow_info import FlowInfo
from verizon.models.qos_device_id import QosDeviceId
from verizon.models.qos_device_info import QosDeviceInfo
from verizon.models.subscribe_request import SubscribeRequest

subscribe_request = SubscribeRequest(
    account_name='0000123456-00001',
    device_info=[
        QosDeviceInfo(
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
    ]
)
```

