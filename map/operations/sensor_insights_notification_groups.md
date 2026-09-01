<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsNotificationGroups — operations

Accessor: `client.sensor_insights_notification_groups` · Source: `verizon/apis/sensor_insights_notification_groups.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_notification_groups.sensor_insights_add_users_to_notification_group_request

- **Route**: `POST /dm/v1/notificationGroups/actions/add-users`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_add_users_to_notification_group_request(body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SensorInsightsAddUsersToNotificationGroupRequestErrorBody]`
- **Error**: `SensorInsightsAddUsersToNotificationGroupRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoAddUsersToNotificationGroupRequest` | `verizon/models/dto_add_users_to_notification_group_request.py` |
| `DtoAddUsersToNotificationGroupRequestDict` | `verizon/models/dto_add_users_to_notification_group_request.py` |
| `SensorInsightsAddUsersToNotificationGroupRequestErrorBody` | `verizon/errors/sensor_insights_add_users_to_notification_group_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_notification_groups.sensor_insights_create_notification_group_request

- **Route**: `POST /dm/v1/notificationGroups`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_create_notification_group_request(body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoNotificationGroupResponseEntity`
- **Returns (raw)**: `ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsCreateNotificationGroupRequestErrorBody]`
- **Error**: `SensorInsightsCreateNotificationGroupRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoCreateNotificationGroupRequest` | `verizon/models/dto_create_notification_group_request.py` |
| `DtoCreateNotificationGroupRequestDict` | `verizon/models/dto_create_notification_group_request.py` |
| `DtoNotificationGroupResponseEntity` | `verizon/models/dto_notification_group_response_entity.py` |
| `SensorInsightsCreateNotificationGroupRequestErrorBody` | `verizon/errors/sensor_insights_create_notification_group_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_notification_groups.sensor_insights_delete_notification_group

- **Route**: `DELETE /dm/v1/notificationGroups`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_delete_notification_group(payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payload`
- **Params**: `payload` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SensorInsightsDeleteNotificationGroupErrorBody]`
- **Error**: `SensorInsightsDeleteNotificationGroupErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError404` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoDeleteNotificationGroupRequest` | `verizon/models/dto_delete_notification_group_request.py` |
| `DtoDeleteNotificationGroupRequestDict` | `verizon/models/dto_delete_notification_group_request.py` |
| `SensorInsightsDeleteNotificationGroupErrorBody` | `verizon/errors/sensor_insights_delete_notification_group_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |

### client.sensor_insights_notification_groups.sensor_insights_list_notification_group_request

- **Route**: `POST /dm/v1/notificationGroups/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_notification_group_request(body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DtoNotificationGroupResponseEntity]`
- **Returns (raw)**: `ApiResult[list[DtoNotificationGroupResponseEntity], SensorInsightsListNotificationGroupRequestErrorBody]`
- **Error**: `SensorInsightsListNotificationGroupRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListNotificationGroupRequest` | `verizon/models/dto_list_notification_group_request.py` |
| `DtoListNotificationGroupRequestDict` | `verizon/models/dto_list_notification_group_request.py` |
| `DtoNotificationGroupResponseEntity` | `verizon/models/dto_notification_group_response_entity.py` |
| `SensorInsightsListNotificationGroupRequestErrorBody` | `verizon/errors/sensor_insights_list_notification_group_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_notification_groups.sensor_insights_remove_users_from_notification_group_request

- **Route**: `POST /dm/v1/notificationGroups/actions/remove-users`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_remove_users_from_notification_group_request(body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody]`
- **Error**: `SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoRemoveUsersFromNotificationGroupRequest` | `verizon/models/dto_remove_users_from_notification_group_request.py` |
| `DtoRemoveUsersFromNotificationGroupRequestDict` | `verizon/models/dto_remove_users_from_notification_group_request.py` |
| `SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody` | `verizon/errors/sensor_insights_remove_users_from_notification_group_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_notification_groups.sensor_insights_update_notification_group_request

- **Route**: `PATCH /dm/v1/notificationGroups`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_update_notification_group_request(body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoNotificationGroupResponseEntity`
- **Returns (raw)**: `ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsUpdateNotificationGroupRequestErrorBody]`
- **Error**: `SensorInsightsUpdateNotificationGroupRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoUpdateNotificationGroupRequest` | `verizon/models/dto_update_notification_group_request.py` |
| `DtoUpdateNotificationGroupRequestDict` | `verizon/models/dto_update_notification_group_request.py` |
| `DtoNotificationGroupResponseEntity` | `verizon/models/dto_notification_group_response_entity.py` |
| `SensorInsightsUpdateNotificationGroupRequestErrorBody` | `verizon/errors/sensor_insights_update_notification_group_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

