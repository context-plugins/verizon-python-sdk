
# Feature Item

## Structure

`FeatureItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Required | - |
| `geometry` | [LineString](../../doc/models/line-string.md) \| [Polygon](../../doc/models/polygon.md) \| [MultiLineString](../../doc/models/multi-line-string.md) \| [MultiPolygon](../../doc/models/multi-polygon.md) | Required | - |
| `properties` | `Any` | Required | Properties object for a GeoJSON Feature (no additional properties allowed). |

## Example

```python
import jsonpickle

from verizon.models.feature_item import FeatureItem
from verizon.models.line_string import LineString
from verizon.models.type_1_enum import Type1Enum
from verizon.models.type_2_enum import Type2Enum

feature_item = FeatureItem(
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
```

