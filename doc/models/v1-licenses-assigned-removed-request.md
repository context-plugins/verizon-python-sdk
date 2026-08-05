
# V1 Licenses Assigned Removed Request

IMEIs of the devices to assign licenses to.

## Structure

`V1LicensesAssignedRemovedRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[str]` | Required | The IMEIs of the devices. |

## Example

```python
from verizon.models.v1_licenses_assigned_removed_request import V1LicensesAssignedRemovedRequest

v1_licenses_assigned_removed_request = V1LicensesAssignedRemovedRequest(
    device_list=[
        '900000000000001',
        '900000000000998',
        '900000000000999'
    ]
)
```

