
# Request Body for Usage

## Structure

`RequestBodyForUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | - |
| `device_id` | [`List[ReadySimDeviceId]`](../../doc/models/ready-sim-device-id.md) | Optional | - |
| `start_time` | `datetime` | Optional | - |
| `end_time` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.ready_sim_device_id import ReadySimDeviceId
from verizon.models.request_body_for_usage import RequestBodyForUsage

request_body_for_usage = RequestBodyForUsage(
    account_id='0000123456-000001',
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

