<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoftwareManagementReportsV3 — operations

Accessor: `client.software_management_reports_v3` · Source: `verizon/apis/software_management_reports_v3.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.software_management_reports_v3.get_campaign_device_status2

- **Route**: `GET /reports/{acc}/campaigns/{campaignId}/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_campaign_device_status2(acc: str, campaign_id: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `campaign_id`
- **Params**: `acc` — path · `campaign_id` — path `campaignId` · `last_seen_device_id` — query `lastSeenDeviceId`
- **Returns (parsed)**: `V3CampaignDevice`
- **Returns (raw)**: `ApiResult[V3CampaignDevice, GetCampaignDeviceStatus2ErrorBody]`
- **Error**: `GetCampaignDeviceStatus2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3CampaignDevice` | `verizon/models/v3_campaign_device.py` |
| `GetCampaignDeviceStatus2ErrorBody` | `verizon/errors/get_campaign_device_status2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_reports_v3.get_campaign_history_by_status2

- **Route**: `GET /reports/{acc}/firmware/campaigns`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_campaign_history_by_status2(acc: str, campaign_status: CampaignStatusOrStr, *, last_seen_campaign_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `campaign_status`
- **Params**: `acc` — path · `campaign_status` — query `campaignStatus` · `last_seen_campaign_id` — query `lastSeenCampaignId`
- **Returns (parsed)**: `V3CampaignHistory`
- **Returns (raw)**: `ApiResult[V3CampaignHistory, GetCampaignHistoryByStatus2ErrorBody]`
- **Error**: `GetCampaignHistoryByStatus2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CampaignStatusOrStr` | `verizon/models/enums/campaign_status.py` |
| `V3CampaignHistory` | `verizon/models/v3_campaign_history.py` |
| `GetCampaignHistoryByStatus2ErrorBody` | `verizon/errors/get_campaign_history_by_status2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.software_management_reports_v3.get_device_firmware_upgrade_history3

- **Route**: `GET /reports/{acc}/devices/{deviceId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_device_firmware_upgrade_history3(acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `device_id`
- **Params**: `acc` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `list[DeviceFirmwareUpgrade]`
- **Returns (raw)**: `ApiResult[list[DeviceFirmwareUpgrade], GetDeviceFirmwareUpgradeHistory3ErrorBody]`
- **Error**: `GetDeviceFirmwareUpgradeHistory3ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceFirmwareUpgrade` | `verizon/models/device_firmware_upgrade.py` |
| `GetDeviceFirmwareUpgradeHistory3ErrorBody` | `verizon/errors/get_device_firmware_upgrade_history3_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

