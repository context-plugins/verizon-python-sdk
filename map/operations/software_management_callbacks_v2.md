<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementCallbacksV2 — operations

Accessor: `client.software_management_callbacks_v2` · Source: `verizon/apis/software_management_callbacks_v2.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_callbacks_v2.deregister_callback4

- **Route**: `DELETE /callbacks/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def deregister_callback4(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `FotaV2SuccessResult`
- **Returns (raw)**: `ApiResult[FotaV2SuccessResult, DeregisterCallback4ErrorBody]`
- **Error**: `DeregisterCallback4ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV2SuccessResult` | `verizon/models/fota_v2_success_result.py` |
| `DeregisterCallback4ErrorBody` | `verizon/errors/deregister_callback4_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_callbacks_v2.list_registered_callbacks4

- **Route**: `GET /callbacks/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def list_registered_callbacks4(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `CallbackSummary`
- **Returns (raw)**: `ApiResult[CallbackSummary, ListRegisteredCallbacks4ErrorBody]`
- **Error**: `ListRegisteredCallbacks4ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CallbackSummary` | `verizon/models/callback_summary.py` |
| `ListRegisteredCallbacks4ErrorBody` | `verizon/errors/list_registered_callbacks4_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_callbacks_v2.register_callback4

- **Route**: `POST /callbacks/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def register_callback4(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `FotaV2CallbackRegistrationResult`
- **Returns (raw)**: `ApiResult[FotaV2CallbackRegistrationResult, RegisterCallback4ErrorBody]`
- **Error**: `RegisterCallback4ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV2CallbackRegistrationResult` | `verizon/models/fota_v2_callback_registration_result.py` |
| `RegisterCallback4ErrorBody` | `verizon/errors/register_callback4_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_callbacks_v2.update_callback

- **Route**: `PUT /callbacks/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def update_callback(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `FotaV2CallbackRegistrationResult`
- **Returns (raw)**: `ApiResult[FotaV2CallbackRegistrationResult, UpdateCallbackErrorBody]`
- **Error**: `UpdateCallbackErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV2CallbackRegistrationResult` | `verizon/models/fota_v2_callback_registration_result.py` |
| `UpdateCallbackErrorBody` | `verizon/errors/update_callback_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

