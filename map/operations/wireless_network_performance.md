<!-- Generated file — do not edit; regenerated with the SDK. -->

# WirelessNetworkPerformance — operations

Accessor: `client.wireless_network_performance` · Source: `verizon/apis/wireless_network_performance.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wireless_network_performance.device_experience30days_history

- **Route**: `POST /m2m/v1/intelligence/device-experience/history/30-days`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_experience30days_history(body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WnprequestResponse`
- **Returns (raw)**: `ApiResult[WnprequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetDeviceExperienceScoreHistoryRequest` | `verizon/models/get_device_experience_score_history_request.py` |
| `GetDeviceExperienceScoreHistoryRequestDict` | `verizon/models/get_device_experience_score_history_request.py` |
| `WnprequestResponse` | `verizon/models/wnprequest_response.py` |

### client.wireless_network_performance.device_experience_bulk_latest

- **Route**: `POST /m2m/v1/intelligence/device-experience/bulk/latest`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_experience_bulk_latest(body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WnprequestResponse`
- **Returns (raw)**: `ApiResult[WnprequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetDeviceExperienceScoreBulkRequest` | `verizon/models/get_device_experience_score_bulk_request.py` |
| `GetDeviceExperienceScoreBulkRequestDict` | `verizon/models/get_device_experience_score_bulk_request.py` |
| `WnprequestResponse` | `verizon/models/wnprequest_response.py` |

### client.wireless_network_performance.domestic4_g_and5_g_nationwide_network_coverage

- **Route**: `POST /m2m/v1/intelligence/wireless-coverage`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def domestic4_g_and5_g_nationwide_network_coverage(body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WnprequestResponse`
- **Returns (raw)**: `ApiResult[WnprequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `M2MV1IntelligenceWirelessCoverageRequest` | `verizon/models/unions/m2_mv1_intelligence_wireless_coverage_request.py` |
| `M2MV1IntelligenceWirelessCoverageRequestDict` | `verizon/models/unions/m2_mv1_intelligence_wireless_coverage_request.py` |
| `WnprequestResponse` | `verizon/models/wnprequest_response.py` |

### client.wireless_network_performance.near_real_time_network_conditions

- **Route**: `POST /m2m/v1/intelligence/network-conditions`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def near_real_time_network_conditions(body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WnprequestResponse`
- **Returns (raw)**: `ApiResult[WnprequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetNetworkConditionsRequest` | `verizon/models/get_network_conditions_request.py` |
| `GetNetworkConditionsRequestDict` | `verizon/models/get_network_conditions_request.py` |
| `WnprequestResponse` | `verizon/models/wnprequest_response.py` |

### client.wireless_network_performance.site_proximity

- **Route**: `POST /m2m/v1/intelligence/site-proximity/action/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def site_proximity(body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WnprequestResponse`
- **Returns (raw)**: `ApiResult[WnprequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetNetworkConditionsRequest` | `verizon/models/get_network_conditions_request.py` |
| `GetNetworkConditionsRequestDict` | `verizon/models/get_network_conditions_request.py` |
| `WnprequestResponse` | `verizon/models/wnprequest_response.py` |

