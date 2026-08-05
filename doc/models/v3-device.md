
# V3 Device

Device information.

## Structure

`V3Device`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `request_status` | `str` | Optional | Success or failure. |
| `result_reason` | `str` | Optional | - |
| `mdn` | `str` | Optional | MDN. |
| `model` | `str` | Optional | Device model. |
| `make` | `str` | Optional | Device make. |
| `firmware` | `str` | Optional | Device firmware version. |
| `fota_eligible` | `bool` | Optional | Value=true if the device software can be upgraded over the air using the Software Management Services API. |
| `status` | `str` | Optional | Device status. |
| `license_assigned` | `bool` | Optional | License assigned device. |
| `protocol` | `str` | Optional | Firmware protocol. Valid values include: LWM2M, OMADM, HTTP or NONE. |
| `software_list` | [`List[V3SoftwareInfo]`](../../doc/models/v3-software-info.md) | Optional | List of sofware.<br><br>**Constraints**: *Maximum Items*: `1000` |
| `file_list` | [`List[V3SoftwareInfo]`](../../doc/models/v3-software-info.md) | Optional | List of files.<br><br>**Constraints**: *Maximum Items*: `1000` |
| `create_time` | `str` | Optional | The date and time of when the device is created. |
| `status_time` | `str` | Optional | The date and time of when the device firmware or software is updated. |
| `update_time` | `str` | Optional | The date and time of when the device is updated. |
| `refresh_time` | `str` | Optional | The date and time of when the device is refreshed. |
| `last_connection_time` | `datetime` | Optional | The date and time of when the device reachability is checked. |

## Example

```python
import dateutil.parser

from verizon.models.v3_device import V3Device

v3_device = V3Device(
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
```

