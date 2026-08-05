
# Devices Request

Request body for retrieving devices based on vendorID and optional filters

## Structure

`DevicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_id` | `str` | Required | The ID the vendor wants its devices to be registered under. E.g. Verizon, GM, Ford, etc.<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+$` |
| `filter` | [DevicesFilter](../../doc/models/devices-filter.md) \| [PaginationFilter](../../doc/models/pagination-filter.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
from verizon.models.client_subtype_enum import ClientSubtypeEnum
from verizon.models.devices_filter import DevicesFilter
from verizon.models.devices_request import DevicesRequest
from verizon.models.etx_client_type_enum import EtxClientTypeEnum

devices_request = DevicesRequest(
    vendor_id='VerizonETX',
    filter=DevicesFilter(
        client_type=EtxClientTypeEnum.TRAFFICLIGHTCONTROLLER,
        client_subtype=ClientSubtypeEnum.EMERGENCYVEHICLE,
        mec_id='MecId4',
        page_size=182
    )
)
```

