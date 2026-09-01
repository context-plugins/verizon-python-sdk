<!-- Generated file — do not edit; regenerated with the SDK. -->

# EUiccDeviceProfileManagement — operations

Accessor: `client.e_uicc_device_profile_management` · Source: `verizon/apis/e_uicc_device_profile_management.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.e_uicc_device_profile_management.delete_local_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/delete`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def delete_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, DeleteLocalProfileErrorBody]`
- **Error**: `DeleteLocalProfileErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileChangeStateRequest` | `verizon/models/profile_change_state_request.py` |
| `ProfileChangeStateRequestDict` | `verizon/models/profile_change_state_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `DeleteLocalProfileErrorBody` | `verizon/errors/delete_local_profile_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.e_uicc_device_profile_management.disable_local_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/disable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def disable_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, DisableLocalProfileErrorBody]`
- **Error**: `DisableLocalProfileErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileChangeStateRequest` | `verizon/models/profile_change_state_request.py` |
| `ProfileChangeStateRequestDict` | `verizon/models/profile_change_state_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `DisableLocalProfileErrorBody` | `verizon/errors/disable_local_profile_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.e_uicc_device_profile_management.download_local_profile_to_disable

- **Route**: `POST /m2m/v1/devices/profile/actions/download_disable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def download_local_profile_to_disable(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, DownloadLocalProfileToDisableErrorBody]`
- **Error**: `DownloadLocalProfileToDisableErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileChangeStateRequest` | `verizon/models/profile_change_state_request.py` |
| `ProfileChangeStateRequestDict` | `verizon/models/profile_change_state_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `DownloadLocalProfileToDisableErrorBody` | `verizon/errors/download_local_profile_to_disable_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.e_uicc_device_profile_management.download_local_profile_to_enable

- **Route**: `POST /m2m/v1/devices/profile/actions/download_enable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def download_local_profile_to_enable(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, DownloadLocalProfileToEnableErrorBody]`
- **Error**: `DownloadLocalProfileToEnableErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileChangeStateRequest` | `verizon/models/profile_change_state_request.py` |
| `ProfileChangeStateRequestDict` | `verizon/models/profile_change_state_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `DownloadLocalProfileToEnableErrorBody` | `verizon/errors/download_local_profile_to_enable_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.e_uicc_device_profile_management.enable_local_profile

- **Route**: `POST /m2m/v1/devices/profile/actions/enable`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def enable_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, EnableLocalProfileErrorBody]`
- **Error**: `EnableLocalProfileErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileChangeStateRequest` | `verizon/models/profile_change_state_request.py` |
| `ProfileChangeStateRequestDict` | `verizon/models/profile_change_state_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `EnableLocalProfileErrorBody` | `verizon/errors/enable_local_profile_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

