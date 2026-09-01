<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceDiagnostics — operations

Accessor: `client.device_diagnostics` · Source: `verizon/apis/device_diagnostics.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_diagnostics.device_reachability_status_using_post

- **Route**: `POST /m2m/v1/diagnostics/basic/devicereachability/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_reachability_status_using_post(body: NotificationReportStatusRequest | NotificationReportStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, DeviceReachabilityStatusUsingPostErrorBody]`
- **Error**: `DeviceReachabilityStatusUsingPostErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NotificationReportStatusRequest` | `verizon/models/notification_report_status_request.py` |
| `NotificationReportStatusRequestDict` | `verizon/models/notification_report_status_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `DeviceReachabilityStatusUsingPostErrorBody` | `verizon/errors/device_reachability_status_using_post_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_diagnostics.retrieve_active_monitors_using_post

- **Route**: `POST /m2m/v1/diagnostics/basic/devicereachability/monitors`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_active_monitors_using_post(body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, RetrieveActiveMonitorsUsingPostErrorBody]`
- **Error**: `RetrieveActiveMonitorsUsingPostErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RetrieveMonitorsRequest` | `verizon/models/retrieve_monitors_request.py` |
| `RetrieveMonitorsRequestDict` | `verizon/models/retrieve_monitors_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `RetrieveActiveMonitorsUsingPostErrorBody` | `verizon/errors/retrieve_active_monitors_using_post_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

