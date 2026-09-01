<!-- Generated file — do not edit; regenerated with the SDK. -->

# Pwn — operations

Accessor: `client.pwn` · Source: `verizon/apis/pwn.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.pwn.change_pwn_device_i_paddress

- **Route**: `PUT /m2m/v1/devices/pwn/actions/ipaddress`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def change_pwn_device_i_paddress(body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ChangePwndeviceIpaddressResponse`
- **Returns (raw)**: `ApiResult[ChangePwndeviceIpaddressResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChangePwndeviceIpaddressRequest` | `verizon/models/change_pwndevice_ipaddress_request.py` |
| `ChangePwndeviceIpaddressRequestDict` | `verizon/models/change_pwndevice_ipaddress_request.py` |
| `ChangePwndeviceIpaddressResponse` | `verizon/models/change_pwndevice_ipaddress_response.py` |

### client.pwn.change_pwn_device_profile

- **Route**: `POST /m2m/v1/devices/pwn/actions/profile`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def change_pwn_device_profile(body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ChangePwndeviceProfileResponse`
- **Returns (raw)**: `ApiResult[ChangePwndeviceProfileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChangePwndeviceProfileRequest` | `verizon/models/change_pwndevice_profile_request.py` |
| `ChangePwndeviceProfileRequestDict` | `verizon/models/change_pwndevice_profile_request.py` |
| `ChangePwndeviceProfileResponse` | `verizon/models/change_pwndevice_profile_response.py` |

### client.pwn.change_pwn_device_state_activate

- **Route**: `POST /m2m/v1/devices/pwn/actions/state/activate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def change_pwn_device_state_activate(body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ChangePwndeviceStateResponse`
- **Returns (raw)**: `ApiResult[ChangePwndeviceStateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChangePwndeviceStateActivateRequest` | `verizon/models/change_pwndevice_state_activate_request.py` |
| `ChangePwndeviceStateActivateRequestDict` | `verizon/models/change_pwndevice_state_activate_request.py` |
| `ChangePwndeviceStateResponse` | `verizon/models/change_pwndevice_state_response.py` |

### client.pwn.change_pwn_device_state_deactivate

- **Route**: `POST /m2m/v1/devices/pwn/actions/state/deactivate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def change_pwn_device_state_deactivate(body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ChangePwndeviceStateResponse`
- **Returns (raw)**: `ApiResult[ChangePwndeviceStateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChangePwndeviceStateDeactivateRequest` | `verizon/models/change_pwndevice_state_deactivate_request.py` |
| `ChangePwndeviceStateDeactivateRequestDict` | `verizon/models/change_pwndevice_state_deactivate_request.py` |
| `ChangePwndeviceStateResponse` | `verizon/models/change_pwndevice_state_response.py` |

### client.pwn.get_pwn_performance_consent

- **Route**: `GET /m2m/v1/devices/pwn/performance/consent/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_pwn_performance_consent(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `GetPwnperformanceConsentResponse`
- **Returns (raw)**: `ApiResult[GetPwnperformanceConsentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetPwnperformanceConsentResponse` | `verizon/models/get_pwnperformance_consent_response.py` |

### client.pwn.get_profile_list

- **Route**: `GET /m2m/v1/devices/pwn/profiles/list/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_profile_list(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `PwnprofileList`
- **Returns (raw)**: `ApiResult[PwnprofileList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PwnprofileList` | `verizon/models/pwnprofile_list.py` |

### client.pwn.kpi_list

- **Route**: `GET /m2m/v1/devices/pwn/kpi/list/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def kpi_list(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `KpiinfoList`
- **Returns (raw)**: `ApiResult[KpiinfoList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `KpiinfoList` | `verizon/models/kpiinfo_list.py` |

