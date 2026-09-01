<!-- Generated file — do not edit; regenerated with the SDK. -->

# AnomalyTriggers — operations

Accessor: `client.anomaly_triggers` · Source: `verizon/apis/anomaly_triggers.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.anomaly_triggers.create_anomaly_detection_trigger

- **Route**: `POST /m2m/v1/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def create_anomaly_detection_trigger(body: CreateTriggerRequest | CreateTriggerRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AnomalyDetectionTrigger`
- **Returns (raw)**: `ApiResult[AnomalyDetectionTrigger, CreateAnomalyDetectionTriggerErrorBody]`
- **Error**: `CreateAnomalyDetectionTriggerErrorBody` — **Case A (typed)**
- **Error arms**: `IntelligenceResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateTriggerRequest` | `verizon/models/create_trigger_request.py` |
| `CreateTriggerRequestDict` | `verizon/models/create_trigger_request.py` |
| `AnomalyDetectionTrigger` | `verizon/models/anomaly_detection_trigger.py` |
| `CreateAnomalyDetectionTriggerErrorBody` | `verizon/errors/create_anomaly_detection_trigger_error.py` |
| `IntelligenceResult` | `verizon/models/intelligence_result.py` |

### client.anomaly_triggers.delete_anomaly_detection_trigger

- **Route**: `DELETE /m2m/v1/triggers/{triggerId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def delete_anomaly_detection_trigger(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trigger_id`
- **Params**: `trigger_id` — path `triggerId`
- **Returns (parsed)**: `AnomalyDetectionTrigger`
- **Returns (raw)**: `ApiResult[AnomalyDetectionTrigger, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AnomalyDetectionTrigger` | `verizon/models/anomaly_detection_trigger.py` |

### client.anomaly_triggers.list_anomaly_detection_trigger_settings

- **Route**: `GET /m2m/v1/triggers/{triggerId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_anomaly_detection_trigger_settings(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trigger_id`
- **Params**: `trigger_id` — path `triggerId`
- **Returns (parsed)**: `list[GetTriggerResponseList]`
- **Returns (raw)**: `ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggerSettingsErrorBody]`
- **Error**: `ListAnomalyDetectionTriggerSettingsErrorBody` — **Case A (typed)**
- **Error arms**: `IntelligenceResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTriggerResponseList` | `verizon/models/get_trigger_response_list.py` |
| `ListAnomalyDetectionTriggerSettingsErrorBody` | `verizon/errors/list_anomaly_detection_trigger_settings_error.py` |
| `IntelligenceResult` | `verizon/models/intelligence_result.py` |

### client.anomaly_triggers.list_anomaly_detection_triggers

- **Route**: `GET /m2m/v1/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_anomaly_detection_triggers(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[GetTriggerResponseList]`
- **Returns (raw)**: `ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggersErrorBody]`
- **Error**: `ListAnomalyDetectionTriggersErrorBody` — **Case A (typed)**
- **Error arms**: `IntelligenceResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTriggerResponseList` | `verizon/models/get_trigger_response_list.py` |
| `ListAnomalyDetectionTriggersErrorBody` | `verizon/errors/list_anomaly_detection_triggers_error.py` |
| `IntelligenceResult` | `verizon/models/intelligence_result.py` |

### client.anomaly_triggers.update_anomaly_detection_trigger

- **Route**: `PUT /m2m/v1/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_anomaly_detection_trigger(body: UpdateTriggerRequest | UpdateTriggerRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AnomalyDetectionTrigger`
- **Returns (raw)**: `ApiResult[AnomalyDetectionTrigger, UpdateAnomalyDetectionTriggerErrorBody]`
- **Error**: `UpdateAnomalyDetectionTriggerErrorBody` — **Case A (typed)**
- **Error arms**: `IntelligenceResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateTriggerRequest` | `verizon/models/update_trigger_request.py` |
| `UpdateTriggerRequestDict` | `verizon/models/update_trigger_request.py` |
| `AnomalyDetectionTrigger` | `verizon/models/anomaly_detection_trigger.py` |
| `UpdateAnomalyDetectionTriggerErrorBody` | `verizon/errors/update_anomaly_detection_trigger_error.py` |
| `IntelligenceResult` | `verizon/models/intelligence_result.py` |

