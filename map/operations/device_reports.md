<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceReports — operations

Accessor: `client.device_reports` · Source: `verizon/apis/device_reports.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_reports.calculate_aggregated_report_asynchronous

- **Route**: `POST /report/async/aggregate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def calculate_aggregated_report_asynchronous(body: AggregateSessionReportRequest | AggregateSessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AggregatedReportCallbackResult`
- **Returns (raw)**: `ApiResult[AggregatedReportCallbackResult, CalculateAggregatedReportAsynchronousErrorBody]`
- **Error**: `CalculateAggregatedReportAsynchronousErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AggregateSessionReportRequest` | `verizon/models/aggregate_session_report_request.py` |
| `AggregateSessionReportRequestDict` | `verizon/models/aggregate_session_report_request.py` |
| `AggregatedReportCallbackResult` | `verizon/models/aggregated_report_callback_result.py` |
| `CalculateAggregatedReportAsynchronousErrorBody` | `verizon/errors/calculate_aggregated_report_asynchronous_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

### client.device_reports.calculate_aggregated_report_synchronous

- **Route**: `POST /report/aggregate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def calculate_aggregated_report_synchronous(body: AggregateSessionReportRequest | AggregateSessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AggregateSessionReport`
- **Returns (raw)**: `ApiResult[AggregateSessionReport, CalculateAggregatedReportSynchronousErrorBody]`
- **Error**: `CalculateAggregatedReportSynchronousErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AggregateSessionReportRequest` | `verizon/models/aggregate_session_report_request.py` |
| `AggregateSessionReportRequestDict` | `verizon/models/aggregate_session_report_request.py` |
| `AggregateSessionReport` | `verizon/models/aggregate_session_report.py` |
| `CalculateAggregatedReportSynchronousErrorBody` | `verizon/errors/calculate_aggregated_report_synchronous_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

### client.device_reports.get_sessions_report

- **Route**: `POST /report/sessions`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def get_sessions_report(body: SessionReportRequest | SessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SessionReport`
- **Returns (raw)**: `ApiResult[SessionReport, GetSessionsReportErrorBody]`
- **Error**: `GetSessionsReportErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SessionReportRequest` | `verizon/models/session_report_request.py` |
| `SessionReportRequestDict` | `verizon/models/session_report_request.py` |
| `SessionReport` | `verizon/models/session_report.py` |
| `GetSessionsReportErrorBody` | `verizon/errors/get_sessions_report_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

