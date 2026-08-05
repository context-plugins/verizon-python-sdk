
# Find Device by Property Response List

A success response includes an array of all matching devices. Each device includes the full device resource definition.

## Structure

`FindDeviceByPropertyResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_property` | [`List[FindDeviceByPropertyResponse]`](../../doc/models/find-device-by-property-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.find_device_by_property_response import FindDeviceByPropertyResponse
from verizon.models.find_device_by_property_response_list import FindDeviceByPropertyResponseList

find_device_by_property_response_list = FindDeviceByPropertyResponseList(
    device_property=[
        FindDeviceByPropertyResponse(
            billingaccountid='billingaccountid4',
            createdon='createdon6',
            eventretention='eventretention2',
            iccid='iccid4',
            id='id8'
        ),
        FindDeviceByPropertyResponse(
            billingaccountid='billingaccountid4',
            createdon='createdon6',
            eventretention='eventretention2',
            iccid='iccid4',
            id='id8'
        ),
        FindDeviceByPropertyResponse(
            billingaccountid='billingaccountid4',
            createdon='createdon6',
            eventretention='eventretention2',
            iccid='iccid4',
            id='id8'
        )
    ]
)
```

