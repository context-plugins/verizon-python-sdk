<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiagnosticsSubscriptions — operations

Accessor: `client.diagnostics_subscriptions` · Source: `verizon/apis/diagnostics_subscriptions.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.diagnostics_subscriptions.get_diagnostics_subscription

- **Route**: `GET /subscriptions`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def get_diagnostics_subscription(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — query `accountName`
- **Returns (parsed)**: `DiagnosticsSubscription`
- **Returns (raw)**: `ApiResult[DiagnosticsSubscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DiagnosticsSubscription` | `verizon/models/diagnostics_subscription.py` |

