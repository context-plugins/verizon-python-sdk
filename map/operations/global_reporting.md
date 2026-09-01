<!-- Generated file — do not edit; regenerated with the SDK. -->

# GlobalReporting — operations

Accessor: `client.global_reporting` · Source: `verizon/apis/global_reporting.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.global_reporting.retrieve_global_list

- **Route**: `POST /m2m/v2/devices/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_global_list(body: ESimglobalDeviceList | ESimglobalDeviceListDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ESimrequestResponse`
- **Returns (raw)**: `ApiResult[ESimrequestResponse, RetrieveGlobalListErrorBody]`
- **Error**: `RetrieveGlobalListErrorBody` — **Case A (typed)**
- **Error arms**: `ESimrestErrorResponse` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ESimglobalDeviceList` | `verizon/models/e_simglobal_device_list.py` |
| `ESimglobalDeviceListDict` | `verizon/models/e_simglobal_device_list.py` |
| `ESimrequestResponse` | `verizon/models/e_simrequest_response.py` |
| `RetrieveGlobalListErrorBody` | `verizon/errors/retrieve_global_list_error.py` |
| `ESimrestErrorResponse` | `verizon/models/e_simrest_error_response.py` |

### client.global_reporting.deviceprovhistory_using_post

- **Route**: `POST /m2m/v2/devices/history/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def deviceprovhistory_using_post(body: ESimprovhistoryRequest | ESimprovhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ESimrequestResponse`
- **Returns (raw)**: `ApiResult[ESimrequestResponse, DeviceprovhistoryUsingPostErrorBody]`
- **Error**: `DeviceprovhistoryUsingPostErrorBody` — **Case A (typed)**
- **Error arms**: `ESimrestErrorResponse` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ESimprovhistoryRequest` | `verizon/models/e_simprovhistory_request.py` |
| `ESimprovhistoryRequestDict` | `verizon/models/e_simprovhistory_request.py` |
| `ESimrequestResponse` | `verizon/models/e_simrequest_response.py` |
| `DeviceprovhistoryUsingPostErrorBody` | `verizon/errors/deviceprovhistory_using_post_error.py` |
| `ESimrestErrorResponse` | `verizon/models/e_simrest_error_response.py` |

