
# V1 Licenses Assigned Removed Result

License assignment or removal confirmation.

## Structure

`V1LicensesAssignedRemovedResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `lic_count` | `int` | Optional | Total number of monthly licenses in an MRC subscription. |
| `lic_used_count` | `int` | Optional | Number of licenses assigned to devices after the request completed. |
| `device_list` | [`List[V1DeviceListItem]`](../../doc/models/v1-device-list-item.md) | Optional | A JSON object for each device that was in the request. |

## Example

```python
from verizon.models.v1_device_list_item import V1DeviceListItem
from verizon.models.v1_licenses_assigned_removed_result import V1LicensesAssignedRemovedResult

v1_licenses_assigned_removed_result = V1LicensesAssignedRemovedResult(
    account_name='0242078689-00001',
    lic_count=9000,
    lic_used_count=1000,
    device_list=[
        V1DeviceListItem(
            device_id='900000000000001',
            status='LicenseAssignSuccess',
            reason='Success'
        ),
        V1DeviceListItem(
            device_id='900000000000999',
            status='LicenseAssignSuccess',
            reason='Success'
        )
    ]
)
```

