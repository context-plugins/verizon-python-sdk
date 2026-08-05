
# V2 List of Licenses to Remove Request

License cancellation candidate devices.

## Structure

`V2ListOfLicensesToRemoveRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | List creation option. |
| `count` | `int` | Optional | The number of devices. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.v2_list_of_licenses_to_remove_request import V2ListOfLicensesToRemoveRequest

v2_list_of_licenses_to_remove_request = V2ListOfLicensesToRemoveRequest(
    device_list=[
        '990003425730535',
        '990000473475989'
    ],
    mtype='append',
    count=2
)
```

