
# Device List Result

Device list information.

## Structure

`DeviceListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `device_count` | `int` | Required | Total device count. |
| `device_list` | [`List[V3Device]`](../../doc/models/v3-device.md) | Required | List of devices with id in IMEI.<br><br>**Constraints**: *Maximum Items*: `1000` |

## Example

```python
import dateutil.parser

from verizon.models.device_list_result import DeviceListResult
from verizon.models.v3_device import V3Device

device_list_result = DeviceListResult(
    account_name='0000123456-00001',
    device_count=1,
    device_list=[
        V3Device(
            device_id='15-digit IMEI',
            request_status='requestStatus2',
            result_reason='resultReason2',
            mdn='10-digit MDN',
            model='GM01Q',
            make='SEQUANS COMMUNICATIONS',
            firmware='SR1.2.0.0-10657',
            fota_eligible=True,
            status='Active',
            license_assigned=True,
            protocol='LWM2M',
            create_time='2021-06-03 00:03:56.079 +0000 UTC',
            status_time='2021-06-03 00:03:56.079 +0000 UTC',
            refresh_time='2021-06-03 00:03:56.079 +0000 UTC',
            last_connection_time=dateutil.parser.parse('2012-04-23T18:25:43.511Z')
        )
    ]
)
```

