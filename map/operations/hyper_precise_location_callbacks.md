<!-- Generated file — do not edit; regenerated with the SDK. -->

# HyperPreciseLocationCallbacks — operations

Accessor: `client.hyper_precise_location_callbacks` · Source: `verizon/apis/hyper_precise_location_callbacks.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.hyper_precise_location_callbacks.deregister_callback6

- **Route**: `DELETE /callbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def deregister_callback6(account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_number`, `service`
- **Params**: `account_number` — query `accountNumber` · `service` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeregisterCallback6ErrorBody]`
- **Error**: `DeregisterCallback6ErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeregisterCallback6ErrorBody` | `verizon/errors/deregister_callback6_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

### client.hyper_precise_location_callbacks.list_registered_callbacks6

- **Route**: `GET /callbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def list_registered_callbacks6(account_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_number`
- **Params**: `account_number` — query `accountNumber`
- **Returns (parsed)**: `list[CallbackCreated]`
- **Returns (raw)**: `ApiResult[list[CallbackCreated], ListRegisteredCallbacks6ErrorBody]`
- **Error**: `ListRegisteredCallbacks6ErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CallbackCreated` | `verizon/models/callback_created.py` |
| `ListRegisteredCallbacks6ErrorBody` | `verizon/errors/list_registered_callbacks6_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

### client.hyper_precise_location_callbacks.register_callback6

- **Route**: `POST /callbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def register_callback6(account_number: str, body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_number`, `body`
- **Params**: `account_number` — query `accountNumber` · `body` — JSON body
- **Returns (parsed)**: `CallbackRegistered`
- **Returns (raw)**: `ApiResult[CallbackRegistered, RegisterCallback6ErrorBody]`
- **Error**: `RegisterCallback6ErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `HyperPreciseLocationCallback` | `verizon/models/hyper_precise_location_callback.py` |
| `HyperPreciseLocationCallbackDict` | `verizon/models/hyper_precise_location_callback.py` |
| `CallbackRegistered` | `verizon/models/callback_registered.py` |
| `RegisterCallback6ErrorBody` | `verizon/errors/register_callback6_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

