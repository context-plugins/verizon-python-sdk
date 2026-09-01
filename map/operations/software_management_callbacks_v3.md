<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementCallbacksV3 — operations

Accessor: `client.software_management_callbacks_v3` · Source: `verizon/apis/software_management_callbacks_v3.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_callbacks_v3.deregister_callback5

- **Route**: `DELETE /callbacks/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def deregister_callback5(acc: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`
- **Params**: `acc` — path
- **Returns (parsed)**: `FotaV3SuccessResult`
- **Returns (raw)**: `ApiResult[FotaV3SuccessResult, DeregisterCallback5ErrorBody]`
- **Error**: `DeregisterCallback5ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV3SuccessResult` | `verizon/models/fota_v3_success_result.py` |
| `DeregisterCallback5ErrorBody` | `verizon/errors/deregister_callback5_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_callbacks_v3.list_registered_callbacks5

- **Route**: `GET /callbacks/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def list_registered_callbacks5(acc: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`
- **Params**: `acc` — path
- **Returns (parsed)**: `FotaV3CallbackSummary`
- **Returns (raw)**: `ApiResult[FotaV3CallbackSummary, ListRegisteredCallbacks5ErrorBody]`
- **Error**: `ListRegisteredCallbacks5ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV3CallbackSummary` | `verizon/models/fota_v3_callback_summary.py` |
| `ListRegisteredCallbacks5ErrorBody` | `verizon/errors/list_registered_callbacks5_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_callbacks_v3.register_callback5

- **Route**: `POST /callbacks/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def register_callback5(acc: str, body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `FotaV3CallbackRegistrationResult`
- **Returns (raw)**: `ApiResult[FotaV3CallbackRegistrationResult, RegisterCallback5ErrorBody]`
- **Error**: `RegisterCallback5ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV3CallbackRegistrationRequest` | `verizon/models/fota_v3_callback_registration_request.py` |
| `FotaV3CallbackRegistrationRequestDict` | `verizon/models/fota_v3_callback_registration_request.py` |
| `FotaV3CallbackRegistrationResult` | `verizon/models/fota_v3_callback_registration_result.py` |
| `RegisterCallback5ErrorBody` | `verizon/errors/register_callback5_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_callbacks_v3.update_callback2

- **Route**: `PUT /callbacks/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def update_callback2(acc: str, body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `FotaV3CallbackRegistrationResult`
- **Returns (raw)**: `ApiResult[FotaV3CallbackRegistrationResult, UpdateCallback2ErrorBody]`
- **Error**: `UpdateCallback2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV3CallbackRegistrationRequest` | `verizon/models/fota_v3_callback_registration_request.py` |
| `FotaV3CallbackRegistrationRequestDict` | `verizon/models/fota_v3_callback_registration_request.py` |
| `FotaV3CallbackRegistrationResult` | `verizon/models/fota_v3_callback_registration_result.py` |
| `UpdateCallback2ErrorBody` | `verizon/errors/update_callback2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

