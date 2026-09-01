<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementSubscriptionsV3 — operations

Accessor: `client.software_management_subscriptions_v3` · Source: `verizon/apis/software_management_subscriptions_v3.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_subscriptions_v3.get_account_subscription_status3

- **Route**: `GET /subscriptions/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_account_subscription_status3(acc: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`
- **Params**: `acc` — path
- **Returns (parsed)**: `FotaV3Subscription`
- **Returns (raw)**: `ApiResult[FotaV3Subscription, GetAccountSubscriptionStatus3ErrorBody]`
- **Error**: `GetAccountSubscriptionStatus3ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV3Subscription` | `verizon/models/fota_v3_subscription.py` |
| `GetAccountSubscriptionStatus3ErrorBody` | `verizon/errors/get_account_subscription_status3_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

