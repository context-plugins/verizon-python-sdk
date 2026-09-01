<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsSmartAlertMetrics — operations

Accessor: `client.sensor_insights_smart_alert_metrics` · Source: `verizon/apis/sensor_insights_smart_alert_metrics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_smart_alert_metrics.sensorinsightsmetricsquery

- **Route**: `POST /dm/v1/smartAlerts/actions/metrics`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensorinsightsmetricsquery(body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoQueryMetricsResponse`
- **Returns (raw)**: `ApiResult[DtoQueryMetricsResponse, SensorinsightsmetricsqueryErrorBody]`
- **Error**: `SensorinsightsmetricsqueryErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoQueryMetrics` | `verizon/models/dto_query_metrics.py` |
| `DtoQueryMetricsDict` | `verizon/models/dto_query_metrics.py` |
| `DtoQueryMetricsResponse` | `verizon/models/dto_query_metrics_response.py` |
| `SensorinsightsmetricsqueryErrorBody` | `verizon/errors/sensorinsightsmetricsquery_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

