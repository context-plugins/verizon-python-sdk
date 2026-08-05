
# Status Response

## Structure

`StatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[a-z-0-9]{3,64}$` |
| `status` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `subrequests` | [`List[Subrequest]`](../../doc/models/subrequest.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.gio_device_id import GIODeviceId
from verizon.models.status_response import StatusResponse
from verizon.models.subrequest import Subrequest

status_response = StatusResponse(
    request_id='d1f08526-5443-4054-9a29-4456490ea9f8',
    status='Success',
    subrequests=[
        Subrequest(
            ids=GIODeviceId(
                kind='kind2',
                id='id4'
            ),
            status='status2'
        ),
        Subrequest(
            ids=GIODeviceId(
                kind='kind2',
                id='id4'
            ),
            status='status2'
        ),
        Subrequest(
            ids=GIODeviceId(
                kind='kind2',
                id='id4'
            ),
            status='status2'
        )
    ]
)
```

