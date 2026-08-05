
# V3 License Assigned Removed Result

License assignment/removal response.

## Structure

`V3LicenseAssignedRemovedResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `lic_count` | `int` | Required | Total license count. |
| `lic_used_count` | `int` | Required | Assigned license count. |
| `device_list` | [`List[V3DeviceStatus]`](../../doc/models/v3-device-status.md) | Required | List of devices with id in IMEI. |

## Example

```python
import dateutil.parser

from verizon.models.v3_device_status import V3DeviceStatus
from verizon.models.v3_license_assigned_removed_result import V3LicenseAssignedRemovedResult

v3_license_assigned_removed_result = V3LicenseAssignedRemovedResult(
    account_name='0000123456-00001',
    lic_count=1000,
    lic_used_count=2,
    device_list=[
        V3DeviceStatus(
            device_id='15-digit IMEI',
            status='UpgradePending',
            result_reason='Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC',
            updated_time=dateutil.parser.parse('2022-08-05T21:05:27.129Z'),
            recent_attempt_time=dateutil.parser.parse('2022-10-05T21:05:01.19Z'),
            next_attempt_time=dateutil.parser.parse('2022-10-06T18:35:00Z')
        )
    ]
)
```

