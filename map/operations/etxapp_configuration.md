<!-- Generated file — do not edit; regenerated with the SDK. -->

# EtxappConfiguration — operations

Accessor: `client.etxapp_configuration` · Source: `verizon/apis/etxapp_configuration.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.etxapp_configuration.create_configuration

- **Route**: `POST /api/v1/application/configurations/geofence`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def create_configuration(vendor_id: str, body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`, `body`
- **Params**: `vendor_id` — header `VendorID` · `body` — JSON body
- **Returns (parsed)**: `GeoFenceConfigurationResponse`
- **Returns (raw)**: `ApiResult[GeoFenceConfigurationResponse, CreateConfigurationErrorBody]`
- **Error**: `CreateConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ResponseError` [400, 403, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeoFenceConfigurationRequest` | `verizon/models/geo_fence_configuration_request.py` |
| `GeoFenceConfigurationRequestDict` | `verizon/models/geo_fence_configuration_request.py` |
| `GeoFenceConfigurationResponse` | `verizon/models/geo_fence_configuration_response.py` |
| `CreateConfigurationErrorBody` | `verizon/errors/create_configuration_error.py` |
| `ResponseError` | `verizon/models/response_error.py` |

### client.etxapp_configuration.delete_configuration

- **Route**: `DELETE /api/v1/application/configurations/geofence`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def delete_configuration(id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `vendor_id`
- **Params**: `id` — query · `vendor_id` — header `VendorID`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteConfigurationErrorBody]`
- **Error**: `DeleteConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ResponseError` [403, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteConfigurationErrorBody` | `verizon/errors/delete_configuration_error.py` |
| `ResponseError` | `verizon/models/response_error.py` |

### client.etxapp_configuration.get_configuration

- **Route**: `GET /api/v1/application/configurations/geofence`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def get_configuration(id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `vendor_id`
- **Params**: `id` — query · `vendor_id` — header `VendorID`
- **Returns (parsed)**: `GeoFenceConfigurationResponse`
- **Returns (raw)**: `ApiResult[GeoFenceConfigurationResponse, GetConfigurationErrorBody]`
- **Error**: `GetConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ResponseError` [403, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeoFenceConfigurationResponse` | `verizon/models/geo_fence_configuration_response.py` |
| `GetConfigurationErrorBody` | `verizon/errors/get_configuration_error.py` |
| `ResponseError` | `verizon/models/response_error.py` |

### client.etxapp_configuration.get_configuration_list

- **Route**: `GET /api/v1/application/configurations/geofence/ids`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def get_configuration_list(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`
- **Params**: `vendor_id` — header `VendorID`
- **Returns (parsed)**: `list[ConfigurationListItem]`
- **Returns (raw)**: `ApiResult[list[ConfigurationListItem], GetConfigurationListErrorBody]`
- **Error**: `GetConfigurationListErrorBody` — **Case A (typed)**
- **Error arms**: `ResponseError` [403, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfigurationListItem` | `verizon/models/configuration_list_item.py` |
| `GetConfigurationListErrorBody` | `verizon/errors/get_configuration_list_error.py` |
| `ResponseError` | `verizon/models/response_error.py` |

### client.etxapp_configuration.update_configuration

- **Route**: `PUT /api/v1/application/configurations/geofence`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def update_configuration(id: str, vendor_id: str, body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `vendor_id`, `body`
- **Params**: `id` — query · `vendor_id` — header `VendorID` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateConfigurationErrorBody]`
- **Error**: `UpdateConfigurationErrorBody` — **Case A (typed)**
- **Error arms**: `ResponseError` [400, 403, 404, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeoFenceConfigurationUpdateRequest` | `verizon/models/geo_fence_configuration_update_request.py` |
| `GeoFenceConfigurationUpdateRequestDict` | `verizon/models/geo_fence_configuration_update_request.py` |
| `UpdateConfigurationErrorBody` | `verizon/errors/update_configuration_error.py` |
| `ResponseError` | `verizon/models/response_error.py` |

