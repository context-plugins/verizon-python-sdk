
# V2 List of Licenses to Remove

A list of license cancellation candidate devices.

## Structure

`V2ListOfLicensesToRemove`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Required | Cancellation candidate devices count. |
| `has_more_data` | `bool` | Required | Flag to indicat more devices. |
| `update_time` | `str` | Required | Last update time. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.v2_list_of_licenses_to_remove import V2ListOfLicensesToRemove

v2_list_of_licenses_to_remove = V2ListOfLicensesToRemove(
    count=6,
    has_more_data=False,
    update_time='2018-03-22 00:06:00.069 +0000 UTC',
    device_list=[
        '990003425730535',
        '990000473475989',
        '990005733420535',
        '990000347475989',
        '990007303425535',
        '990007590473489'
    ]
)
```

