<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiagnosticsCallbacks — operations

Accessor: `client.diagnostics_callbacks` · Source: `verizon/apis/diagnostics_callbacks.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.diagnostics_callbacks.get_diagnostics_subscription_callback_info

- **Route**: `GET /callbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def get_diagnostics_subscription_callback_info(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — query `accountName`
- **Returns (parsed)**: `list[DeviceDiagnosticsCallback]`
- **Returns (raw)**: `ApiResult[list[DeviceDiagnosticsCallback], GetDiagnosticsSubscriptionCallbackInfoErrorBody]`
- **Error**: `GetDiagnosticsSubscriptionCallbackInfoErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceDiagnosticsResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceDiagnosticsCallback` | `verizon/models/device_diagnostics_callback.py` |
| `GetDiagnosticsSubscriptionCallbackInfoErrorBody` | `verizon/errors/get_diagnostics_subscription_callback_info_error.py` |
| `DeviceDiagnosticsResult` | `verizon/models/device_diagnostics_result.py` |

### client.diagnostics_callbacks.register_diagnostics_callback_url

- **Route**: `POST /callbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def register_diagnostics_callback_url(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DeviceDiagnosticsCallback`
- **Returns (raw)**: `ApiResult[DeviceDiagnosticsCallback, RegisterDiagnosticsCallbackUrlErrorBody]`
- **Error**: `RegisterDiagnosticsCallbackUrlErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceDiagnosticsResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceDiagnosticsCallback` | `verizon/models/device_diagnostics_callback.py` |
| `RegisterDiagnosticsCallbackUrlErrorBody` | `verizon/errors/register_diagnostics_callback_url_error.py` |
| `DeviceDiagnosticsResult` | `verizon/models/device_diagnostics_result.py` |

### client.diagnostics_callbacks.unregister_diagnostics_callback

- **Route**: `DELETE /callbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_diagnostics`
- **Signature**: `def unregister_diagnostics_callback(account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `service_name`
- **Params**: `account_name` — query `accountName` · `service_name` — query `serviceName`
- **Returns (parsed)**: `DeviceDiagnosticsCallback`
- **Returns (raw)**: `ApiResult[DeviceDiagnosticsCallback, UnregisterDiagnosticsCallbackErrorBody]`
- **Error**: `UnregisterDiagnosticsCallbackErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceDiagnosticsResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceDiagnosticsCallback` | `verizon/models/device_diagnostics_callback.py` |
| `UnregisterDiagnosticsCallbackErrorBody` | `verizon/errors/unregister_diagnostics_callback_error.py` |
| `DeviceDiagnosticsResult` | `verizon/models/device_diagnostics_result.py` |

