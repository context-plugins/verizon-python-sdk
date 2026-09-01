<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiagnosticsFactoryReset — operations

Accessor: `client.diagnostics_factory_reset` · Source: `verizon/apis/diagnostics_factory_reset.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.diagnostics_factory_reset.decives_restart

- **Route**: `POST /devices/actions/restart`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def decives_restart(body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DiagnosticsObservationResult`
- **Returns (raw)**: `ApiResult[DiagnosticsObservationResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeviceResetRequest` | `verizon/models/device_reset_request.py` |
| `DeviceResetRequestDict` | `verizon/models/device_reset_request.py` |
| `DiagnosticsObservationResult` | `verizon/models/diagnostics_observation_result.py` |

