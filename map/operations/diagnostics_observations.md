<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiagnosticsObservations — operations

Accessor: `client.diagnostics_observations` · Source: `verizon/apis/diagnostics_observations.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.diagnostics_observations.start_diagnostics_observation

- **Route**: `POST /devices/attributes/actions/observe`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def start_diagnostics_observation(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DiagnosticsObservationResult`
- **Returns (raw)**: `ApiResult[DiagnosticsObservationResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DiagnosticsObservationResult` | `verizon/models/diagnostics_observation_result.py` |

### client.diagnostics_observations.stop_diagnostics_observation

- **Route**: `DELETE /devices/attributes/actions/observe`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def stop_diagnostics_observation(transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transaction_id`, `account_name`
- **Params**: `transaction_id` — query `transactionId` · `account_name` — query `accountName`
- **Returns (parsed)**: `DiagnosticsObservationResult`
- **Returns (raw)**: `ApiResult[DiagnosticsObservationResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DiagnosticsObservationResult` | `verizon/models/diagnostics_observation_result.py` |

