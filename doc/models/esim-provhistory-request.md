
# ESIM Provhistory Request

## Structure

`ESIMProvhistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `device_filter` | [`List[DeviceId2]`](../../doc/models/device-id-2.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `earliest` | `datetime` | Optional | - |
| `latest` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.device_id_2 import DeviceId2
from verizon.models.esim_provhistory_request import ESIMProvhistoryRequest

e_sim_provhistory_request = ESIMProvhistoryRequest(
    account_name='0000123456-00001',
    device_filter=[
        DeviceId2(
            id='id4',
            kind='kind2'
        ),
        DeviceId2(
            id='id4',
            kind='kind2'
        ),
        DeviceId2(
            id='id4',
            kind='kind2'
        )
    ],
    earliest=dateutil.parser.parse('2021-10-15T04:49:35-00:00'),
    latest=dateutil.parser.parse('2021-10-15T04:49:49-00:00')
)
```

