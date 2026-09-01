<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceSmsMessaging — operations

Accessor: `client.device_sms_messaging` · Source: `verizon/apis/device_sms_messaging.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_sms_messaging.get_sms_messages

- **Route**: `GET /m2m/v1/sms/{accountName}/history`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_sms_messages(account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName` · `next` — query
- **Returns (parsed)**: `SmsMessagesResponse`
- **Returns (raw)**: `ApiResult[SmsMessagesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SmsMessagesResponse` | `verizon/models/sms_messages_response.py` |

### client.device_sms_messaging.list_sms_message_history

- **Route**: `POST /m2m/v1/devices/sms/history/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_sms_message_history(body: SmseventHistoryRequest | SmseventHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SmseventHistoryRequest` | `verizon/models/smsevent_history_request.py` |
| `SmseventHistoryRequestDict` | `verizon/models/smsevent_history_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.device_sms_messaging.send_an_sms_message

- **Route**: `POST /m2m/v1/sms`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def send_an_sms_message(body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GiosmssendRequest` | `verizon/models/giosmssend_request.py` |
| `GiosmssendRequestDict` | `verizon/models/giosmssend_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.device_sms_messaging.start_sms_message_delivery

- **Route**: `PUT /m2m/v1/sms/{accountName}/startCallbacks`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def start_sms_message_delivery(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `SuccessResponse`
- **Returns (raw)**: `ApiResult[SuccessResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SuccessResponse` | `verizon/models/success_response.py` |

