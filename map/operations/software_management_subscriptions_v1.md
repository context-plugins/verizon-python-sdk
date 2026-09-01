<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementSubscriptionsV1 — operations

Accessor: `client.software_management_subscriptions_v1` · Source: `verizon/apis/software_management_subscriptions_v1.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_subscriptions_v1.get_account_license_status

- **Route**: `GET /licenses/{account}/index/{startIndex}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def get_account_license_status(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `start_index`
- **Params**: `account` — path · `start_index` — path `startIndex`
- **Returns (parsed)**: `AccountLicenseInfo`
- **Returns (raw)**: `ApiResult[AccountLicenseInfo, GetAccountLicenseStatusErrorBody]`
- **Error**: `GetAccountLicenseStatusErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountLicenseInfo` | `verizon/models/account_license_info.py` |
| `GetAccountLicenseStatusErrorBody` | `verizon/errors/get_account_license_status_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_subscriptions_v1.get_account_subscription_status

- **Route**: `GET /subscriptions/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def get_account_subscription_status(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `V1AccountSubscription`
- **Returns (raw)**: `ApiResult[V1AccountSubscription, GetAccountSubscriptionStatusErrorBody]`
- **Error**: `GetAccountSubscriptionStatusErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1AccountSubscription` | `verizon/models/v1_account_subscription.py` |
| `GetAccountSubscriptionStatusErrorBody` | `verizon/errors/get_account_subscription_status_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

