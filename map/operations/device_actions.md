<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceActions — operations

Accessor: `client.device_actions` · Source: `verizon/apis/device_actions.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_actions.account_information

- **Route**: `GET /v1/accounts/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def account_information(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `AccountDetails`
- **Returns (raw)**: `ApiResult[AccountDetails, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountDetails` | `verizon/models/account_details.py` |

### client.device_actions.aggregate_usage

- **Route**: `POST /v1/devices/usage/actions/list/aggregate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def aggregate_usage(body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AggregateUsage` | `verizon/models/aggregate_usage.py` |
| `AggregateUsageDict` | `verizon/models/aggregate_usage.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.device_actions.daily_usage

- **Route**: `POST /v1/devices/usage/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def daily_usage(body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DailyUsageResponse`
- **Returns (raw)**: `ApiResult[DailyUsageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DailyUsage` | `verizon/models/daily_usage.py` |
| `DailyUsageDict` | `verizon/models/daily_usage.py` |
| `DailyUsageResponse` | `verizon/models/daily_usage_response.py` |

### client.device_actions.get_asynchronous_request_status

- **Route**: `GET /m2m/v2/accounts/{accountName}/requests/{requestID}/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_asynchronous_request_status(account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `request_id`
- **Params**: `account_name` — path `accountName` · `request_id` — path `requestID`
- **Returns (parsed)**: `StatusResponse`
- **Returns (raw)**: `ApiResult[StatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StatusResponse` | `verizon/models/status_response.py` |

### client.device_actions.retrieve_device_provisioning_history

- **Route**: `POST /m2m/v2/devices/history/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_device_provisioning_history(body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProvhistoryRequest` | `verizon/models/provhistory_request.py` |
| `ProvhistoryRequestDict` | `verizon/models/provhistory_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.device_actions.retrieve_the_global_device_list

- **Route**: `POST /m2m/v2/devices/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_the_global_device_list(body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GiorequestResponse`
- **Returns (raw)**: `ApiResult[GiorequestResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetDeviceListWithProfilesRequest` | `verizon/models/get_device_list_with_profiles_request.py` |
| `GetDeviceListWithProfilesRequestDict` | `verizon/models/get_device_list_with_profiles_request.py` |
| `GiorequestResponse` | `verizon/models/giorequest_response.py` |

### client.device_actions.service_plan_list

- **Route**: `GET /v1/plans/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def service_plan_list(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `AccountDetails`
- **Returns (raw)**: `ApiResult[AccountDetails, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountDetails` | `verizon/models/account_details.py` |

