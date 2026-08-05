# Map-Message-Controller

Endpoints for ingesting, querying, and deleting V2X MAP messages.

```python
map_message_controller = client.map_message_controller
```

## Class Name

`MapMessageController`

## Methods

* [Download MAP Messages](../../doc/controllers/map-message-controller.md#download-map-messages)
* [Ingest MAP Messages](../../doc/controllers/map-message-controller.md#ingest-map-messages)
* [Query Map Messages](../../doc/controllers/map-message-controller.md#query-map-messages)
* [Delete Map Message](../../doc/controllers/map-message-controller.md#delete-map-message)


# Download MAP Messages

**This endpoint is deprecated.**

This endpoint is deprecated. (Use /api/v2/mapdata/query for new integrations).

This endpoint allows user to download SAE J2735 or ETSI MAP messages in ASN.1 UPER base64 encoded format. The area for the MAP messages is needed to be defined in the query.

**Required request header:** `Accept` — specifies the response format. Omitting this header will result in a `400 Bad Request`. Supported values:

- `text/plain` — ASN.1 UPER base64-encoded MAP messages (one per line)
- `application/json` — JSON-encoded MAP messages

```python
def download_map_messages(self,
                         vendor_id,
                         geofence)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [sessionToken](../../doc/auth/custom-header-signature-1.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_id` | `str` | Header, Required | The VendorID set during the Vendor registration call.<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+$` |
| `geofence` | [`GeofencePolygon`](../../doc/models/geofence-polygon.md) | Query, Required | GeoJSON Polygon defining the area to retrieve MAP messages for. |

## Response Type

**200**: Line separated ASN.1 UPER J2735/ETSI base64 encoded MapData messages

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
vendor_id = 'VzMapManager'

geofence = GeofencePolygon(
    mtype=ETXMAPMessageGeofenceGeometryEnum.POLYGON,
    coordinates=[
        [
            -77.479395,
            38.990773
        ],
        [
            -77.114566,
            38.99944
        ],
        [
            -77.100228,
            38.817204
        ],
        [
            -77.418059,
            38.827754
        ],
        [
            -77.479395,
            38.990773
        ]
    ]
)

result = map_message_controller.download_map_messages(
    vendor_id,
    geofence
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 401 | Unauthorized | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 403 | Forbidden | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 404 | Not found | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 429 | Too many requests | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 503 | Internal server error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| Default | unexpected error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |


# Ingest MAP Messages

This endpoint allows the user to upload map messages in ASN.1 UPER base64 encoded format or JER (JSON) formats. The MAP data message can have more than one intersections in it.
Both SAE and ETSI defined MAP messages are supported. The SAE type MAP messages have to be wrapped in a MessageFrame, as defined in the SAE J2735 standard.
The ETSI type MAP messages are expected as MAPEM structures that include the ETSI header, as defined in the ETSI TS 103 301 standard.
Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

**Required request header:** `Content-Type` — specifies the format of the request body. Omitting or sending an unsupported value will result in a `415 Unsupported Media Type`. Supported values:

- `text/plain` — ASN.1 UPER base64-encoded MAP message
- `application/json` — JSON representation of the MAP message

```python
def ingest_map_messages(self,
                       vendor_id,
                       map_data_message_standard,
                       body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [sessionToken](../../doc/auth/custom-header-signature-1.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_id` | `str` | Header, Required | The VendorID set during the Vendor registration call.<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+$` |
| `map_data_message_standard` | [`ETXMessageStandardEnum`](../../doc/models/etx-message-standard-enum.md) | Header, Required | Select which V2X messaging standard will be used for the message generation. The following options are supported:<br><br>- "etsi": The message will be generated using the ETSI (European) standard (e.g. MAPEM).<br>- "sae": The message will be generated using the SAE J2735 (North American) standard (e.g. MAP).<br>- if not sent while POST, defaults to "sae"<br><br>**Constraints**: *Maximum Length*: `4`, *Pattern*: `^(etsi\|sae)$` |
| `body` | [`ETXMAPDataIngestRequest`](../../doc/models/etxmap-data-ingest-request.md) | Body, Required | UPER/ASN.1 J2735/ETSI base64 encoded MapData message or JSON representation of the MapData message. |

## Response Type

**201**: Map message/s successfully uploaded

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
vendor_id = 'VzMapManager'

map_data_message_standard = ETXMessageStandardEnum.SAE

body = ETXMAPDataIngestRequest(
    message_id=18,
    value=jsonpickle.decode('{"intersections":[{"id":{"region":0,"id":156},"laneWidth":366,"refPoint":{"lat":389284111,"long":-772410713},"revision":3}],"msgIssueRevision":3}')
)

result = map_message_controller.ingest_map_messages(
    vendor_id,
    map_data_message_standard,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 401 | Unauthorized | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 403 | Forbidden | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 405 | Method not allowed | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 429 | Too many requests | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 503 | Internal server error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| Default | unexpected error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |


# Query Map Messages

This endpoint allows users to download SAE J2735 or ETSI MAP messages as a JSON list.
Depending on the expectedType parameter, the response contains either ASN.1 UPER base64-encoded messages with their respective region and intersection IDs, or fully decoded JSON messages.
The area for MAP message retrieval must be defined in the request body using one of two methods:
An array of region and intersection ID pairs, or a GeoJSON geofence specification.

```python
def query_map_messages(self,
                      vendor_id,
                      body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [sessionToken](../../doc/auth/custom-header-signature-1.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_id` | `str` | Header, Required | The VendorID set during the Vendor registration call.<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+$` |
| `body` | [ETX MAP Message Intersection Coordinates](../../doc/models/etxmap-message-intersection-coordinates.md) \| [ETX MAP Message GeoJSON Polygon](../../doc/models/etxmap-message-geo-json-polygon.md) | Body, Required | Request structure for querying MAP records. Provide either regionIntersectionPairs (coordinates) or geoJson, not both. |

## Response Type

**200**: Successfully retrieved MAP messages. Returns a JSON array where each element contains either a base64 string or parsed message object.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[Any]`.

## Example Usage

```python
vendor_id = 'VzMapManager'

body = ETXMAPMessageIntersectionCoordinates(
    region_intersection_pairs=[
        RegionIntersectionPair(
            intersection_id=5233,
            region_id=100
        )
    ],
    message_standard=ETXMessageStandardEnum.SAE,
    expected_type=ETXExpectedTypeEnum.BASE64,
    page_size=50
)

result = map_message_controller.query_map_messages(
    vendor_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
[
  {
    "messageStandard": "sae",
    "regionId": 100,
    "intersectionId": 5233,
    "payload": "asdfKDSiORel23=="
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 401 | Unauthorized | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 403 | Forbidden | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 405 | Method not allowed | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 429 | Too many requests | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 503 | Internal server error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| Default | unexpected error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |


# Delete Map Message

Removes a map message for the specified region and intersection ID.

```python
def delete_map_message(self,
                      region_id,
                      i_10_nid)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [sessionToken](../../doc/auth/custom-header-signature-1.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region_id` | `str` | Template, Required | Region ID to filter the map messages. |
| `i_10_nid` | `str` | Template, Required | Intersection ID to filter the map messages. |

## Response Type

**204**: Deleted successfully (No Content)

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
region_id = '0'

i_10_nid = '58399'

result = map_message_controller.delete_map_message(
    region_id,
    i_10_nid
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 401 | Unauthorized | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 403 | Forbidden | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 404 | Not found | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 429 | Too many requests | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| 503 | Internal server error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |
| Default | unexpected error | [`MdmErrorResponseException`](../../doc/models/mdm-error-response-exception.md) |

