<!-- Generated file — do not edit; regenerated with the SDK. -->

# SessionManagement — operations

Accessor: `client.session_management` · Source: `verizon/apis/session_management.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.session_management.end_connectivity_management_session

- **Route**: `POST /m2m/v1/session/logout`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def end_connectivity_management_session(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `LogOutRequest`
- **Returns (raw)**: `ApiResult[LogOutRequest, EndConnectivityManagementSessionErrorBody]`
- **Error**: `EndConnectivityManagementSessionErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LogOutRequest` | `verizon/models/log_out_request.py` |
| `EndConnectivityManagementSessionErrorBody` | `verizon/errors/end_connectivity_management_session_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.session_management.reset_connectivity_management_password

- **Route**: `PUT /m2m/v1/session/password/actions/reset`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def reset_connectivity_management_password(body: SessionResetPasswordRequest | SessionResetPasswordRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SessionResetPasswordResult`
- **Returns (raw)**: `ApiResult[SessionResetPasswordResult, ResetConnectivityManagementPasswordErrorBody]`
- **Error**: `ResetConnectivityManagementPasswordErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SessionResetPasswordRequest` | `verizon/models/session_reset_password_request.py` |
| `SessionResetPasswordRequestDict` | `verizon/models/session_reset_password_request.py` |
| `SessionResetPasswordResult` | `verizon/models/session_reset_password_result.py` |
| `ResetConnectivityManagementPasswordErrorBody` | `verizon/errors/reset_connectivity_management_password_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.session_management.start_connectivity_management_session

- **Route**: `POST /m2m/v1/session/login`
- **Auth**: `thingspace_oauth`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def start_connectivity_management_session(*, body: LogInRequest | LogInRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LogInResult`
- **Returns (raw)**: `ApiResult[LogInResult, StartConnectivityManagementSessionErrorBody]`
- **Error**: `StartConnectivityManagementSessionErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LogInRequest` | `verizon/models/log_in_request.py` |
| `LogInRequestDict` | `verizon/models/log_in_request.py` |
| `LogInResult` | `verizon/models/log_in_result.py` |
| `StartConnectivityManagementSessionErrorBody` | `verizon/errors/start_connectivity_management_session_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

