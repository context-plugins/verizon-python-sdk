<!-- Generated file — do not edit; regenerated with the SDK. -->

# CampaignsV3 — operations

Accessor: `client.campaigns_v3` · Source: `verizon/apis/campaigns_v3.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.campaigns_v3.cancel_campaign2

- **Route**: `DELETE /campaigns/{accountName}/{campaignId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def cancel_campaign2(account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `campaign_id`
- **Params**: `account_name` — path `accountName` · `campaign_id` — path `campaignId`
- **Returns (parsed)**: `FotaV3SuccessResult`
- **Returns (raw)**: `ApiResult[FotaV3SuccessResult, CancelCampaign2ErrorBody]`
- **Error**: `CancelCampaign2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FotaV3SuccessResult` | `verizon/models/fota_v3_success_result.py` |
| `CancelCampaign2ErrorBody` | `verizon/errors/cancel_campaign2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.campaigns_v3.get_campaign_information2

- **Route**: `GET /campaigns/{accountName}/{campaignId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_campaign_information2(account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `campaign_id`
- **Params**: `account_name` — path `accountName` · `campaign_id` — path `campaignId`
- **Returns (parsed)**: `Campaign`
- **Returns (raw)**: `ApiResult[Campaign, GetCampaignInformation2ErrorBody]`
- **Error**: `GetCampaignInformation2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Campaign` | `verizon/models/campaign.py` |
| `GetCampaignInformation2ErrorBody` | `verizon/errors/get_campaign_information2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.campaigns_v3.schedule_campaign_firmware_upgrade2

- **Route**: `POST /campaigns/firmware/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def schedule_campaign_firmware_upgrade2(account_name: str, body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `body`
- **Params**: `account_name` — path `accountName` · `body` — JSON body
- **Returns (parsed)**: `FirmwareCampaign`
- **Returns (raw)**: `ApiResult[FirmwareCampaign, ScheduleCampaignFirmwareUpgrade2ErrorBody]`
- **Error**: `ScheduleCampaignFirmwareUpgrade2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CampaignFirmwareUpgrade` | `verizon/models/campaign_firmware_upgrade.py` |
| `CampaignFirmwareUpgradeDict` | `verizon/models/campaign_firmware_upgrade.py` |
| `FirmwareCampaign` | `verizon/models/firmware_campaign.py` |
| `ScheduleCampaignFirmwareUpgrade2ErrorBody` | `verizon/errors/schedule_campaign_firmware_upgrade2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.campaigns_v3.update_campaign_dates2

- **Route**: `PUT /campaigns/firmware/{acc}/{campaignId}/dates`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def update_campaign_dates2(acc: str, campaign_id: str, body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `campaign_id`, `body`
- **Params**: `acc` — path · `campaign_id` — path `campaignId` · `body` — JSON body
- **Returns (parsed)**: `FirmwareCampaign`
- **Returns (raw)**: `ApiResult[FirmwareCampaign, UpdateCampaignDates2ErrorBody]`
- **Error**: `UpdateCampaignDates2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3ChangeCampaignDatesRequest` | `verizon/models/v3_change_campaign_dates_request.py` |
| `V3ChangeCampaignDatesRequestDict` | `verizon/models/v3_change_campaign_dates_request.py` |
| `FirmwareCampaign` | `verizon/models/firmware_campaign.py` |
| `UpdateCampaignDates2ErrorBody` | `verizon/errors/update_campaign_dates2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.campaigns_v3.update_campaign_firmware_devices2

- **Route**: `PUT /campaigns/firmware/{acc}/{campaignId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def update_campaign_firmware_devices2(acc: str, campaign_id: str, body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `campaign_id`, `body`
- **Params**: `acc` — path · `campaign_id` — path `campaignId` · `body` — JSON body
- **Returns (parsed)**: `V3AddOrRemoveDeviceResult`
- **Returns (raw)**: `ApiResult[V3AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevices2ErrorBody]`
- **Error**: `UpdateCampaignFirmwareDevices2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3AddOrRemoveDeviceRequest` | `verizon/models/v3_add_or_remove_device_request.py` |
| `V3AddOrRemoveDeviceRequestDict` | `verizon/models/v3_add_or_remove_device_request.py` |
| `V3AddOrRemoveDeviceResult` | `verizon/models/v3_add_or_remove_device_result.py` |
| `UpdateCampaignFirmwareDevices2ErrorBody` | `verizon/errors/update_campaign_firmware_devices2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

