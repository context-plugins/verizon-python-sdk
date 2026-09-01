<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementLicensesV1 — operations

Accessor: `client.software_management_licenses_v1` · Source: `verizon/apis/software_management_licenses_v1.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_licenses_v1.assign_licenses_to_devices

- **Route**: `POST /licenses/{account}/assign`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def assign_licenses_to_devices(account: str, body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `body`
- **Params**: `account` — path · `body` — JSON body
- **Returns (parsed)**: `V1LicensesAssignedRemovedResult`
- **Returns (raw)**: `ApiResult[V1LicensesAssignedRemovedResult, AssignLicensesToDevicesErrorBody]`
- **Error**: `AssignLicensesToDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1LicensesAssignedRemovedRequest` | `verizon/models/v1_licenses_assigned_removed_request.py` |
| `V1LicensesAssignedRemovedRequestDict` | `verizon/models/v1_licenses_assigned_removed_request.py` |
| `V1LicensesAssignedRemovedResult` | `verizon/models/v1_licenses_assigned_removed_result.py` |
| `AssignLicensesToDevicesErrorBody` | `verizon/errors/assign_licenses_to_devices_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_licenses_v1.create_list_of_licenses_to_remove

- **Route**: `POST /licenses/{account}/cancel`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def create_list_of_licenses_to_remove(account: str, body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `body`
- **Params**: `account` — path · `body` — JSON body
- **Returns (parsed)**: `V1ListOfLicensesToRemoveResult`
- **Returns (raw)**: `ApiResult[V1ListOfLicensesToRemoveResult, CreateListOfLicensesToRemoveErrorBody]`
- **Error**: `CreateListOfLicensesToRemoveErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ListOfLicensesToRemoveRequest` | `verizon/models/v1_list_of_licenses_to_remove_request.py` |
| `V1ListOfLicensesToRemoveRequestDict` | `verizon/models/v1_list_of_licenses_to_remove_request.py` |
| `V1ListOfLicensesToRemoveResult` | `verizon/models/v1_list_of_licenses_to_remove_result.py` |
| `CreateListOfLicensesToRemoveErrorBody` | `verizon/errors/create_list_of_licenses_to_remove_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_licenses_v1.delete_list_of_licenses_to_remove

- **Route**: `DELETE /licenses/{account}/cancel`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def delete_list_of_licenses_to_remove(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteListOfLicensesToRemoveErrorBody]`
- **Error**: `DeleteListOfLicensesToRemoveErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteListOfLicensesToRemoveErrorBody` | `verizon/errors/delete_list_of_licenses_to_remove_error.py` |

### client.software_management_licenses_v1.list_licenses_to_remove

- **Route**: `GET /licenses/{account}/cancel/index/{startIndex}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def list_licenses_to_remove(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `start_index`
- **Params**: `account` — path · `start_index` — path `startIndex`
- **Returns (parsed)**: `V1ListOfLicensesToRemove`
- **Returns (raw)**: `ApiResult[V1ListOfLicensesToRemove, ListLicensesToRemoveErrorBody]`
- **Error**: `ListLicensesToRemoveErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ListOfLicensesToRemove` | `verizon/models/v1_list_of_licenses_to_remove.py` |
| `ListLicensesToRemoveErrorBody` | `verizon/errors/list_licenses_to_remove_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_licenses_v1.remove_licenses_from_devices

- **Route**: `POST /licenses/{account}/remove`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def remove_licenses_from_devices(account: str, body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `body`
- **Params**: `account` — path · `body` — JSON body
- **Returns (parsed)**: `V1LicensesAssignedRemovedResult`
- **Returns (raw)**: `ApiResult[V1LicensesAssignedRemovedResult, RemoveLicensesFromDevicesErrorBody]`
- **Error**: `RemoveLicensesFromDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1LicensesAssignedRemovedRequest` | `verizon/models/v1_licenses_assigned_removed_request.py` |
| `V1LicensesAssignedRemovedRequestDict` | `verizon/models/v1_licenses_assigned_removed_request.py` |
| `V1LicensesAssignedRemovedResult` | `verizon/models/v1_licenses_assigned_removed_result.py` |
| `RemoveLicensesFromDevicesErrorBody` | `verizon/errors/remove_licenses_from_devices_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

