
# Connectivity Management Success Result

Response to successful request.

## Structure

`ConnectivityManagementSuccessResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Optional | A value of “true” indicates that the device group was created successfully. |

## Example

```python
from verizon.models.connectivity_management_success_result import ConnectivityManagementSuccessResult

connectivity_management_success_result = ConnectivityManagementSuccessResult(
    success=True
)
```

