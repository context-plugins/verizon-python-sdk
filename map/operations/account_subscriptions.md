<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountSubscriptions — operations

Accessor: `client.account_subscriptions` · Source: `verizon/apis/account_subscriptions.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_subscriptions.list_account_subscriptions

- **Route**: `POST /v1/accounts/subscriptions/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `m2_m`
- **Signature**: `def list_account_subscriptions(body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict, *, x_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `x_request_id` — header `X-Request-ID` · `body` — JSON body
- **Returns (parsed)**: `SecuritySubscriptionResult`
- **Returns (raw)**: `ApiResult[SecuritySubscriptionResult, ListAccountSubscriptionsErrorBody]`
- **Error**: `ListAccountSubscriptionsErrorBody` — **Case A (typed)**
- **Error arms**: `SecurityResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SecuritySubscriptionRequest` | `verizon/models/security_subscription_request.py` |
| `SecuritySubscriptionRequestDict` | `verizon/models/security_subscription_request.py` |
| `SecuritySubscriptionResult` | `verizon/models/security_subscription_result.py` |
| `ListAccountSubscriptionsErrorBody` | `verizon/errors/list_account_subscriptions_error.py` |
| `SecurityResult` | `verizon/models/security_result.py` |

