<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsSmartAlerts — operations

Accessor: `client.sensor_insights_smart_alerts` · Source: `verizon/apis/sensor_insights_smart_alerts.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_smart_alerts.sensor_insights_bulk_update

- **Route**: `POST /dm/v1/smartAlerts/actions/bulkupdate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_bulk_update(body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserSmartAlert`
- **Returns (raw)**: `ApiResult[UserSmartAlert, SensorInsightsBulkUpdateErrorBody]`
- **Error**: `SensorInsightsBulkUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoBulkUpdate` | `verizon/models/dto_bulk_update.py` |
| `DtoBulkUpdateDict` | `verizon/models/dto_bulk_update.py` |
| `UserSmartAlert` | `verizon/models/user_smart_alert.py` |
| `SensorInsightsBulkUpdateErrorBody` | `verizon/errors/sensor_insights_bulk_update_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_smart_alerts.sensor_insights_list_smart_alerts_request

- **Route**: `POST /dm/v1/smartAlerts/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_smart_alerts_request(body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[UserSmartAlert]`
- **Returns (raw)**: `ApiResult[list[UserSmartAlert], SensorInsightsListSmartAlertsRequestErrorBody]`
- **Error**: `SensorInsightsListSmartAlertsRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListSmartAlertsRequest` | `verizon/models/dto_list_smart_alerts_request.py` |
| `DtoListSmartAlertsRequestDict` | `verizon/models/dto_list_smart_alerts_request.py` |
| `UserSmartAlert` | `verizon/models/user_smart_alert.py` |
| `SensorInsightsListSmartAlertsRequestErrorBody` | `verizon/errors/sensor_insights_list_smart_alerts_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_smart_alerts.sensor_insights_patch_smart_alert_request

- **Route**: `PATCH /dm/v1/smartAlerts`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_patch_smart_alert_request(body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UserSmartAlert`
- **Returns (raw)**: `ApiResult[UserSmartAlert, SensorInsightsPatchSmartAlertRequestErrorBody]`
- **Error**: `SensorInsightsPatchSmartAlertRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoPatchSmartAlertRequest` | `verizon/models/dto_patch_smart_alert_request.py` |
| `DtoPatchSmartAlertRequestDict` | `verizon/models/dto_patch_smart_alert_request.py` |
| `UserSmartAlert` | `verizon/models/user_smart_alert.py` |
| `SensorInsightsPatchSmartAlertRequestErrorBody` | `verizon/errors/sensor_insights_patch_smart_alert_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

