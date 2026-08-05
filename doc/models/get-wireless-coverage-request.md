
# Get Wireless Coverage Request

Get wireless coverage.

## Structure

`GetWirelessCoverageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `request_type` | `str` | Required | Type of request made. FWA for address qualification and NW for Nationwide coverage.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `12`, *Pattern*: `^[A-Za-z]{1,12}$` |
| `location_type` | `str` | Required | Type of location detail. |
| `locations` | [`Locationscoord`](../../doc/models/locationscoord.md) | Required | - |
| `network_types_list` | [`List[NetworkTypeObject]`](../../doc/models/network-type-object.md) | Required | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.coordinates import Coordinates
from verizon.models.get_wireless_coverage_request import GetWirelessCoverageRequest
from verizon.models.locationscoord import Locationscoord
from verizon.models.network_type_object import NetworkTypeObject

get_wireless_coverage_request = GetWirelessCoverageRequest(
    account_name='0000123456-00001',
    request_type='NW',
    location_type='LONGLAT',
    locations=Locationscoord(
        coordinates_list=[
            Coordinates(
                latitude='latitude6',
                longitude='longitude4'
            ),
            Coordinates(
                latitude='latitude6',
                longitude='longitude4'
            )
        ]
    ),
    network_types_list=[
        NetworkTypeObject(
            network_type='LTE'
        )
    ]
)
```

