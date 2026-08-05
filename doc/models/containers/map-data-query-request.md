
# Map Data Query Request

Request structure for querying MAP records. Provide either regionIntersectionPairs (coordinates) or geoJson, not both.

## Data Type

`ETXMAPMessageIntersectionCoordinates | ETXMAPMessageGeoJSONPolygon`

## Cases

| Type |
|  --- |
| [`ETXMAPMessageIntersectionCoordinates`](../../../doc/models/etxmap-message-intersection-coordinates.md) |
| [`ETXMAPMessageGeoJSONPolygon`](../../../doc/models/etxmap-message-geo-json-polygon.md) |

## ETXMAPMessageIntersectionCoordinates

### Initialization Code

#### Example

```python
value = ETXMAPMessageIntersectionCoordinates(
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

## ETXMAPMessageGeoJSONPolygon

### Initialization Code

#### Example

```python
value = ETXMAPMessageGeoJSONPolygon(
    geo_json=jsonpickle.decode('{"type":"Polygon","coordinates":[[[-77.14,39.01],[-77.03,39.01],[-77.03,38.85],[-77.14,38.85],[-77.14,39.01]]]}'),
    message_standard=ETXMessageStandardEnum.SAE,
    expected_type=ETXExpectedTypeEnum.BASE64,
    page_token='Y3Vyc29yX3Rva2VuX2V4YW1wbGU=',
    page_size=50
)
```

