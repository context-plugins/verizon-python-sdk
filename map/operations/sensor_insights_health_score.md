<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsHealthScore — operations

Accessor: `client.sensor_insights_health_score` · Source: `verizon/apis/sensor_insights_health_score.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_health_score.sensor_insights_get_network_health_score_response

- **Route**: `POST /dm/v1/healthscore/network`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_get_network_health_score_response(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DtoGetNetworkHealthScoreResponse`
- **Returns (raw)**: `ApiResult[DtoGetNetworkHealthScoreResponse, SensorInsightsGetNetworkHealthScoreResponseErrorBody]`
- **Error**: `SensorInsightsGetNetworkHealthScoreResponseErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoGetNetworkHealthScoreResponse` | `verizon/models/dto_get_network_health_score_response.py` |
| `SensorInsightsGetNetworkHealthScoreResponseErrorBody` | `verizon/errors/sensor_insights_get_network_health_score_response_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_health_score.sensor_insights_health_score_summary

- **Route**: `POST /dm/v1/healthscore/summary`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_health_score_summary(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DtoHealthScoreSummary`
- **Returns (raw)**: `ApiResult[DtoHealthScoreSummary, SensorInsightsHealthScoreSummaryErrorBody]`
- **Error**: `SensorInsightsHealthScoreSummaryErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoHealthScoreSummary` | `verizon/models/dto_health_score_summary.py` |
| `SensorInsightsHealthScoreSummaryErrorBody` | `verizon/errors/sensor_insights_health_score_summary_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

