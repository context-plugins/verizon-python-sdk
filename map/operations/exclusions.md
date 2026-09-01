<!-- Generated file — do not edit; regenerated with the SDK. -->

# Exclusions — operations

Accessor: `client.exclusions` · Source: `verizon/apis/exclusions.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.exclusions.devices_location_get_consent_async

- **Route**: `GET /devicelocations/action/consents`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def devices_location_get_consent_async(account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — query `accountName` · `device_id` — query `deviceId`
- **Returns (parsed)**: `GetAccountDeviceConsent`
- **Returns (raw)**: `ApiResult[GetAccountDeviceConsent, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetAccountDeviceConsent` | `verizon/models/get_account_device_consent.py` |

### client.exclusions.devices_location_give_consent_async

- **Route**: `POST /devicelocations/action/consents`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def devices_location_give_consent_async(*, body: AccountConsentCreate | AccountConsentCreateDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ConsentTransactionId`
- **Returns (raw)**: `ApiResult[ConsentTransactionId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountConsentCreate` | `verizon/models/account_consent_create.py` |
| `AccountConsentCreateDict` | `verizon/models/account_consent_create.py` |
| `ConsentTransactionId` | `verizon/models/consent_transaction_id.py` |

### client.exclusions.devices_location_update_consent

- **Route**: `PUT /devicelocations/action/consents`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def devices_location_update_consent(*, body: AccountConsentUpdate | AccountConsentUpdateDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ConsentTransactionId`
- **Returns (raw)**: `ApiResult[ConsentTransactionId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountConsentUpdate` | `verizon/models/account_consent_update.py` |
| `AccountConsentUpdateDict` | `verizon/models/account_consent_update.py` |
| `ConsentTransactionId` | `verizon/models/consent_transaction_id.py` |

### client.exclusions.exclude_devices

- **Route**: `POST /consents`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def exclude_devices(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DeviceLocationSuccessResult`
- **Returns (raw)**: `ApiResult[DeviceLocationSuccessResult, ExcludeDevicesErrorBody]`
- **Error**: `ExcludeDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLocationSuccessResult` | `verizon/models/device_location_success_result.py` |
| `ExcludeDevicesErrorBody` | `verizon/errors/exclude_devices_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.exclusions.list_excluded_devices

- **Route**: `GET /consents/{accountName}/index/{startIndex}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def list_excluded_devices(account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `start_index`
- **Params**: `account_name` — path `accountName` · `start_index` — path `startIndex`
- **Returns (parsed)**: `DevicesConsentResult`
- **Returns (raw)**: `ApiResult[DevicesConsentResult, ListExcludedDevicesErrorBody]`
- **Error**: `ListExcludedDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DevicesConsentResult` | `verizon/models/devices_consent_result.py` |
| `ListExcludedDevicesErrorBody` | `verizon/errors/list_excluded_devices_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.exclusions.remove_devices_from_exclusion_list

- **Route**: `DELETE /consents`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def remove_devices_from_exclusion_list(account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `device_list`
- **Params**: `account_name` — query `accountName` · `device_list` — query `deviceList`
- **Returns (parsed)**: `DeviceLocationSuccessResult`
- **Returns (raw)**: `ApiResult[DeviceLocationSuccessResult, RemoveDevicesFromExclusionListErrorBody]`
- **Error**: `RemoveDevicesFromExclusionListErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLocationSuccessResult` | `verizon/models/device_location_success_result.py` |
| `RemoveDevicesFromExclusionListErrorBody` | `verizon/errors/remove_devices_from_exclusion_list_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

