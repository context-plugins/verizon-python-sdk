
# M2m V1 Intelligence Wireless Coverage Request

## Structure

`M2mV1IntelligenceWirelessCoverageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `request_type` | `str` | Optional | Type of request made. FWA for address qualification and NW for Nationwide coverage.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `12`, *Pattern*: `^[A-Za-z]{1,12}$` |
| `location_type` | `str` | Optional | Type of location detail.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `12`, *Pattern*: `^[A-Za-z]{3,12}$` |
| `locations` | [`Locations1`](../../doc/models/locations-1.md) | Optional | - |
| `network_types_list` | [`List[NetworkTypeObject]`](../../doc/models/network-type-object.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.address_item import AddressItem
from verizon.models.coordinates import Coordinates
from verizon.models.locations_1 import Locations1
from verizon.models.m2m__v1_intelligence_wireless_coverage_request import M2mV1IntelligenceWirelessCoverageRequest
from verizon.models.network_type_object import NetworkTypeObject

m2m__v1_intelligence_wireless_coverage_request = M2mV1IntelligenceWirelessCoverageRequest(
    account_name='0000123456-00001',
    request_type='NW',
    location_type='LONGLAT',
    locations=Locations1(
        coordinates_list=[
            Coordinates(
                latitude='latitude6',
                longitude='longitude4'
            ),
            Coordinates(
                latitude='latitude6',
                longitude='longitude4'
            )
        ],
        address_list=[
            AddressItem(
                address_line_1='addressLine10',
                address_line_2='addressLine28',
                city='city8',
                state='state4',
                country='country2'
            )
        ]
    ),
    network_types_list=[
        NetworkTypeObject(
            network_type='networkType2'
        ),
        NetworkTypeObject(
            network_type='networkType2'
        ),
        NetworkTypeObject(
            network_type='networkType2'
        )
    ]
)
```

