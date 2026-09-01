<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountRequests — operations

Accessor: `client.account_requests` · Source: `verizon/apis/account_requests.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_requests.get_current_asynchronous_request_status

- **Route**: `GET /m2m/v1/accounts/{aname}/requests/{requestId}/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_current_asynchronous_request_status(aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`, `request_id`
- **Params**: `aname` — path · `request_id` — path `requestId`
- **Returns (parsed)**: `AsynchronousRequestResult`
- **Returns (raw)**: `ApiResult[AsynchronousRequestResult, GetCurrentAsynchronousRequestStatusErrorBody]`
- **Error**: `GetCurrentAsynchronousRequestStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AsynchronousRequestResult` | `verizon/models/asynchronous_request_result.py` |
| `GetCurrentAsynchronousRequestStatusErrorBody` | `verizon/errors/get_current_asynchronous_request_status_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

