<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountDevices — operations

Accessor: `client.account_devices` · Source: `verizon/apis/account_devices.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_devices.get_account_device_information

- **Route**: `GET /devices/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def get_account_device_information(acc: str, *, last_seen_device_id: str | None = None, protocol: DevicesProtocolOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`
- **Params**: `acc` — path · `last_seen_device_id` — query `lastSeenDeviceId` · `protocol` — query
- **Returns (parsed)**: `V3AccountDeviceList`
- **Returns (raw)**: `ApiResult[V3AccountDeviceList, GetAccountDeviceInformationErrorBody]`
- **Error**: `GetAccountDeviceInformationErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DevicesProtocolOrStr` | `verizon/models/enums/devices_protocol.py` |
| `V3AccountDeviceList` | `verizon/models/v3_account_device_list.py` |
| `GetAccountDeviceInformationErrorBody` | `verizon/errors/get_account_device_information_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

### client.account_devices.list_account_devices_information

- **Route**: `POST /devices/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v3`
- **Signature**: `def list_account_devices_information(acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `body`
- **Params**: `acc` — path · `body` — JSON body
- **Returns (parsed)**: `DeviceListResult`
- **Returns (raw)**: `ApiResult[DeviceListResult, ListAccountDevicesInformationErrorBody]`
- **Error**: `ListAccountDevicesInformationErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV3Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceImei` | `verizon/models/device_imei.py` |
| `DeviceImeiDict` | `verizon/models/device_imei.py` |
| `DeviceListResult` | `verizon/models/device_list_result.py` |
| `ListAccountDevicesInformationErrorBody` | `verizon/errors/list_account_devices_information_error.py` |
| `FotaV3Result` | `verizon/models/fota_v3_result.py` |

