<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceGroups — operations

Accessor: `client.device_groups` · Source: `verizon/apis/device_groups.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_groups.create_device_group

- **Route**: `POST /m2m/v1/groups`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def create_device_group(body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ConnectivityManagementSuccessResult`
- **Returns (raw)**: `ApiResult[ConnectivityManagementSuccessResult, CreateDeviceGroupErrorBody]`
- **Error**: `CreateDeviceGroupErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateDeviceGroupRequest` | `verizon/models/create_device_group_request.py` |
| `CreateDeviceGroupRequestDict` | `verizon/models/create_device_group_request.py` |
| `ConnectivityManagementSuccessResult` | `verizon/models/connectivity_management_success_result.py` |
| `CreateDeviceGroupErrorBody` | `verizon/errors/create_device_group_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_groups.delete_device_group

- **Route**: `DELETE /m2m/v1/groups/{aname}/name/{gname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def delete_device_group(aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`, `gname`
- **Params**: `aname` — path · `gname` — path
- **Returns (parsed)**: `ConnectivityManagementSuccessResult`
- **Returns (raw)**: `ApiResult[ConnectivityManagementSuccessResult, DeleteDeviceGroupErrorBody]`
- **Error**: `DeleteDeviceGroupErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConnectivityManagementSuccessResult` | `verizon/models/connectivity_management_success_result.py` |
| `DeleteDeviceGroupErrorBody` | `verizon/errors/delete_device_group_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_groups.get_device_group_information

- **Route**: `GET /m2m/v1/groups/{aname}/name/{gname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_device_group_information(aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`, `gname`
- **Params**: `aname` — path · `gname` — path · `next` — query
- **Returns (parsed)**: `DeviceGroupDevicesData`
- **Returns (raw)**: `ApiResult[DeviceGroupDevicesData, GetDeviceGroupInformationErrorBody]`
- **Error**: `GetDeviceGroupInformationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceGroupDevicesData` | `verizon/models/device_group_devices_data.py` |
| `GetDeviceGroupInformationErrorBody` | `verizon/errors/get_device_group_information_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_groups.list_device_groups

- **Route**: `GET /m2m/v1/groups/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_device_groups(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `list[DeviceGroup]`
- **Returns (raw)**: `ApiResult[list[DeviceGroup], ListDeviceGroupsErrorBody]`
- **Error**: `ListDeviceGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceGroup` | `verizon/models/device_group.py` |
| `ListDeviceGroupsErrorBody` | `verizon/errors/list_device_groups_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_groups.update_device_group

- **Route**: `PUT /m2m/v1/groups/{aname}/name/{gname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_device_group(aname: str, gname: str, body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`, `gname`, `body`
- **Params**: `aname` — path · `gname` — path · `body` — JSON body
- **Returns (parsed)**: `ConnectivityManagementSuccessResult`
- **Returns (raw)**: `ApiResult[ConnectivityManagementSuccessResult, UpdateDeviceGroupErrorBody]`
- **Error**: `UpdateDeviceGroupErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceGroupUpdateRequest` | `verizon/models/device_group_update_request.py` |
| `DeviceGroupUpdateRequestDict` | `verizon/models/device_group_update_request.py` |
| `ConnectivityManagementSuccessResult` | `verizon/models/connectivity_management_success_result.py` |
| `UpdateDeviceGroupErrorBody` | `verizon/errors/update_device_group_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

