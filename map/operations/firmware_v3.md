<!-- Generated file — do not edit; regenerated with the SDK. -->

# FirmwareV3 — operations

Accessor: `client.firmware_v3` · Source: `verizon/apis/firmware_v3.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.firmware_v3.list_available_firmware2

- **Route**: `GET /firmware/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def list_available_firmware2(acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `protocol`
- **Params**: `acc` — path · `protocol` — query
- **Returns (parsed)**: `list[FirmwarePackage]`
- **Returns (raw)**: `ApiResult[list[FirmwarePackage], ListAvailableFirmware2ErrorBody]`
- **Error**: `ListAvailableFirmware2ErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FirmwareProtocolOrStr` | `verizon/models/enums/firmware_protocol.py` |
| `FirmwarePackage` | `verizon/models/firmware_package.py` |
| `ListAvailableFirmware2ErrorBody` | `verizon/errors/list_available_firmware2_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.firmware_v3.report_device_firmware

- **Route**: `PUT /firmware/{acc}/async/{deviceId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def report_device_firmware(acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `device_id`
- **Params**: `acc` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `DeviceFirmwareVersionUpdateResult`
- **Returns (raw)**: `ApiResult[DeviceFirmwareVersionUpdateResult, ReportDeviceFirmwareErrorBody]`
- **Error**: `ReportDeviceFirmwareErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceFirmwareVersionUpdateResult` | `verizon/models/device_firmware_version_update_result.py` |
| `ReportDeviceFirmwareErrorBody` | `verizon/errors/report_device_firmware_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.firmware_v3.synchronize_device_firmware

- **Route**: `PUT /firmware/{acc}/devices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def synchronize_device_firmware(acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `DeviceFirmwareList`
- **Returns (raw)**: `ApiResult[DeviceFirmwareList, SynchronizeDeviceFirmwareErrorBody]`
- **Error**: `SynchronizeDeviceFirmwareErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FirmwareImei` | `verizon/models/firmware_imei.py` |
| `FirmwareImeiDict` | `verizon/models/firmware_imei.py` |
| `DeviceFirmwareList` | `verizon/models/device_firmware_list.py` |
| `SynchronizeDeviceFirmwareErrorBody` | `verizon/errors/synchronize_device_firmware_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

