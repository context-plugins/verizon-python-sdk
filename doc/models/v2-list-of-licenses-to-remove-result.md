
# V2 List of Licenses to Remove Result

List of created license cancellation devices.

## Structure

`V2ListOfLicensesToRemoveResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Required | The number of devices. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.v2_list_of_licenses_to_remove_result import V2ListOfLicensesToRemoveResult

v2_list_of_licenses_to_remove_result = V2ListOfLicensesToRemoveResult(
    count=2,
    device_list=[
        '990003425730535',
        '990000473475989'
    ]
)
```

