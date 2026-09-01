<!-- Generated file — do not edit; regenerated with the SDK. -->

# MapMessageController — operations

Accessor: `client.map_message_controller` · Source: `verizon/apis/map_message_controller.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.map_message_controller.delete_map_message

- **Route**: `DELETE /api/v2/mapdata/regionid/{regionId}/i10nid/{i10nid}`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def delete_map_message(region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `region_id`, `i10nid`
- **Params**: `region_id` — path `regionId` · `i10nid` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteMapMessageErrorBody]`
- **Error**: `DeleteMapMessageErrorBody` — **Case A (typed)**
- **Error arms**: `MdmErrorResponse` [400, 401, 403, 404, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteMapMessageErrorBody` | `verizon/errors/delete_map_message_error.py` |
| `MdmErrorResponse` | `verizon/models/mdm_error_response.py` |

### client.map_message_controller.download_map_messages

- **Route**: `GET /api/v2/mapdata`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def download_map_messages(geofence: GeofencePolygon | GeofencePolygonDict, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `geofence`, `vendor_id`
- **Params**: `geofence` — query `Geofence` · `vendor_id` — header `VendorID`
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, DownloadMapmessagesErrorBody]`
- **Error**: `DownloadMapmessagesErrorBody` — **Case A (typed)**
- **Error arms**: `MdmErrorResponse` [400, 401, 403, 404, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeofencePolygon` | `verizon/models/geofence_polygon.py` |
| `GeofencePolygonDict` | `verizon/models/geofence_polygon.py` |
| `DownloadMapmessagesErrorBody` | `verizon/errors/download_mapmessages_error.py` |
| `MdmErrorResponse` | `verizon/models/mdm_error_response.py` |

### client.map_message_controller.ingest_map_messages

- **Route**: `POST /api/v2/mapdata`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def ingest_map_messages(vendor_id: str, map_data_message_standard: EtxmessageStandardEnumOrStr, body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`, `map_data_message_standard`, `body`
- **Params**: `vendor_id` — header `VendorID` · `map_data_message_standard` — header `MessageStandard` · `body` — JSON body
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, IngestMapmessagesErrorBody]`
- **Error**: `IngestMapmessagesErrorBody` — **Case A (typed)**
- **Error arms**: `MdmErrorResponse` [400, 401, 403, 405, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EtxmessageStandardEnumOrStr` | `verizon/models/enums/etxmessage_standard_enum.py` |
| `EtxMapDataIngestRequest` | `verizon/models/etx_map_data_ingest_request.py` |
| `EtxMapDataIngestRequestDict` | `verizon/models/etx_map_data_ingest_request.py` |
| `IngestMapmessagesErrorBody` | `verizon/errors/ingest_mapmessages_error.py` |
| `MdmErrorResponse` | `verizon/models/mdm_error_response.py` |

### client.map_message_controller.query_map_messages

- **Route**: `POST /api/v2/mapdata/query`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def query_map_messages(vendor_id: str, body: MapDataQueryRequest | MapDataQueryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`, `body`
- **Params**: `vendor_id` — header `VendorID` · `body` — JSON body
- **Returns (parsed)**: `list[Any]`
- **Returns (raw)**: `ApiResult[list[Any], QueryMapMessagesErrorBody]`
- **Error**: `QueryMapMessagesErrorBody` — **Case A (typed)**
- **Error arms**: `MdmErrorResponse` [400, 401, 403, 405, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MapDataQueryRequest` | `verizon/models/unions/map_data_query_request.py` |
| `MapDataQueryRequestDict` | `verizon/models/unions/map_data_query_request.py` |
| `QueryMapMessagesErrorBody` | `verizon/errors/query_map_messages_error.py` |
| `MdmErrorResponse` | `verizon/models/mdm_error_response.py` |

