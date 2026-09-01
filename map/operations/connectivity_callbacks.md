<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConnectivityCallbacks — operations

Accessor: `client.connectivity_callbacks` · Source: `verizon/apis/connectivity_callbacks.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.connectivity_callbacks.deregister_callback

- **Route**: `DELETE /m2m/v1/callbacks/{aname}/name/{sname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def deregister_callback(aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`, `sname`
- **Params**: `aname` — path · `sname` — path
- **Returns (parsed)**: `CallbackActionResult`
- **Returns (raw)**: `ApiResult[CallbackActionResult, DeregisterCallbackErrorBody]`
- **Error**: `DeregisterCallbackErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CallbackActionResult` | `verizon/models/callback_action_result.py` |
| `DeregisterCallbackErrorBody` | `verizon/errors/deregister_callback_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.connectivity_callbacks.list_registered_callbacks

- **Route**: `GET /m2m/v1/callbacks/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_registered_callbacks(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `list[ConnectivityManagementCallback]`
- **Returns (raw)**: `ApiResult[list[ConnectivityManagementCallback], ListRegisteredCallbacksErrorBody]`
- **Error**: `ListRegisteredCallbacksErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConnectivityManagementCallback` | `verizon/models/connectivity_management_callback.py` |
| `ListRegisteredCallbacksErrorBody` | `verizon/errors/list_registered_callbacks_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.connectivity_callbacks.register_callback

- **Route**: `POST /m2m/v1/callbacks/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def register_callback(aname: str, body: RegisterCallbackRequest | RegisterCallbackRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`, `body`
- **Params**: `aname` — path · `body` — JSON body
- **Returns (parsed)**: `CallbackActionResult`
- **Returns (raw)**: `ApiResult[CallbackActionResult, RegisterCallbackErrorBody]`
- **Error**: `RegisterCallbackErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RegisterCallbackRequest` | `verizon/models/register_callback_request.py` |
| `RegisterCallbackRequestDict` | `verizon/models/register_callback_request.py` |
| `CallbackActionResult` | `verizon/models/callback_action_result.py` |
| `RegisterCallbackErrorBody` | `verizon/errors/register_callback_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

