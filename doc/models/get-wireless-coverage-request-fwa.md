
# Get Wireless Coverage Request FWA

Get wireless coverage FWA.

## Structure

`GetWirelessCoverageRequestFWA`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `request_type` | `str` | Required | Type of request made. FWA for address qualification and NW for Nationwide coverage.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `12`, *Pattern*: `^[A-Za-z]{1,12}$` |
| `location_type` | `str` | Required | Type of location detail.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `12`, *Pattern*: `^[A-Za-z]{3,12}$` |
| `locations` | [`Locations`](../../doc/models/locations.md) | Required | - |
| `network_types_list` | [`List[NetworkTypeObject]`](../../doc/models/network-type-object.md) | Required | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.address_item import AddressItem
from verizon.models.get_wireless_coverage_request_fwa import GetWirelessCoverageRequestFWA
from verizon.models.locations import Locations
from verizon.models.network_type_object import NetworkTypeObject

get_wireless_coverage_request_fwa = GetWirelessCoverageRequestFWA(
    account_name='0000123456-00001',
    request_type='NW',
    location_type='ADDRESS',
    locations=Locations(
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
            network_type='LTE'
        )
    ]
)
```

