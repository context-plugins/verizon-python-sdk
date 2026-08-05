
# V1 List of Licenses to Remove

List of cancellation candidate devices.

## Structure

`V1ListOfLicensesToRemove`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | The total number of devices on the list. |
| `has_more_data` | `bool` | Optional | True if there are more devices to retrieve. |
| `update_time` | `datetime` | Optional | The date and time that the list was last updated. |
| `device_list` | `List[str]` | Optional | The IMEIs of the devices. |

## Example

```python
import dateutil.parser

from verizon.models.v1_list_of_licenses_to_remove import V1ListOfLicensesToRemove

v1_list_of_licenses_to_remove = V1ListOfLicensesToRemove(
    count=6,
    has_more_data=False,
    update_time=dateutil.parser.parse('2018-03-22T12:06:06.000Z'),
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

