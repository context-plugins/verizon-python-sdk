
# A Request Body for Usage

## Structure

`ARequestBodyForUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`List[ReadySimDeviceId]`](../../doc/models/ready-sim-device-id.md) | Optional | - |
| `start_time` | `datetime` | Optional | - |
| `end_time` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.a_request_body_for_usage import ARequestBodyForUsage
from verizon.models.ready_sim_device_id import ReadySimDeviceId

a_request_body_for_usage = ARequestBodyForUsage(
    device_id=[
        ReadySimDeviceId(
            kind='kind8',
            id='id0'
        )
    ],
    start_time=dateutil.parser.parse('2021-08-15T00:00:00Z'),
    end_time=dateutil.parser.parse('2021-08-16T00:00:00Z')
)
```

