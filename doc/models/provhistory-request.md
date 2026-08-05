
# Provhistory Request

## Structure

`ProvhistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Z a-z 0-9 \-]{3,32}$` |
| `device_filter` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `earliest` | `datetime` | Optional | - |
| `latest` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.gio_device_id import GIODeviceId
from verizon.models.provhistory_request import ProvhistoryRequest

provhistory_request = ProvhistoryRequest(
    account_name='0000123456-00001',
    device_filter=[
        GIODeviceId(
            kind='kind2',
            id='id4'
        ),
        GIODeviceId(
            kind='kind2',
            id='id4'
        )
    ],
    earliest=dateutil.parser.parse('2021-10-15T04:49:35-00:00'),
    latest=dateutil.parser.parse('2021-10-15T04:49:49-00:00')
)
```

