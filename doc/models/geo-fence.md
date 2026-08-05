
# Geo Fence

The GeoJSON representation of geofence. Geofence supports the following geometry types: LineString, Polygon, MultiLineString, and MultiPolygon. The system only supports a single Feature in the FeatureCollection, so only one Line, Polygon, MultiLine or MultiPolygon can be defined within one Geofencing configuration.

## Structure

`GeoFence`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Required | - |
| `features` | [`List[FeatureItem]`](../../doc/models/feature-item.md) | Required | **Constraints**: *Minimum Items*: `1`, *Maximum Items*: `1` |

## Example

```python
import jsonpickle

from verizon.models.feature_item import FeatureItem
from verizon.models.geo_fence import GeoFence
from verizon.models.line_string import LineString
from verizon.models.type_1_enum import Type1Enum
from verizon.models.type_2_enum import Type2Enum
from verizon.models.type_enum import TypeEnum

geo_fence = GeoFence(
    mtype=TypeEnum.FEATURECOLLECTION,
    features=[
        FeatureItem(
            mtype=Type1Enum.FEATURE,
            geometry=LineString(
                mtype=Type2Enum.LINESTRING,
                coordinates=[
                    [
                        51.53,
                        51.54
                    ],
                    [
                        51.53,
                        51.54
                    ]
                ]
            ),
            properties=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        )
    ]
)
```

