<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementLicensesV2 — operations

Accessor: `client.software_management_licenses_v2` · Source: `verizon/apis/software_management_licenses_v2.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_licenses_v2.assign_licenses_to_devices2

- **Route**: `POST /licenses/{account}/assign`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def assign_licenses_to_devices2(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `V2LicensesAssignedRemovedResult`
- **Returns (raw)**: `ApiResult[V2LicensesAssignedRemovedResult, AssignLicensesToDevices2ErrorBody]`
- **Error**: `AssignLicensesToDevices2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2LicensesAssignedRemovedResult` | `verizon/models/v2_licenses_assigned_removed_result.py` |
| `AssignLicensesToDevices2ErrorBody` | `verizon/errors/assign_licenses_to_devices2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_licenses_v2.create_list_of_licenses_to_remove2

- **Route**: `POST /licenses/{account}/cancel`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def create_list_of_licenses_to_remove2(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `V2ListOfLicensesToRemoveResult`
- **Returns (raw)**: `ApiResult[V2ListOfLicensesToRemoveResult, CreateListOfLicensesToRemove2ErrorBody]`
- **Error**: `CreateListOfLicensesToRemove2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ListOfLicensesToRemoveResult` | `verizon/models/v2_list_of_licenses_to_remove_result.py` |
| `CreateListOfLicensesToRemove2ErrorBody` | `verizon/errors/create_list_of_licenses_to_remove2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_licenses_v2.delete_list_of_licenses_to_remove2

- **Route**: `DELETE /licenses/{account}/cancel`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def delete_list_of_licenses_to_remove2(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `FotaV2SuccessResult`
- **Returns (raw)**: `ApiResult[FotaV2SuccessResult, DeleteListOfLicensesToRemove2ErrorBody]`
- **Error**: `DeleteListOfLicensesToRemove2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV2SuccessResult` | `verizon/models/fota_v2_success_result.py` |
| `DeleteListOfLicensesToRemove2ErrorBody` | `verizon/errors/delete_list_of_licenses_to_remove2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_licenses_v2.get_account_license_status2

- **Route**: `GET /licenses/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_account_license_status2(account: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path · `last_seen_device_id` — query `lastSeenDeviceId`
- **Returns (parsed)**: `V2LicenseSummary`
- **Returns (raw)**: `ApiResult[V2LicenseSummary, GetAccountLicenseStatus2ErrorBody]`
- **Error**: `GetAccountLicenseStatus2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2LicenseSummary` | `verizon/models/v2_license_summary.py` |
| `GetAccountLicenseStatus2ErrorBody` | `verizon/errors/get_account_license_status2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_licenses_v2.list_licenses_to_remove2

- **Route**: `GET /licenses/{account}/cancel`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def list_licenses_to_remove2(account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path · `start_index` — query `startIndex`
- **Returns (parsed)**: `V2ListOfLicensesToRemove`
- **Returns (raw)**: `ApiResult[V2ListOfLicensesToRemove, ListLicensesToRemove2ErrorBody]`
- **Error**: `ListLicensesToRemove2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2ListOfLicensesToRemove` | `verizon/models/v2_list_of_licenses_to_remove.py` |
| `ListLicensesToRemove2ErrorBody` | `verizon/errors/list_licenses_to_remove2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_licenses_v2.remove_licenses_from_devices2

- **Route**: `POST /licenses/{account}/remove`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def remove_licenses_from_devices2(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `V2LicensesAssignedRemovedResult`
- **Returns (raw)**: `ApiResult[V2LicensesAssignedRemovedResult, RemoveLicensesFromDevices2ErrorBody]`
- **Error**: `RemoveLicensesFromDevices2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2LicensesAssignedRemovedResult` | `verizon/models/v2_licenses_assigned_removed_result.py` |
| `RemoveLicensesFromDevices2ErrorBody` | `verizon/errors/remove_licenses_from_devices2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

