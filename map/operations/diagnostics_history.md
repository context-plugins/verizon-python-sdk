<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiagnosticsHistory — operations

Accessor: `client.diagnostics_history` · Source: `verizon/apis/diagnostics_history.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.diagnostics_history.get_diagnostics_history

- **Route**: `POST /history/actions/$search`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def get_diagnostics_history(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[History]`
- **Returns (raw)**: `ApiResult[list[History], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `History` | `verizon/models/history.py` |

