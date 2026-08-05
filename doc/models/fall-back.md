
# Fall Back

## Structure

`FallBack`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | List[List[List[[deviceIdarray](../../doc/models/device-idarray.md)]]] \| None | Optional | This is 2d List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example

```python
from verizon.models.device_idarray import DeviceIdarray
from verizon.models.fall_back import FallBack

fall_back = FallBack(
    devices=[
        [
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ],
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ],
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ]
        ],
        [
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ],
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ],
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ]
        ],
        [
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ],
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ],
            [
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                ),
                DeviceIdarray(
                    kind='kind6',
                    id='id8'
                )
            ]
        ]
    ],
    account_name='accountName2'
)
```

