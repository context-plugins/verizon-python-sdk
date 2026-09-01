<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceProfileManagement — operations

Accessor: `client.device_profile_management` · Source: `verizon/apis/device_profile_management.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_profile_management.activate_device_through_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/activate_enable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def activate_device_through_profile(body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, ActivateDeviceThroughProfileErrorBody]`
- **Error**: `ActivateDeviceThroughProfileErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ActivateDeviceProfileRequest` | `verizon/models/activate_device_profile_request.py` |
| `ActivateDeviceProfileRequestDict` | `verizon/models/activate_device_profile_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `ActivateDeviceThroughProfileErrorBody` | `verizon/errors/activate_device_through_profile_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.device_profile_management.profile_to_activate_device

- **Route**: `POST /m2m/v1/devices/profile/actions/activate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def profile_to_activate_device(body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, ProfileToActivateDeviceErrorBody]`
- **Error**: `ProfileToActivateDeviceErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileRequest` | `verizon/models/profile_request.py` |
| `ProfileRequestDict` | `verizon/models/profile_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `ProfileToActivateDeviceErrorBody` | `verizon/errors/profile_to_activate_device_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.device_profile_management.profile_to_deactivate_device

- **Route**: `POST /m2m/v1/devices/profile/actions/deactivate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def profile_to_deactivate_device(body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, ProfileToDeactivateDeviceErrorBody]`
- **Error**: `ProfileToDeactivateDeviceErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeactivateDeviceProfileRequest` | `verizon/models/deactivate_device_profile_request.py` |
| `DeactivateDeviceProfileRequestDict` | `verizon/models/deactivate_device_profile_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `ProfileToDeactivateDeviceErrorBody` | `verizon/errors/profile_to_deactivate_device_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.device_profile_management.profile_to_set_fallback_attribute

- **Route**: `POST /m2m/v1/devices/profile/actions/setfallbackattribute`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def profile_to_set_fallback_attribute(body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, ProfileToSetFallbackAttributeErrorBody]`
- **Error**: `ProfileToSetFallbackAttributeErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetFallbackAttributeRequest` | `verizon/models/set_fallback_attribute_request.py` |
| `SetFallbackAttributeRequestDict` | `verizon/models/set_fallback_attribute_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `ProfileToSetFallbackAttributeErrorBody` | `verizon/errors/profile_to_set_fallback_attribute_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

