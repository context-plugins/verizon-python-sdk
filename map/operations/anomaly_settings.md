<!-- Generated file — do not edit; regenerated with the SDK. -->

# AnomalySettings — operations

Accessor: `client.anomaly_settings` · Source: `verizon/apis/anomaly_settings.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.anomaly_settings.activate_anomaly_detection

- **Route**: `POST /m2m/v1/intelligence/anomaly/settings`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def activate_anomaly_detection(body: AnomalyDetectionRequest | AnomalyDetectionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IntelligenceSuccessResult`
- **Returns (raw)**: `ApiResult[IntelligenceSuccessResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AnomalyDetectionRequest` | `verizon/models/anomaly_detection_request.py` |
| `AnomalyDetectionRequestDict` | `verizon/models/anomaly_detection_request.py` |
| `IntelligenceSuccessResult` | `verizon/models/intelligence_success_result.py` |

### client.anomaly_settings.list_anomaly_detection_settings

- **Route**: `GET /m2m/v1/intelligence/{accountName}/anomaly/settings`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_anomaly_detection_settings(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `AnomalyDetectionSettings`
- **Returns (raw)**: `ApiResult[AnomalyDetectionSettings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AnomalyDetectionSettings` | `verizon/models/anomaly_detection_settings.py` |

### client.anomaly_settings.reset_anomaly_detection_parameters

- **Route**: `PUT /m2m/v1/intelligence/{accountName}/anomaly/settings/reset`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def reset_anomaly_detection_parameters(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `IntelligenceSuccessResult`
- **Returns (raw)**: `ApiResult[IntelligenceSuccessResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IntelligenceSuccessResult` | `verizon/models/intelligence_success_result.py` |

