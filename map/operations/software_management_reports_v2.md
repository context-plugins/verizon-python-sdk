<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementReportsV2 — operations

Accessor: `client.software_management_reports_v2` · Source: `verizon/apis/software_management_reports_v2.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_reports_v2.get_campaign_device_status

- **Route**: `GET /reports/{account}/campaigns/{campaignId}/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_campaign_device_status(account: str, campaign_id: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `campaign_id`
- **Params**: `account` — path · `campaign_id` — path `campaignId` · `last_seen_device_id` — query `lastSeenDeviceId`
- **Returns (parsed)**: `V2CampaignDevice`
- **Returns (raw)**: `ApiResult[V2CampaignDevice, GetCampaignDeviceStatusErrorBody]`
- **Error**: `GetCampaignDeviceStatusErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2CampaignDevice` | `verizon/models/v2_campaign_device.py` |
| `GetCampaignDeviceStatusErrorBody` | `verizon/errors/get_campaign_device_status_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_reports_v2.get_campaign_history_by_status

- **Route**: `GET /reports/{account}/campaigns`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_campaign_history_by_status(account: str, campaign_status: str, *, last_seen_campaign_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `campaign_status`
- **Params**: `account` — path · `campaign_status` — query `campaignStatus` · `last_seen_campaign_id` — query `lastSeenCampaignId`
- **Returns (parsed)**: `V2CampaignHistory`
- **Returns (raw)**: `ApiResult[V2CampaignHistory, GetCampaignHistoryByStatusErrorBody]`
- **Error**: `GetCampaignHistoryByStatusErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2CampaignHistory` | `verizon/models/v2_campaign_history.py` |
| `GetCampaignHistoryByStatusErrorBody` | `verizon/errors/get_campaign_history_by_status_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_reports_v2.get_device_firmware_upgrade_history2

- **Route**: `GET /reports/{account}/devices/{deviceId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_device_firmware_upgrade_history2(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_id`
- **Params**: `account` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `list[DeviceSoftwareUpgrade]`
- **Returns (raw)**: `ApiResult[list[DeviceSoftwareUpgrade], GetDeviceFirmwareUpgradeHistory2ErrorBody]`
- **Error**: `GetDeviceFirmwareUpgradeHistory2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceSoftwareUpgrade` | `verizon/models/device_software_upgrade.py` |
| `GetDeviceFirmwareUpgradeHistory2ErrorBody` | `verizon/errors/get_device_firmware_upgrade_history2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_reports_v2.list_account_devices2

- **Route**: `GET /devices/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def list_account_devices2(account: str, *, last_seen_device_id: str | None = None, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path · `last_seen_device_id` — query `lastSeenDeviceId` · `distribution_type` — query `distributionType`
- **Returns (parsed)**: `V2AccountDeviceList`
- **Returns (raw)**: `ApiResult[V2AccountDeviceList, ListAccountDevices2ErrorBody]`
- **Error**: `ListAccountDevices2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2AccountDeviceList` | `verizon/models/v2_account_device_list.py` |
| `ListAccountDevices2ErrorBody` | `verizon/errors/list_account_devices2_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.software_management_reports_v2.list_available_software

- **Route**: `GET /software/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def list_available_software(account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path · `distribution_type` — query `distributionType`
- **Returns (parsed)**: `list[SoftwarePackage]`
- **Returns (raw)**: `ApiResult[list[SoftwarePackage], ListAvailableSoftwareErrorBody]`
- **Error**: `ListAvailableSoftwareErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SoftwarePackage` | `verizon/models/software_package.py` |
| `ListAvailableSoftwareErrorBody` | `verizon/errors/list_available_software_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

