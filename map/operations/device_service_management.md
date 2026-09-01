<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceServiceManagement — operations

Accessor: `client.device_service_management` · Source: `verizon/apis/device_service_management.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_service_management.get_device_hyper_precise_status

- **Route**: `GET /devices/services`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def get_device_hyper_precise_status(imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `imei`, `account_number`
- **Params**: `imei` — query · `account_number` — query `accountNumber`
- **Returns (parsed)**: `BullseyeServiceResult`
- **Returns (raw)**: `ApiResult[BullseyeServiceResult, GetDeviceHyperPreciseStatusErrorBody]`
- **Error**: `GetDeviceHyperPreciseStatusErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BullseyeServiceResult` | `verizon/models/bullseye_service_result.py` |
| `GetDeviceHyperPreciseStatusErrorBody` | `verizon/errors/get_device_hyper_precise_status_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

### client.device_service_management.update_device_hyper_precise_status

- **Route**: `PUT /devices/services`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def update_device_hyper_precise_status(body: BullseyeServiceRequest | BullseyeServiceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BullseyeServiceResult`
- **Returns (raw)**: `ApiResult[BullseyeServiceResult, UpdateDeviceHyperPreciseStatusErrorBody]`
- **Error**: `UpdateDeviceHyperPreciseStatusErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BullseyeServiceRequest` | `verizon/models/bullseye_service_request.py` |
| `BullseyeServiceRequestDict` | `verizon/models/bullseye_service_request.py` |
| `BullseyeServiceResult` | `verizon/models/bullseye_service_result.py` |
| `UpdateDeviceHyperPreciseStatusErrorBody` | `verizon/errors/update_device_hyper_precise_status_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

