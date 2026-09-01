<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsDevices — operations

Accessor: `client.sensor_insights_devices` · Source: `verizon/apis/sensor_insights_devices.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_devices.sensor_insights_device_action_set_request

- **Route**: `POST /dm/v1/devices/actions/set`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_device_action_set_request(body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoDeviceActionSetResponse`
- **Returns (raw)**: `ApiResult[DtoDeviceActionSetResponse, SensorInsightsDeviceActionSetRequestErrorBody]`
- **Error**: `SensorInsightsDeviceActionSetRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError403` [403] · `ManagementError404` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DmV1DevicesActionsSetRequest` | `verizon/models/unions/dm_v1_devices_actions_set_request.py` |
| `DmV1DevicesActionsSetRequestDict` | `verizon/models/unions/dm_v1_devices_actions_set_request.py` |
| `DtoDeviceActionSetResponse` | `verizon/models/dto_device_action_set_response.py` |
| `SensorInsightsDeviceActionSetRequestErrorBody` | `verizon/errors/sensor_insights_device_action_set_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |

### client.sensor_insights_devices.sensor_insights_last_reported_time_request

- **Route**: `POST /dm/v1/devices/lastreported`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_last_reported_time_request(body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoLastReportedTimeResponse`
- **Returns (raw)**: `ApiResult[DtoLastReportedTimeResponse, SensorInsightsLastReportedTimeRequestErrorBody]`
- **Error**: `SensorInsightsLastReportedTimeRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError403` [403] · `ManagementError404` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoLastReportedTimeRequest` | `verizon/models/dto_last_reported_time_request.py` |
| `DtoLastReportedTimeRequestDict` | `verizon/models/dto_last_reported_time_request.py` |
| `DtoLastReportedTimeResponse` | `verizon/models/dto_last_reported_time_response.py` |
| `SensorInsightsLastReportedTimeRequestErrorBody` | `verizon/errors/sensor_insights_last_reported_time_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |

### client.sensor_insights_devices.sensor_insights_list_device_experience_history_request

- **Route**: `POST /dm/v1/devices/experience/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_device_experience_history_request(body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[UserDeviceExperienceHistory]`
- **Returns (raw)**: `ApiResult[list[UserDeviceExperienceHistory], SensorInsightsListDeviceExperienceHistoryRequestErrorBody]`
- **Error**: `SensorInsightsListDeviceExperienceHistoryRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListDeviceExperienceHistoryRequest` | `verizon/models/dto_list_device_experience_history_request.py` |
| `DtoListDeviceExperienceHistoryRequestDict` | `verizon/models/dto_list_device_experience_history_request.py` |
| `UserDeviceExperienceHistory` | `verizon/models/user_device_experience_history.py` |
| `SensorInsightsListDeviceExperienceHistoryRequestErrorBody` | `verizon/errors/sensor_insights_list_device_experience_history_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_devices.sensor_insights_list_devices_request

- **Route**: `POST /dm/v1/devices/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_devices_request(body: DtoListDevicesRequest | DtoListDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DtoExpandedDeviceResponse]`
- **Returns (raw)**: `ApiResult[list[DtoExpandedDeviceResponse], SensorInsightsListDevicesRequestErrorBody]`
- **Error**: `SensorInsightsListDevicesRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError` [400, 401, 403, 404, 406, 415, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListDevicesRequest` | `verizon/models/dto_list_devices_request.py` |
| `DtoListDevicesRequestDict` | `verizon/models/dto_list_devices_request.py` |
| `DtoExpandedDeviceResponse` | `verizon/models/dto_expanded_device_response.py` |
| `SensorInsightsListDevicesRequestErrorBody` | `verizon/errors/sensor_insights_list_devices_request_error.py` |
| `ManagementError` | `verizon/models/management_error.py` |

### client.sensor_insights_devices.sensor_insights_list_network_experience_history_request

- **Route**: `POST /dm/v1/devices/networkexperience/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_network_experience_history_request(body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[UserNetworkExperienceHistory]`
- **Returns (raw)**: `ApiResult[list[UserNetworkExperienceHistory], SensorInsightsListNetworkExperienceHistoryRequestErrorBody]`
- **Error**: `SensorInsightsListNetworkExperienceHistoryRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListNetworkExperienceHistoryRequest` | `verizon/models/dto_list_network_experience_history_request.py` |
| `DtoListNetworkExperienceHistoryRequestDict` | `verizon/models/dto_list_network_experience_history_request.py` |
| `UserNetworkExperienceHistory` | `verizon/models/user_network_experience_history.py` |
| `SensorInsightsListNetworkExperienceHistoryRequestErrorBody` | `verizon/errors/sensor_insights_list_network_experience_history_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_devices.sensor_insights_patch_device_request

- **Route**: `PATCH /dm/v1/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_patch_device_request(body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ResourceDevice`
- **Returns (raw)**: `ApiResult[ResourceDevice, SensorInsightsPatchDeviceRequestErrorBody]`
- **Error**: `SensorInsightsPatchDeviceRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoPatchDeviceRequest` | `verizon/models/dto_patch_device_request.py` |
| `DtoPatchDeviceRequestDict` | `verizon/models/dto_patch_device_request.py` |
| `ResourceDevice` | `verizon/models/resource_device.py` |
| `SensorInsightsPatchDeviceRequestErrorBody` | `verizon/errors/sensor_insights_patch_device_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

