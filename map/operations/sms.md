<!-- Generated file — do not edit; regenerated with the SDK. -->

# Sms — operations

Accessor: `client.sms` · Source: `verizon/apis/sms.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sms.list_devices_sms_messages

- **Route**: `GET /m2m/v1/sms/{aname}/history`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_devices_sms_messages(aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path · `next` — query
- **Returns (parsed)**: `SmsmessagesQueryResult`
- **Returns (raw)**: `ApiResult[SmsmessagesQueryResult, ListDevicesSmsmessagesErrorBody]`
- **Error**: `ListDevicesSmsmessagesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SmsmessagesQueryResult` | `verizon/models/smsmessages_query_result.py` |
| `ListDevicesSmsmessagesErrorBody` | `verizon/errors/list_devices_smsmessages_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.sms.send_sms_to_device

- **Route**: `POST /m2m/v1/sms`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def send_sms_to_device(body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, SendSmstoDeviceErrorBody]`
- **Error**: `SendSmstoDeviceErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SmssendRequest` | `verizon/models/smssend_request.py` |
| `SmssendRequestDict` | `verizon/models/smssend_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `SendSmstoDeviceErrorBody` | `verizon/errors/send_smsto_device_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.sms.start_queued_sms_delivery

- **Route**: `PUT /m2m/v1/sms/{aname}/startCallbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def start_queued_sms_delivery(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `ConnectivityManagementSuccessResult`
- **Returns (raw)**: `ApiResult[ConnectivityManagementSuccessResult, StartQueuedSmsdeliveryErrorBody]`
- **Error**: `StartQueuedSmsdeliveryErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConnectivityManagementSuccessResult` | `verizon/models/connectivity_management_success_result.py` |
| `StartQueuedSmsdeliveryErrorBody` | `verizon/errors/start_queued_smsdelivery_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

