<!-- Generated file — do not edit; regenerated with the SDK. -->

# PromotionPeriodInformation — operations

Accessor: `client.promotion_period_information` · Source: `verizon/apis/promotion_period_information.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.promotion_period_information.get_promo_device_aggregate_usage_history

- **Route**: `POST /m2m/v1/devices/usage/actions/promoaggregateusage`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_promo_device_aggregate_usage_history(body: RequestBodyForUsage | RequestBodyForUsageDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UsageRequestResponse`
- **Returns (raw)**: `ApiResult[UsageRequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RequestBodyForUsage` | `verizon/models/request_body_for_usage.py` |
| `RequestBodyForUsageDict` | `verizon/models/request_body_for_usage.py` |
| `UsageRequestResponse` | `verizon/models/usage_request_response.py` |

### client.promotion_period_information.get_promo_device_usage_history

- **Route**: `POST /m2m/v1/devices/usage/actions/promodeviceusage`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_promo_device_usage_history(body: ARequestBodyForUsage | ARequestBodyForUsageDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ResponseToUsageQuery`
- **Returns (raw)**: `ApiResult[ResponseToUsageQuery, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ARequestBodyForUsage` | `verizon/models/a_request_body_for_usage.py` |
| `ARequestBodyForUsageDict` | `verizon/models/a_request_body_for_usage.py` |
| `ResponseToUsageQuery` | `verizon/models/response_to_usage_query.py` |

