<!-- Generated file — do not edit; regenerated with the SDK. -->

# AnomalyTriggersV2 — operations

Accessor: `client.anomaly_triggers_v2` · Source: `verizon/apis/anomaly_triggers_v2.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.anomaly_triggers_v2.create_anomaly_detection_trigger_v2

- **Route**: `POST /m2m/v2/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def create_anomaly_detection_trigger_v2(body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AnomalyDetectionTrigger`
- **Returns (raw)**: `ApiResult[AnomalyDetectionTrigger, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTriggerRequestOptions` | `verizon/models/unions/create_trigger_request_options.py` |
| `CreateTriggerRequestOptionsDict` | `verizon/models/unions/create_trigger_request_options.py` |
| `AnomalyDetectionTrigger` | `verizon/models/anomaly_detection_trigger.py` |

### client.anomaly_triggers_v2.list_anomaly_detection_trigger_settings_v2

- **Route**: `GET /m2m/v2/triggers/{triggerId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_anomaly_detection_trigger_settings_v2(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trigger_id`
- **Params**: `trigger_id` — path `triggerId`
- **Returns (parsed)**: `AnomalyTriggerResult`
- **Returns (raw)**: `ApiResult[AnomalyTriggerResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AnomalyTriggerResult` | `verizon/models/anomaly_trigger_result.py` |

### client.anomaly_triggers_v2.update_anomaly_detection_trigger_v2

- **Route**: `PUT /m2m/v2/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_anomaly_detection_trigger_v2(body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IntelligenceSuccessResult`
- **Returns (raw)**: `ApiResult[IntelligenceSuccessResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateTriggerRequestOptions` | `verizon/models/unions/update_trigger_request_options.py` |
| `UpdateTriggerRequestOptionsDict` | `verizon/models/unions/update_trigger_request_options.py` |
| `IntelligenceSuccessResult` | `verizon/models/intelligence_success_result.py` |

