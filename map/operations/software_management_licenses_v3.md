<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementLicensesV3 — operations

Accessor: `client.software_management_licenses_v3` · Source: `verizon/apis/software_management_licenses_v3.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_licenses_v3.assign_licenses_to_devices3

- **Route**: `POST /licenses/{acc}/assign`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def assign_licenses_to_devices3(acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `V3LicenseAssignedRemovedResult`
- **Returns (raw)**: `ApiResult[V3LicenseAssignedRemovedResult, AssignLicensesToDevices3ErrorBody]`
- **Error**: `AssignLicensesToDevices3ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3LicenseImei` | `verizon/models/v3_license_imei.py` |
| `V3LicenseImeiDict` | `verizon/models/v3_license_imei.py` |
| `V3LicenseAssignedRemovedResult` | `verizon/models/v3_license_assigned_removed_result.py` |
| `AssignLicensesToDevices3ErrorBody` | `verizon/errors/assign_licenses_to_devices3_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_licenses_v3.get_account_licenses_status

- **Route**: `GET /licenses/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_account_licenses_status(acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`
- **Params**: `acc` — path · `last_seen_device_id` — query `lastSeenDeviceId`
- **Returns (parsed)**: `V3LicenseSummary`
- **Returns (raw)**: `ApiResult[V3LicenseSummary, GetAccountLicensesStatusErrorBody]`
- **Error**: `GetAccountLicensesStatusErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3LicenseSummary` | `verizon/models/v3_license_summary.py` |
| `GetAccountLicensesStatusErrorBody` | `verizon/errors/get_account_licenses_status_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_licenses_v3.remove_licenses_from_devices3

- **Route**: `POST /licenses/{acc}/remove`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def remove_licenses_from_devices3(acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `V3LicenseAssignedRemovedResult`
- **Returns (raw)**: `ApiResult[V3LicenseAssignedRemovedResult, RemoveLicensesFromDevices3ErrorBody]`
- **Error**: `RemoveLicensesFromDevices3ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3LicenseImei` | `verizon/models/v3_license_imei.py` |
| `V3LicenseImeiDict` | `verizon/models/v3_license_imei.py` |
| `V3LicenseAssignedRemovedResult` | `verizon/models/v3_license_assigned_removed_result.py` |
| `RemoveLicensesFromDevices3ErrorBody` | `verizon/errors/remove_licenses_from_devices3_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

