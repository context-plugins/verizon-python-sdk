<!-- Generated file — do not edit; regenerated with the SDK. -->

# CloudConnectorDevices — operations

Accessor: `client.cloud_connector_devices` · Source: `verizon/apis/cloud_connector_devices.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cloud_connector_devices.delete_device_from_account

- **Route**: `POST /devices/actions/delete`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def delete_device_from_account(body: RemoveDeviceRequest | RemoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RemoveDeviceRequest` | `verizon/models/remove_device_request.py` |
| `RemoveDeviceRequestDict` | `verizon/models/remove_device_request.py` |

### client.cloud_connector_devices.find_device_by_property_values

- **Route**: `POST /devices/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def find_device_by_property_values(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FindDeviceByPropertyResponseList`
- **Returns (raw)**: `ApiResult[FindDeviceByPropertyResponseList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `QuerySubscriptionRequest` | `verizon/models/query_subscription_request.py` |
| `QuerySubscriptionRequestDict` | `verizon/models/query_subscription_request.py` |
| `FindDeviceByPropertyResponseList` | `verizon/models/find_device_by_property_response_list.py` |

### client.cloud_connector_devices.search_device_event_history

- **Route**: `POST /devices/fields/actions/history/search`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def search_device_event_history(body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchDeviceEventHistoryResponseList`
- **Returns (raw)**: `ApiResult[SearchDeviceEventHistoryResponseList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchDeviceEventHistoryRequest` | `verizon/models/search_device_event_history_request.py` |
| `SearchDeviceEventHistoryRequestDict` | `verizon/models/search_device_event_history_request.py` |
| `SearchDeviceEventHistoryResponseList` | `verizon/models/search_device_event_history_response_list.py` |

### client.cloud_connector_devices.search_devices_resources_by_property_values

- **Route**: `POST /devices/actions/search`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def search_devices_resources_by_property_values(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchDeviceByPropertyResponseList`
- **Returns (raw)**: `ApiResult[SearchDeviceByPropertyResponseList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `QuerySubscriptionRequest` | `verizon/models/query_subscription_request.py` |
| `QuerySubscriptionRequestDict` | `verizon/models/query_subscription_request.py` |
| `SearchDeviceByPropertyResponseList` | `verizon/models/search_device_by_property_response_list.py` |

### client.cloud_connector_devices.search_sensor_readings

- **Route**: `POST /devices/fields/{fieldname}/actions/history`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def search_sensor_readings(fieldname: str, body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `fieldname`, `body`
- **Params**: `fieldname` — path · `body` — JSON body
- **Returns (parsed)**: `SearchSensorHistoryResponseList`
- **Returns (raw)**: `ApiResult[SearchSensorHistoryResponseList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchSensorHistoryRequest` | `verizon/models/search_sensor_history_request.py` |
| `SearchSensorHistoryRequestDict` | `verizon/models/search_sensor_history_request.py` |
| `SearchSensorHistoryResponseList` | `verizon/models/search_sensor_history_response_list.py` |

### client.cloud_connector_devices.update_devices_configuration_value

- **Route**: `POST /devices/configuration/actions/set`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def update_devices_configuration_value(body: ChangeConfigurationRequest | ChangeConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ChangeConfigurationResponse`
- **Returns (raw)**: `ApiResult[ChangeConfigurationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChangeConfigurationRequest` | `verizon/models/change_configuration_request.py` |
| `ChangeConfigurationRequestDict` | `verizon/models/change_configuration_request.py` |
| `ChangeConfigurationResponse` | `verizon/models/change_configuration_response.py` |

