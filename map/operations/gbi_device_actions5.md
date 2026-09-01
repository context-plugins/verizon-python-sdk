<!-- Generated file — do not edit; regenerated with the SDK. -->

# GbiDeviceActions5 — operations

Accessor: `client.gbi_device_actions5` · Source: `verizon/apis/gbi_device_actions5.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.gbi_device_actions5.business_internet_serviceplanchange

- **Route**: `PUT /actions/plan`
- **Auth**: `thingspace_oauth` OR `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def business_internet_serviceplanchange(body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GbiRequestResponse5`
- **Returns (raw)**: `ApiResult[GbiRequestResponse5, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GbichangeRequest5` | `verizon/models/gbichange_request5.py` |
| `GbichangeRequest5Dict` | `verizon/models/gbichange_request5.py` |
| `GbiRequestResponse5` | `verizon/models/gbi_request_response5.py` |

### client.gbi_device_actions5.business_internetactivate_using_post

- **Route**: `POST /actions/activate`
- **Auth**: `thingspace_oauth` OR `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def business_internetactivate_using_post(body: GbiactivateRequest5 | GbiactivateRequest5Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GbiRequestResponse5`
- **Returns (raw)**: `ApiResult[GbiRequestResponse5, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GbiactivateRequest5` | `verizon/models/gbiactivate_request5.py` |
| `GbiactivateRequest5Dict` | `verizon/models/gbiactivate_request5.py` |
| `GbiRequestResponse5` | `verizon/models/gbi_request_response5.py` |

### client.gbi_device_actions5.business_internetlist_device_information

- **Route**: `POST /actions/list`
- **Auth**: `thingspace_oauth` OR `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def business_internetlist_device_information(body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GbideviceDetailsresponse5`
- **Returns (raw)**: `ApiResult[GbideviceDetailsresponse5, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GbideviceId5` | `verizon/models/gbidevice_id5.py` |
| `GbideviceId5Dict` | `verizon/models/gbidevice_id5.py` |
| `GbideviceDetailsresponse5` | `verizon/models/gbidevice_detailsresponse5.py` |

