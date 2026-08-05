
# Get Network Conditions Request

Get network conditions.

## Structure

`GetNetworkConditionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `location_type` | `str` | Required | Type of location detail. |
| `coordinates` | [`Coordinates`](../../doc/models/coordinates.md) | Required | Coordinates information. |

## Example

```python
from verizon.models.coordinates import Coordinates
from verizon.models.get_network_conditions_request import GetNetworkConditionsRequest

get_network_conditions_request = GetNetworkConditionsRequest(
    account_name='0000123456-00001',
    location_type='LONGLAT',
    coordinates=Coordinates(
        latitude='-33.84819',
        longitude='151.22049'
    )
)
```

