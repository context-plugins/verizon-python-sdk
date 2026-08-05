
# ETXMAP Message Geo JSON Polygon

Query MAP records using a GeoJSON polygon to define the spatial area

## Structure

`ETXMAPMessageGeoJSONPolygon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_standard` | [`ETXMessageStandardEnum`](../../doc/models/etx-message-standard-enum.md) | Optional | V2X messaging standard selection. Accepted values are 'sae' (SAE J2735) and 'etsi' (ETSI TS 103 301).<br><br>**Default**: `"sae"`<br><br>**Constraints**: *Maximum Length*: `4`, *Pattern*: `^(etsi\|sae)$` |
| `geo_json` | `Any` | Required | GeoJSON Polygon defining the area to retrieve MAP messages for. |
| `expected_type` | [`ETXExpectedTypeEnum`](../../doc/models/etx-expected-type-enum.md) | Optional | The format of the payload in the response body.<br><br>**Default**: `"BASE64"`<br><br>**Constraints**: *Maximum Length*: `6`, *Pattern*: `^(BASE64\|JSON)$` |
| `page_token` | `str` | Optional | Base64 encoded token used to retrieve the next page of results<br><br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[A-Za-z0-9+/]+=*$` |
| `page_size` | `int` | Optional | Maximum number of records to return in a single page<br><br>**Default**: `200`<br><br>**Constraints**: `>= 1`, `<= 500` |

## Example

```python
import jsonpickle

from verizon.models.etx_expected_type_enum import ETXExpectedTypeEnum
from verizon.models.etx_message_standard_enum import ETXMessageStandardEnum
from verizon.models.etxmap_message_geo_json_polygon import ETXMAPMessageGeoJSONPolygon

etx_map_message_geo_json_polygon = ETXMAPMessageGeoJSONPolygon(
    geo_json=jsonpickle.decode('{"type":"Polygon","coordinates":[[[-77.14,39.01],[-77.03,39.01],[-77.03,38.85],[-77.14,38.85],[-77.14,39.01]]]}'),
    message_standard=ETXMessageStandardEnum.SAE,
    expected_type=ETXExpectedTypeEnum.BASE64,
    page_token='Y3Vyc29yX3Rva2VuX2V4YW1wbGU=',
    page_size=50
)
```

