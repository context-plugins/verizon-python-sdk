<!-- Generated file — do not edit; regenerated with the SDK. -->

# FirmwareV1 — operations

Accessor: `client.firmware_v1` · Source: `verizon/apis/firmware_v1.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.firmware_v1.cancel_scheduled_firmware_upgrade

- **Route**: `DELETE /upgrades/{accountName}/upgrade/{upgradeId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def cancel_scheduled_firmware_upgrade(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `upgrade_id`
- **Params**: `account_name` — path `accountName` · `upgrade_id` — path `upgradeId`
- **Returns (parsed)**: `FotaV1SuccessResult`
- **Returns (raw)**: `ApiResult[FotaV1SuccessResult, CancelScheduledFirmwareUpgradeErrorBody]`
- **Error**: `CancelScheduledFirmwareUpgradeErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV1SuccessResult` | `verizon/models/fota_v1_success_result.py` |
| `CancelScheduledFirmwareUpgradeErrorBody` | `verizon/errors/cancel_scheduled_firmware_upgrade_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.firmware_v1.list_available_firmware

- **Route**: `GET /firmware/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def list_available_firmware(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `list[Firmware]`
- **Returns (raw)**: `ApiResult[list[Firmware], ListAvailableFirmwareErrorBody]`
- **Error**: `ListAvailableFirmwareErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Firmware` | `verizon/models/firmware.py` |
| `ListAvailableFirmwareErrorBody` | `verizon/errors/list_available_firmware_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.firmware_v1.list_firmware_upgrade_details

- **Route**: `GET /upgrades/{accountName}/upgrade/{upgradeId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def list_firmware_upgrade_details(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `upgrade_id`
- **Params**: `account_name` — path `accountName` · `upgrade_id` — path `upgradeId`
- **Returns (parsed)**: `FirmwareUpgrade`
- **Returns (raw)**: `ApiResult[FirmwareUpgrade, ListFirmwareUpgradeDetailsErrorBody]`
- **Error**: `ListFirmwareUpgradeDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FirmwareUpgrade` | `verizon/models/firmware_upgrade.py` |
| `ListFirmwareUpgradeDetailsErrorBody` | `verizon/errors/list_firmware_upgrade_details_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.firmware_v1.schedule_firmware_upgrade

- **Route**: `POST /upgrades`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def schedule_firmware_upgrade(body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FirmwareUpgrade`
- **Returns (raw)**: `ApiResult[FirmwareUpgrade, ScheduleFirmwareUpgradeErrorBody]`
- **Error**: `ScheduleFirmwareUpgradeErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FirmwareUpgradeRequest` | `verizon/models/firmware_upgrade_request.py` |
| `FirmwareUpgradeRequestDict` | `verizon/models/firmware_upgrade_request.py` |
| `FirmwareUpgrade` | `verizon/models/firmware_upgrade.py` |
| `ScheduleFirmwareUpgradeErrorBody` | `verizon/errors/schedule_firmware_upgrade_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

### client.firmware_v1.update_firmware_upgrade_devices

- **Route**: `PUT /upgrades/{accountName}/upgrade/{upgradeId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v1`
- **Signature**: `def update_firmware_upgrade_devices(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `upgrade_id`
- **Params**: `account_name` — path `accountName` · `upgrade_id` — path `upgradeId`
- **Returns (parsed)**: `FirmwareUpgradeChangeResult`
- **Returns (raw)**: `ApiResult[FirmwareUpgradeChangeResult, UpdateFirmwareUpgradeDevicesErrorBody]`
- **Error**: `UpdateFirmwareUpgradeDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV1Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FirmwareUpgradeChangeResult` | `verizon/models/firmware_upgrade_change_result.py` |
| `UpdateFirmwareUpgradeDevicesErrorBody` | `verizon/errors/update_firmware_upgrade_devices_error.py` |
| `FotaV1Result` | `verizon/models/fota_v1_result.py` |

