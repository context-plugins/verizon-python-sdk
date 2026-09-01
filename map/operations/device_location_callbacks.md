<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceLocationCallbacks — operations

Accessor: `client.device_location_callbacks` · Source: `verizon/apis/device_location_callbacks.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_location_callbacks.cancel_async_report

- **Route**: `DELETE /devicelocations/{txid}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def cancel_async_report(txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `txid`, `account_name`
- **Params**: `txid` — path · `account_name` — query `accountName`
- **Returns (parsed)**: `TransactionId`
- **Returns (raw)**: `ApiResult[TransactionId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionId` | `verizon/models/transaction_id.py` |

### client.device_location_callbacks.deregister_callback2

- **Route**: `DELETE /callbacks/{accountName}/name/{service}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def deregister_callback2(account_name: str, service: CallbackServiceNameOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `service`
- **Params**: `account_name` — path `accountName` · `service` — path
- **Returns (parsed)**: `DeviceLocationSuccessResult`
- **Returns (raw)**: `ApiResult[DeviceLocationSuccessResult, DeregisterCallback2ErrorBody]`
- **Error**: `DeregisterCallback2ErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CallbackServiceNameOrStr` | `verizon/models/enums/callback_service_name.py` |
| `DeviceLocationSuccessResult` | `verizon/models/device_location_success_result.py` |
| `DeregisterCallback2ErrorBody` | `verizon/errors/deregister_callback2_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.device_location_callbacks.list_registered_callbacks2

- **Route**: `GET /callbacks/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def list_registered_callbacks2(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `list[DeviceLocationCallback]`
- **Returns (raw)**: `ApiResult[list[DeviceLocationCallback], ListRegisteredCallbacks2ErrorBody]`
- **Error**: `ListRegisteredCallbacks2ErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLocationCallback` | `verizon/models/device_location_callback.py` |
| `ListRegisteredCallbacks2ErrorBody` | `verizon/errors/list_registered_callbacks2_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.device_location_callbacks.register_callback2

- **Route**: `POST /callbacks/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def register_callback2(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `CallbackRegistrationResult`
- **Returns (raw)**: `ApiResult[CallbackRegistrationResult, RegisterCallback2ErrorBody]`
- **Error**: `RegisterCallback2ErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CallbackRegistrationResult` | `verizon/models/callback_registration_result.py` |
| `RegisterCallback2ErrorBody` | `verizon/errors/register_callback2_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

