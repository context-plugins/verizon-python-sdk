<!-- Generated file — do not edit; regenerated with the SDK. -->

# HplDeviceManagement — operations

Accessor: `client.hpl_device_management` · Source: `verizon/apis/hpl_device_management.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.hpl_device_management.add_devices_hyper_precise

- **Route**: `POST /devices/actions/add`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_location`
- **Signature**: `def add_devices_hyper_precise(body: HplAddDevicesRequest | HplAddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[HplAddDevicesRequest]`
- **Returns (raw)**: `ApiResult[list[HplAddDevicesRequest], AddDevicesHyperPreciseErrorBody]`
- **Error**: `AddDevicesHyperPreciseErrorBody` — **Case A (typed)**
- **Error arms**: `HyperPreciseLocationResult` [400, 401, 403, 404, 405, 406, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `HplAddDevicesRequest` | `verizon/models/hpl_add_devices_request.py` |
| `HplAddDevicesRequestDict` | `verizon/models/hpl_add_devices_request.py` |
| `AddDevicesHyperPreciseErrorBody` | `verizon/errors/add_devices_hyper_precise_error.py` |
| `HyperPreciseLocationResult` | `verizon/models/hyper_precise_location_result.py` |

