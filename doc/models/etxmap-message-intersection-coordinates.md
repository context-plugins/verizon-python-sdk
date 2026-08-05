
# ETXMAP Message Intersection Coordinates

Query MAP records using specific region and intersection identifier pairs

## Structure

`ETXMAPMessageIntersectionCoordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_standard` | [`ETXMessageStandardEnum`](../../doc/models/etx-message-standard-enum.md) | Optional | V2X messaging standard selection. Accepted values are 'sae' (SAE J2735) and 'etsi' (ETSI TS 103 301).<br><br>**Default**: `"sae"`<br><br>**Constraints**: *Maximum Length*: `4`, *Pattern*: `^(etsi\|sae)$` |
| `region_intersection_pairs` | [`List[RegionIntersectionPair]`](../../doc/models/region-intersection-pair.md) | Required | List of region and intersection ID pairs to retrieve MAP messages for.<br><br>**Constraints**: *Maximum Items*: `200` |
| `expected_type` | [`ETXExpectedTypeEnum`](../../doc/models/etx-expected-type-enum.md) | Optional | The format of the payload in the response body.<br><br>**Default**: `"BASE64"`<br><br>**Constraints**: *Maximum Length*: `6`, *Pattern*: `^(BASE64\|JSON)$` |
| `page_token` | `str` | Optional | Base64 encoded token used to retrieve the next page of results<br><br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[A-Za-z0-9+/]+=*$` |
| `page_size` | `int` | Optional | Maximum number of records to return in a single page<br><br>**Default**: `200`<br><br>**Constraints**: `>= 1`, `<= 500` |

## Example

```python
from verizon.models.etx_expected_type_enum import ETXExpectedTypeEnum
from verizon.models.etx_message_standard_enum import ETXMessageStandardEnum
from verizon.models.etxmap_message_intersection_coordinates import ETXMAPMessageIntersectionCoordinates
from verizon.models.region_intersection_pair import RegionIntersectionPair

etx_map_message_intersection_coordinates = ETXMAPMessageIntersectionCoordinates(
    region_intersection_pairs=[
        RegionIntersectionPair(
            intersection_id=5233,
            region_id=100
        )
    ],
    message_standard=ETXMessageStandardEnum.SAE,
    expected_type=ETXExpectedTypeEnum.BASE64,
    page_token='Y3Vyc29yX3Rva2VuX2V4YW1wbGU=',
    page_size=50
)
```

