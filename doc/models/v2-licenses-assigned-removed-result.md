
# V2 Licenses Assigned Removed Result

License assignment or removal confirmation.

## Structure

`V2LicensesAssignedRemovedResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `lic_total_count` | `int` | Required | Total license count. |
| `lic_used_count` | `int` | Required | Assigned license count. |
| `device_list` | [`List[V2DeviceStatus]`](../../doc/models/v2-device-status.md) | Required | List of devices with id in IMEI. |

## Example

```python
from verizon.models.v2_device_status import V2DeviceStatus
from verizon.models.v2_licenses_assigned_removed_result import V2LicensesAssignedRemovedResult

v2_licenses_assigned_removed_result = V2LicensesAssignedRemovedResult(
    account_name='0242078689-00001',
    lic_total_count=1000,
    lic_used_count=502,
    device_list=[
        V2DeviceStatus(
            device_id='990003425730524',
            status='Success',
            result_reason='Success'
        ),
        V2DeviceStatus(
            device_id='990000473475967',
            status='Failure',
            result_reason='Device does not exist.'
        )
    ]
)
```

