
# Search Device by Property Response List

A success response includes an array of all matching devices.

## Structure

`SearchDeviceByPropertyResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_property` | [`List[SearchDeviceByPropertyResponse]`](../../doc/models/search-device-by-property-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.acceleration import Acceleration
from verizon.models.fields_1 import Fields1
from verizon.models.search_device_by_property_fields import SearchDeviceByPropertyFields
from verizon.models.search_device_by_property_response import SearchDeviceByPropertyResponse
from verizon.models.search_device_by_property_response_list import SearchDeviceByPropertyResponseList

search_device_by_property_response_list = SearchDeviceByPropertyResponseList(
    device_property=[
        SearchDeviceByPropertyResponse(
            billingaccountid='billingaccountid4',
            createdon='createdon6',
            eventretention='eventretention2',
            fields=Fields1(
                item=SearchDeviceByPropertyFields(
                    acceleration=Acceleration(
                        x='x6',
                        y='y4',
                        z='z6'
                    ),
                    battery='battery0',
                    humidity='humidity4',
                    light='light6',
                    pressure='pressure2'
                )
            ),
            iccid='iccid4'
        ),
        SearchDeviceByPropertyResponse(
            billingaccountid='billingaccountid4',
            createdon='createdon6',
            eventretention='eventretention2',
            fields=Fields1(
                item=SearchDeviceByPropertyFields(
                    acceleration=Acceleration(
                        x='x6',
                        y='y4',
                        z='z6'
                    ),
                    battery='battery0',
                    humidity='humidity4',
                    light='light6',
                    pressure='pressure2'
                )
            ),
            iccid='iccid4'
        ),
        SearchDeviceByPropertyResponse(
            billingaccountid='billingaccountid4',
            createdon='createdon6',
            eventretention='eventretention2',
            fields=Fields1(
                item=SearchDeviceByPropertyFields(
                    acceleration=Acceleration(
                        x='x6',
                        y='y4',
                        z='z6'
                    ),
                    battery='battery0',
                    humidity='humidity4',
                    light='light6',
                    pressure='pressure2'
                )
            ),
            iccid='iccid4'
        )
    ]
)
```

