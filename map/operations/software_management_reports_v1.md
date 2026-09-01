<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementReportsV1 — operations

Accessor: `client.software_management_reports_v1` · Source: `verizon/apis/software_management_reports_v1.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_reports_v1.get_device_firmware_upgrade_history

- **Route**: `GET /reports/{account}/devices/{deviceId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def get_device_firmware_upgrade_history(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_id`
- **Params**: `account` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `list[DeviceUpgradeHistory]`
- **Returns (raw)**: `ApiResult[list[DeviceUpgradeHistory], GetDeviceFirmwareUpgradeHistoryErrorBody]`
- **Error**: `GetDeviceFirmwareUpgradeHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceUpgradeHistory` | `verizon/models/device_upgrade_history.py` |
| `GetDeviceFirmwareUpgradeHistoryErrorBody` | `verizon/errors/get_device_firmware_upgrade_history_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_reports_v1.list_account_devices

- **Route**: `GET /devices/{account}/index/{startIndex}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def list_account_devices(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `start_index`
- **Params**: `account` — path · `start_index` — path `startIndex`
- **Returns (parsed)**: `DeviceListQueryResult`
- **Returns (raw)**: `ApiResult[DeviceListQueryResult, ListAccountDevicesErrorBody]`
- **Error**: `ListAccountDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceListQueryResult` | `verizon/models/device_list_query_result.py` |
| `ListAccountDevicesErrorBody` | `verizon/errors/list_account_devices_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.software_management_reports_v1.list_upgrades_for_specified_status

- **Route**: `GET /reports/{account}/status/{upgradeStatus}/index/{startIndex}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def list_upgrades_for_specified_status(account: str, upgrade_status: UpgradeStatusOrStr, start_index: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `upgrade_status`, `start_index`
- **Params**: `account` — path · `upgrade_status` — path `upgradeStatus` · `start_index` — path `startIndex`
- **Returns (parsed)**: `UpgradeListQueryResult`
- **Returns (raw)**: `ApiResult[UpgradeListQueryResult, ListUpgradesForSpecifiedStatusErrorBody]`
- **Error**: `ListUpgradesForSpecifiedStatusErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpgradeStatusOrStr` | `verizon/models/enums/upgrade_status.py` |
| `UpgradeListQueryResult` | `verizon/models/upgrade_list_query_result.py` |
| `ListUpgradesForSpecifiedStatusErrorBody` | `verizon/errors/list_upgrades_for_specified_status_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

