<!-- Generated file — do not edit; regenerated with the SDK. -->

# SimActions — operations

Accessor: `client.sim_actions` · Source: `verizon/apis/sim_actions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sim_actions.newactivatecode

- **Route**: `POST /m2m/v1/devices/profile/actions/renew_activation_code`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def newactivatecode(body: ESimprofileRequest2 | ESimprofileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ESimrequestResponse`
- **Returns (raw)**: `ApiResult[ESimrequestResponse, NewactivatecodeErrorBody]`
- **Error**: `NewactivatecodeErrorBody` — **Case A (typed)**
- **Error arms**: `ESimrestErrorResponse` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ESimprofileRequest2` | `verizon/models/e_simprofile_request2.py` |
| `ESimprofileRequest2Dict` | `verizon/models/e_simprofile_request2.py` |
| `ESimrequestResponse` | `verizon/models/e_simrequest_response.py` |
| `NewactivatecodeErrorBody` | `verizon/errors/newactivatecode_error.py` |
| `ESimrestErrorResponse` | `verizon/models/e_simrest_error_response.py` |

### client.sim_actions.setactivate_using_post

- **Route**: `POST /m2m/v1/devices/profile/actions/activate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def setactivate_using_post(body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ESimrequestResponse`
- **Returns (raw)**: `ApiResult[ESimrequestResponse, SetactivateUsingPostErrorBody]`
- **Error**: `SetactivateUsingPostErrorBody` — **Case A (typed)**
- **Error arms**: `ESimrestErrorResponse` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ESimprofileRequest` | `verizon/models/e_simprofile_request.py` |
| `ESimprofileRequestDict` | `verizon/models/e_simprofile_request.py` |
| `ESimrequestResponse` | `verizon/models/e_simrequest_response.py` |
| `SetactivateUsingPostErrorBody` | `verizon/errors/setactivate_using_post_error.py` |
| `ESimrestErrorResponse` | `verizon/models/e_simrest_error_response.py` |

### client.sim_actions.setdeactivate_using_post

- **Route**: `POST /m2m/v1/devices/profile/actions/deactivate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def setdeactivate_using_post(body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ESimrequestResponse`
- **Returns (raw)**: `ApiResult[ESimrequestResponse, SetdeactivateUsingPostErrorBody]`
- **Error**: `SetdeactivateUsingPostErrorBody` — **Case A (typed)**
- **Error arms**: `ESimrestErrorResponse` [400, 401, 403, 404, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProfileRequest2` | `verizon/models/profile_request2.py` |
| `ProfileRequest2Dict` | `verizon/models/profile_request2.py` |
| `ESimrequestResponse` | `verizon/models/e_simrequest_response.py` |
| `SetdeactivateUsingPostErrorBody` | `verizon/errors/setdeactivate_using_post_error.py` |
| `ESimrestErrorResponse` | `verizon/models/e_simrest_error_response.py` |

