<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsUsers — operations

Accessor: `client.sensor_insights_users` · Source: `verizon/apis/sensor_insights_users.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_users.sensor_insights_create_user_request

- **Route**: `POST /dm/v1/users`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_create_user_request(body: DtoCreateUserRequest | DtoCreateUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ResourceUser`
- **Returns (raw)**: `ApiResult[ResourceUser, SensorInsightsCreateUserRequestErrorBody]`
- **Error**: `SensorInsightsCreateUserRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoCreateUserRequest` | `verizon/models/dto_create_user_request.py` |
| `DtoCreateUserRequestDict` | `verizon/models/dto_create_user_request.py` |
| `ResourceUser` | `verizon/models/resource_user.py` |
| `SensorInsightsCreateUserRequestErrorBody` | `verizon/errors/sensor_insights_create_user_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_users.sensor_insights_delete_user

- **Route**: `DELETE /dm/v1/users`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_delete_user(deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `deleterequestpayload`
- **Params**: `deleterequestpayload` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SensorInsightsDeleteUserErrorBody]`
- **Error**: `SensorInsightsDeleteUserErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError404` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoDeleteUserRequest` | `verizon/models/dto_delete_user_request.py` |
| `DtoDeleteUserRequestDict` | `verizon/models/dto_delete_user_request.py` |
| `SensorInsightsDeleteUserErrorBody` | `verizon/errors/sensor_insights_delete_user_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |

### client.sensor_insights_users.sensor_insights_list_user_request

- **Route**: `POST /dm/v1/users/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_user_request(body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[ResourceUser]`
- **Returns (raw)**: `ApiResult[list[ResourceUser], SensorInsightsListUserRequestErrorBody]`
- **Error**: `SensorInsightsListUserRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListUserRequest` | `verizon/models/dto_list_user_request.py` |
| `DtoListUserRequestDict` | `verizon/models/dto_list_user_request.py` |
| `ResourceUser` | `verizon/models/resource_user.py` |
| `SensorInsightsListUserRequestErrorBody` | `verizon/errors/sensor_insights_list_user_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_users.sensor_insights_update_user_request

- **Route**: `PATCH /dm/v1/users`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_update_user_request(body: DtoUpdateUserRequest | DtoUpdateUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ResourceUser`
- **Returns (raw)**: `ApiResult[ResourceUser, SensorInsightsUpdateUserRequestErrorBody]`
- **Error**: `SensorInsightsUpdateUserRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoUpdateUserRequest` | `verizon/models/dto_update_user_request.py` |
| `DtoUpdateUserRequestDict` | `verizon/models/dto_update_user_request.py` |
| `ResourceUser` | `verizon/models/resource_user.py` |
| `SensorInsightsUpdateUserRequestErrorBody` | `verizon/errors/sensor_insights_update_user_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

