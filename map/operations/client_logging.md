<!-- Generated file — do not edit; regenerated with the SDK. -->

# ClientLogging — operations

Accessor: `client.client_logging` · Source: `verizon/apis/client_logging.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.client_logging.disable_device_logging

- **Route**: `DELETE /logging/{account}/devices/{deviceId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def disable_device_logging(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_id`
- **Params**: `account` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DisableDeviceLoggingErrorBody]`
- **Error**: `DisableDeviceLoggingErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisableDeviceLoggingErrorBody` | `verizon/errors/disable_device_logging_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.client_logging.disable_logging_for_devices

- **Route**: `DELETE /logging/{account}/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def disable_logging_for_devices(account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_ids`
- **Params**: `account` — path · `device_ids` — query `deviceIds`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DisableLoggingForDevicesErrorBody]`
- **Error**: `DisableLoggingForDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisableLoggingForDevicesErrorBody` | `verizon/errors/disable_logging_for_devices_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.client_logging.enable_device_logging

- **Route**: `PUT /logging/{account}/devices/{deviceId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def enable_device_logging(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_id`
- **Params**: `account` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `DeviceLoggingStatus`
- **Returns (raw)**: `ApiResult[DeviceLoggingStatus, EnableDeviceLoggingErrorBody]`
- **Error**: `EnableDeviceLoggingErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLoggingStatus` | `verizon/models/device_logging_status.py` |
| `EnableDeviceLoggingErrorBody` | `verizon/errors/enable_device_logging_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.client_logging.enable_logging_for_devices

- **Route**: `PUT /logging/{account}/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def enable_logging_for_devices(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `list[DeviceLoggingStatus]`
- **Returns (raw)**: `ApiResult[list[DeviceLoggingStatus], EnableLoggingForDevicesErrorBody]`
- **Error**: `EnableLoggingForDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLoggingStatus` | `verizon/models/device_logging_status.py` |
| `EnableLoggingForDevicesErrorBody` | `verizon/errors/enable_logging_for_devices_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.client_logging.list_device_logs

- **Route**: `GET /logging/{account}/devices/{deviceId}/logs`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def list_device_logs(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_id`
- **Params**: `account` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `list[DeviceLog]`
- **Returns (raw)**: `ApiResult[list[DeviceLog], ListDeviceLogsErrorBody]`
- **Error**: `ListDeviceLogsErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLog` | `verizon/models/device_log.py` |
| `ListDeviceLogsErrorBody` | `verizon/errors/list_device_logs_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.client_logging.list_devices_with_logging_enabled

- **Route**: `GET /logging/{account}/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def list_devices_with_logging_enabled(account: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`
- **Params**: `account` — path
- **Returns (parsed)**: `list[DeviceLoggingStatus]`
- **Returns (raw)**: `ApiResult[list[DeviceLoggingStatus], ListDevicesWithLoggingEnabledErrorBody]`
- **Error**: `ListDevicesWithLoggingEnabledErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLoggingStatus` | `verizon/models/device_logging_status.py` |
| `ListDevicesWithLoggingEnabledErrorBody` | `verizon/errors/list_devices_with_logging_enabled_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

