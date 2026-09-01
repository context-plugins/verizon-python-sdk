<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `api_endpoints_for_5_g_business_internet_5_g_bi/client.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.business_internet_serviceplanchange

- **Route**: `PUT /actions/plan`
- **Auth**: `thingspace_oauth` OR `vz_m2m_session_token`
- **Server**: `o_auth_server`
- **Signature**: `def business_internet_serviceplanchange(body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GbiRequestResponse5`
- **Returns (raw)**: `ApiResult[GbiRequestResponse5, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GbichangeRequest5` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbichange_request5.py` |
| `GbichangeRequest5Dict` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbichange_request5.py` |
| `GbiRequestResponse5` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbi_request_response5.py` |

### client.business_internetactivate_using_post

- **Route**: `POST /actions/activate`
- **Auth**: `thingspace_oauth` OR `vz_m2m_session_token`
- **Server**: `o_auth_server`
- **Signature**: `def business_internetactivate_using_post(body: GbiactivateRequest5 | GbiactivateRequest5Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GbiRequestResponse5`
- **Returns (raw)**: `ApiResult[GbiRequestResponse5, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GbiactivateRequest5` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbiactivate_request5.py` |
| `GbiactivateRequest5Dict` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbiactivate_request5.py` |
| `GbiRequestResponse5` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbi_request_response5.py` |

### client.business_internetlist_device_information

- **Route**: `POST /actions/list`
- **Auth**: `thingspace_oauth` OR `vz_m2m_session_token`
- **Server**: `o_auth_server`
- **Signature**: `def business_internetlist_device_information(body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GbideviceDetailsresponse5`
- **Returns (raw)**: `ApiResult[GbideviceDetailsresponse5, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GbideviceId5` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_id5.py` |
| `GbideviceId5Dict` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_id5.py` |
| `GbideviceDetailsresponse5` | `api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_detailsresponse5.py` |

