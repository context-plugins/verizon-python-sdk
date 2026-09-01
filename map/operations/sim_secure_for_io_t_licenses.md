<!-- Generated file — do not edit; regenerated with the SDK. -->

# SimSecureForIoTLicenses — operations

Accessor: `client.sim_secure_for_io_t_licenses` · Source: `verizon/apis/sim_secure_for_io_t_licenses.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sim_secure_for_io_t_licenses.assign_license_to_devices

- **Route**: `POST /v1/devices/license/actions/assign`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `m2_m`
- **Signature**: `def assign_license_to_devices(body: AssignLicenseRequest | AssignLicenseRequestDict, *, x_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `x_request_id` — header `X-Request-ID` · `body` — JSON body
- **Returns (parsed)**: `SecuritySuccessResult`
- **Returns (raw)**: `ApiResult[SecuritySuccessResult, AssignLicenseToDevicesErrorBody]`
- **Error**: `AssignLicenseToDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `SecurityResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AssignLicenseRequest` | `verizon/models/assign_license_request.py` |
| `AssignLicenseRequestDict` | `verizon/models/assign_license_request.py` |
| `SecuritySuccessResult` | `verizon/models/security_success_result.py` |
| `AssignLicenseToDevicesErrorBody` | `verizon/errors/assign_license_to_devices_error.py` |
| `SecurityResult` | `verizon/models/security_result.py` |

### client.sim_secure_for_io_t_licenses.unassign_license_to_devices

- **Route**: `DELETE /v1/devices/license/actions/assign`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `m2_m`
- **Signature**: `def unassign_license_to_devices(x_request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `x_request_id`
- **Params**: `x_request_id` — header `X-Request-ID`
- **Returns (parsed)**: `SecuritySuccessResult`
- **Returns (raw)**: `ApiResult[SecuritySuccessResult, UnassignLicenseToDevicesErrorBody]`
- **Error**: `UnassignLicenseToDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `SecurityResult` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SecuritySuccessResult` | `verizon/models/security_success_result.py` |
| `UnassignLicenseToDevicesErrorBody` | `verizon/errors/unassign_license_to_devices_error.py` |
| `SecurityResult` | `verizon/models/security_result.py` |

