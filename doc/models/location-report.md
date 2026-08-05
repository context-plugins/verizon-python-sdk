
# Location Report

Location information for up to 1,000 devices.

## Structure

`LocationReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dev_location_list` | [`List[Location]`](../../doc/models/location.md) | Optional | Device location information. |
| `has_more_data` | `bool` | Optional | True if there are more device locations to retrieve. |
| `start_index` | `str` | Optional | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices to be returned (hasMoreData=true), set startIndex=1000 for the second request, 2000 for the third request, etc. |
| `total_count` | `int` | Optional | The total number of devices in the original request and in the report. |
| `txid` | `str` | Optional | The transaction ID of the report. |

## Example

```python
from verizon.models.location import Location
from verizon.models.location_report import LocationReport
from verizon.models.position_data import PositionData
from verizon.models.position_error import PositionError

location_report = LocationReport(
    dev_location_list=[
        Location(
            msid='7892345678',
            pd=PositionData(
                time='20170520004421',
                utcoffset='utcoffset2',
                x='33.45324',
                y='-84.59621',
                radius='5571',
                qos=False
            ),
            error=PositionError(
                time='time4',
                utcoffset='utcoffset4',
                mtype='type6',
                info='info4'
            )
        ),
        Location(
            msid='8583239709',
            pd=PositionData(
                time='20170525214342',
                utcoffset='utcoffset2',
                x='38.8408694',
                y='-105.0422583',
                radius='3866',
                qos=False
            ),
            error=PositionError(
                time='time4',
                utcoffset='utcoffset4',
                mtype='type6',
                info='info4'
            )
        ),
        Location(
            msid='7897654321',
            pd=PositionData(
                time='time2',
                utcoffset='utcoffset2',
                x='x8',
                y='y6',
                radius='radius0'
            ),
            error=PositionError(
                time='20170525214342',
                utcoffset='utcoffset4',
                mtype='POSITION METHOD FAILURE',
                info='Exception code=ABSENT SUBSCRIBER'
            )
        )
    ],
    has_more_data=False,
    start_index='0',
    total_count=3,
    txid='2017-12-11Te8b47da2-eeee-ffff-gggg-61815e1e97e9'
)
```

