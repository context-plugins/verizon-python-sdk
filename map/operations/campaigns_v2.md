<!-- Generated file — do not edit; regenerated with the SDK. -->

# CampaignsV2 — operations

Accessor: `client.campaigns_v2` · Source: `verizon/apis/campaigns_v2.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.campaigns_v2.cancel_campaign

- **Route**: `DELETE /campaigns/{account}/{campaignId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def cancel_campaign(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `campaign_id`
- **Params**: `account` — path · `campaign_id` — path `campaignId`
- **Returns (parsed)**: `FotaV2SuccessResult`
- **Returns (raw)**: `ApiResult[FotaV2SuccessResult, CancelCampaignErrorBody]`
- **Error**: `CancelCampaignErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV2SuccessResult` | `verizon/models/fota_v2_success_result.py` |
| `CancelCampaignErrorBody` | `verizon/errors/cancel_campaign_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.campaigns_v2.get_campaign_information

- **Route**: `GET /campaigns/{account}/{campaignId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_campaign_information(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `campaign_id`
- **Params**: `account` — path · `campaign_id` — path `campaignId`
- **Returns (parsed)**: `CampaignSoftware`
- **Returns (raw)**: `ApiResult[CampaignSoftware, GetCampaignInformationErrorBody]`
- **Error**: `GetCampaignInformationErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CampaignSoftware` | `verizon/models/campaign_software.py` |
| `GetCampaignInformationErrorBody` | `verizon/errors/get_campaign_information_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.campaigns_v2.schedule_campaign_firmware_upgrade

- **Route**: `POST /campaigns/{account}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def schedule_campaign_firmware_upgrade(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `CampaignSoftware`
- **Returns (raw)**: `ApiResult[CampaignSoftware, ScheduleCampaignFirmwareUpgradeErrorBody]`
- **Error**: `ScheduleCampaignFirmwareUpgradeErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CampaignSoftware` | `verizon/models/campaign_software.py` |
| `ScheduleCampaignFirmwareUpgradeErrorBody` | `verizon/errors/schedule_campaign_firmware_upgrade_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.campaigns_v2.schedule_file_upgrade

- **Route**: `POST /campaigns/files/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def schedule_file_upgrade(acc: str, body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `UploadAndScheduleFileResponse`
- **Returns (raw)**: `ApiResult[UploadAndScheduleFileResponse, ScheduleFileUpgradeErrorBody]`
- **Error**: `ScheduleFileUpgradeErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadAndScheduleFileRequest` | `verizon/models/upload_and_schedule_file_request.py` |
| `UploadAndScheduleFileRequestDict` | `verizon/models/upload_and_schedule_file_request.py` |
| `UploadAndScheduleFileResponse` | `verizon/models/upload_and_schedule_file_response.py` |
| `ScheduleFileUpgradeErrorBody` | `verizon/errors/schedule_file_upgrade_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.campaigns_v2.schedule_sw_upgrade_http_devices

- **Route**: `POST /campaigns/software/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def schedule_sw_upgrade_http_devices(acc: str, body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `UploadAndScheduleFileResponse`
- **Returns (raw)**: `ApiResult[UploadAndScheduleFileResponse, ScheduleSwupgradeHttpDevicesErrorBody]`
- **Error**: `ScheduleSwupgradeHttpDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SchedulesSoftwareUpgradeRequest` | `verizon/models/schedules_software_upgrade_request.py` |
| `SchedulesSoftwareUpgradeRequestDict` | `verizon/models/schedules_software_upgrade_request.py` |
| `UploadAndScheduleFileResponse` | `verizon/models/upload_and_schedule_file_response.py` |
| `ScheduleSwupgradeHttpDevicesErrorBody` | `verizon/errors/schedule_swupgrade_http_devices_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.campaigns_v2.update_campaign_dates

- **Route**: `PUT /campaigns/{account}/{campaignId}/dates`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def update_campaign_dates(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `campaign_id`
- **Params**: `account` — path · `campaign_id` — path `campaignId`
- **Returns (parsed)**: `CampaignSoftware`
- **Returns (raw)**: `ApiResult[CampaignSoftware, UpdateCampaignDatesErrorBody]`
- **Error**: `UpdateCampaignDatesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CampaignSoftware` | `verizon/models/campaign_software.py` |
| `UpdateCampaignDatesErrorBody` | `verizon/errors/update_campaign_dates_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.campaigns_v2.update_campaign_firmware_devices

- **Route**: `PUT /campaigns/{account}/{campaignId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def update_campaign_firmware_devices(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `campaign_id`
- **Params**: `account` — path · `campaign_id` — path `campaignId`
- **Returns (parsed)**: `V2AddOrRemoveDeviceResult`
- **Returns (raw)**: `ApiResult[V2AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevicesErrorBody]`
- **Error**: `UpdateCampaignFirmwareDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V2AddOrRemoveDeviceResult` | `verizon/models/v2_add_or_remove_device_result.py` |
| `UpdateCampaignFirmwareDevicesErrorBody` | `verizon/errors/update_campaign_firmware_devices_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

