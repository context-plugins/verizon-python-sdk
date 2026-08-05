
# Flow Info

## Structure

`FlowInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `flow_server` | `str` | Optional | - |
| `flow_device` | `str` | Optional | - |
| `flow_direction` | `str` | Optional | - |
| `flow_protocol` | `str` | Optional | - |
| `qci_option` | `str` | Optional | - |

## Example

```python
from verizon.models.flow_info import FlowInfo

flow_info = FlowInfo(
    flow_server='[IPv6 address]:port',
    flow_device='[IPv6 address]:port',
    flow_direction='UPLINK',
    flow_protocol='UDP',
    qci_option='Premium'
)
```

