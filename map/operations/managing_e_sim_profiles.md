<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManagingESimProfiles — operations

Accessor: `client.managing_e_sim_profiles` · Source: `verizon/apis/managing_e_sim_profiles.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.managing_e_sim_profiles.activate_a_device_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/activate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def activate_a_device_profile(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GioprofileRequest` | `verizon/models/gioprofile_request.py` |
| `GioprofileRequestDict` | `verizon/models/gioprofile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.deactivate_a_device_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/deactivate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def deactivate_a_device_profile(body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GiodeactivateDeviceProfileRequest` | `verizon/models/giodeactivate_device_profile_request.py` |
| `GiodeactivateDeviceProfileRequestDict` | `verizon/models/giodeactivate_device_profile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.delete_a_device_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/delete`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def delete_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeviceProfileRequest` | `verizon/models/device_profile_request.py` |
| `DeviceProfileRequestDict` | `verizon/models/device_profile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.device_suspend

- **Route**: `POST /m2m/v1/devices/profile/actions/device_suspend`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_suspend(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GioprofileRequest` | `verizon/models/gioprofile_request.py` |
| `GioprofileRequestDict` | `verizon/models/gioprofile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.download_a_device_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/download`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def download_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeviceProfileRequest` | `verizon/models/device_profile_request.py` |
| `DeviceProfileRequestDict` | `verizon/models/device_profile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.enable_a_device_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/enable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def enable_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeviceProfileRequest` | `verizon/models/device_profile_request.py` |
| `DeviceProfileRequestDict` | `verizon/models/device_profile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.enable_a_device_profile_for_download

- **Route**: `POST /m2m/v1/devices/profile/actions/download_enable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def enable_a_device_profile_for_download(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeviceProfileRequest` | `verizon/models/device_profile_request.py` |
| `DeviceProfileRequestDict` | `verizon/models/device_profile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.profile_suspend

- **Route**: `POST /m2m/v1/devices/profile/actions/profile_suspend`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def profile_suspend(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GioprofileRequest` | `verizon/models/gioprofile_request.py` |
| `GioprofileRequestDict` | `verizon/models/gioprofile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.resume_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/profile_resume`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def resume_profile(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GioprofileRequest` | `verizon/models/gioprofile_request.py` |
| `GioprofileRequestDict` | `verizon/models/gioprofile_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.managing_e_sim_profiles.set_fallback

- **Route**: `POST /v1/devices/profile/actions/setfallbackattribute`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def set_fallback(body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FallBack` | `verizon/models/fall_back.py` |
| `FallBackDict` | `verizon/models/fall_back.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

