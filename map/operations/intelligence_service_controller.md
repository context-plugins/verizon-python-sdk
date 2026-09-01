<!-- Generated file — do not edit; regenerated with the SDK. -->

# IntelligenceServiceController — operations

Accessor: `client.intelligence_service_controller` · Source: `verizon/apis/intelligence_service_controller.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.intelligence_service_controller.set_connection_planner

- **Route**: `POST /v1/intelligence/device/connection-planner`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def set_connection_planner(*, body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AsynchronousRequestResultforplanner`
- **Returns (raw)**: `ApiResult[AsynchronousRequestResultforplanner, SetConnectionPlannerErrorBody]`
- **Error**: `SetConnectionPlannerErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponseforplanner` [400, 403, 404, 406, 429] · `AuthRestErrorResponseforplanner` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetDevicesWindowsRequestforplanner` | `verizon/models/get_devices_windows_requestforplanner.py` |
| `GetDevicesWindowsRequestforplannerDict` | `verizon/models/get_devices_windows_requestforplanner.py` |
| `AsynchronousRequestResultforplanner` | `verizon/models/asynchronous_request_resultforplanner.py` |
| `SetConnectionPlannerErrorBody` | `verizon/errors/set_connection_planner_error.py` |
| `RestErrorResponseforplanner` | `verizon/models/rest_error_responseforplanner.py` |
| `AuthRestErrorResponseforplanner` | `verizon/models/auth_rest_error_responseforplanner.py` |

### client.intelligence_service_controller.status_connection_planner

- **Route**: `POST /v1/intelligence/device/connection-planner/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def status_connection_planner(*, body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetDeviceStatusesResponseforplanner`
- **Returns (raw)**: `ApiResult[GetDeviceStatusesResponseforplanner, StatusConnectionPlannerErrorBody]`
- **Error**: `StatusConnectionPlannerErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponseforplanner` [400, 403, 404, 406, 429] · `AuthRestErrorResponseforplanner` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetDeviceStatusesRequestforplanner` | `verizon/models/get_device_statuses_requestforplanner.py` |
| `GetDeviceStatusesRequestforplannerDict` | `verizon/models/get_device_statuses_requestforplanner.py` |
| `GetDeviceStatusesResponseforplanner` | `verizon/models/get_device_statuses_responseforplanner.py` |
| `StatusConnectionPlannerErrorBody` | `verizon/errors/status_connection_planner_error.py` |
| `RestErrorResponseforplanner` | `verizon/models/rest_error_responseforplanner.py` |
| `AuthRestErrorResponseforplanner` | `verizon/models/auth_rest_error_responseforplanner.py` |

