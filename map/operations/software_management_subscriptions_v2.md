<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementSubscriptionsV2 — operations

Accessor: `client.software_management_subscriptions_v2` · Source: `verizon/apis/software_management_subscriptions_v2.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_subscriptions_v2.get_account_subscription_status2

- **Route**: `GET /subscriptions/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_account_subscription_status2(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `FotaV2Subscription`
- **Returns (raw)**: `ApiResult[FotaV2Subscription, GetAccountSubscriptionStatus2ErrorBody]`
- **Error**: `GetAccountSubscriptionStatus2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV2Subscription` | `verizon/models/fota_v2_subscription.py` |
| `GetAccountSubscriptionStatus2ErrorBody` | `verizon/errors/get_account_subscription_status2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

