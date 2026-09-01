<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceMonitoring — operations

Accessor: `client.device_monitoring` · Source: `verizon/apis/device_monitoring.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_monitoring.device_reachability

- **Route**: `POST /m2m/v1/diagnostics/basic/devicereachability`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_reachability(body: NotificationReportRequest | NotificationReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, DeviceReachabilityErrorBody]`
- **Error**: `DeviceReachabilityErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `NotificationReportRequest` | `verizon/models/notification_report_request.py` |
| `NotificationReportRequestDict` | `verizon/models/notification_report_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `DeviceReachabilityErrorBody` | `verizon/errors/device_reachability_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.device_monitoring.stop_device_reachability

- **Route**: `DELETE /m2m/v1/diagnostics/basic/devicereachability`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def stop_device_reachability(stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `stopreachabilitypayload`
- **Params**: `stopreachabilitypayload` — query
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, StopDeviceReachabilityErrorBody]`
- **Error**: `StopDeviceReachabilityErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `StopMonitorRequest` | `verizon/models/stop_monitor_request.py` |
| `StopMonitorRequestDict` | `verizon/models/stop_monitor_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `StopDeviceReachabilityErrorBody` | `verizon/errors/stop_device_reachability_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

