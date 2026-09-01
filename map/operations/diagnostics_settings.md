<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiagnosticsSettings — operations

Accessor: `client.diagnostics_settings` · Source: `verizon/apis/diagnostics_settings.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.diagnostics_settings.list_diagnostics_settings

- **Route**: `GET /devices/settings`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def list_diagnostics_settings(account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `devices`
- **Params**: `account_name` — query `accountName` · `devices` — query
- **Returns (parsed)**: `list[DiagnosticObservationSetting]`
- **Returns (raw)**: `ApiResult[list[DiagnosticObservationSetting], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DiagnosticObservationSetting` | `verizon/models/diagnostic_observation_setting.py` |

