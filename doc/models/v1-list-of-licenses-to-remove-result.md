
# V1 List of Licenses to Remove Result

List of licenses assigned.

## Structure

`V1ListOfLicensesToRemoveResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | The total number of devices on the cancellation candidate list. |
| `device_list` | `List[str]` | Optional | The IMEIs of the devices. |

## Example

```python
from verizon.models.v1_list_of_licenses_to_remove_result import V1ListOfLicensesToRemoveResult

v1_list_of_licenses_to_remove_result = V1ListOfLicensesToRemoveResult(
    count=2,
    device_list=[
        '900000000000001',
        '900000000000999'
    ]
)
```

