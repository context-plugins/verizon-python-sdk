<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementCallbacksV1 — operations

Accessor: `client.software_management_callbacks_v1` · Source: `verizon/apis/software_management_callbacks_v1.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_callbacks_v1.deregister_callback3

- **Route**: `DELETE /callbacks/{account}/name/{service}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def deregister_callback3(account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `service`
- **Params**: `account` — path · `service` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeregisterCallback3ErrorBody]`
- **Error**: `DeregisterCallback3ErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `CallbackServiceOrStr` | `verizon/models/enums/callback_service.py` |
| `DeregisterCallback3ErrorBody` | `verizon/errors/deregister_callback3_error.py` |

### client.software_management_callbacks_v1.list_registered_callbacks3

- **Route**: `GET /callbacks/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def list_registered_callbacks3(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `list[RegisteredCallbacks]`
- **Returns (raw)**: `ApiResult[list[RegisteredCallbacks], ListRegisteredCallbacks3ErrorBody]`
- **Error**: `ListRegisteredCallbacks3ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RegisteredCallbacks` | `verizon/models/registered_callbacks.py` |
| `ListRegisteredCallbacks3ErrorBody` | `verizon/errors/list_registered_callbacks3_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_callbacks_v1.register_callback3

- **Route**: `POST /callbacks/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def register_callback3(account: str, body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `body`
- **Params**: `account` — path · `body` — JSON body
- **Returns (parsed)**: `FotaV1CallbackRegistrationResult`
- **Returns (raw)**: `ApiResult[FotaV1CallbackRegistrationResult, RegisterCallback3ErrorBody]`
- **Error**: `RegisterCallback3ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV1CallbackRegistrationRequest` | `verizon/models/fota_v1_callback_registration_request.py` |
| `FotaV1CallbackRegistrationRequestDict` | `verizon/models/fota_v1_callback_registration_request.py` |
| `FotaV1CallbackRegistrationResult` | `verizon/models/fota_v1_callback_registration_result.py` |
| `RegisterCallback3ErrorBody` | `verizon/errors/register_callback3_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

