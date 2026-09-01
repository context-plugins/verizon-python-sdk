<!-- Generated file — do not edit; regenerated with the SDK. -->

# Targets — operations

Accessor: `client.targets` · Source: `verizon/apis/targets.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.targets.create_azure_central_io_t_application

- **Route**: `POST /targets/actions/newaic`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def create_azure_central_io_t_application(billingaccount_id: str, body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `billingaccount_id`, `body`
- **Params**: `billingaccount_id` — header `BillingaccountID` · `body` — JSON body
- **Returns (parsed)**: `CreateIoTapplicationResponse`
- **Returns (raw)**: `ApiResult[CreateIoTapplicationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateIoTapplicationRequest` | `verizon/models/create_io_tapplication_request.py` |
| `CreateIoTapplicationRequestDict` | `verizon/models/create_io_tapplication_request.py` |
| `CreateIoTapplicationResponse` | `verizon/models/create_io_tapplication_response.py` |

### client.targets.create_target

- **Route**: `POST /targets`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def create_target(body: CreateTargetRequest | CreateTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Target`
- **Returns (raw)**: `ApiResult[Target, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTargetRequest` | `verizon/models/create_target_request.py` |
| `CreateTargetRequestDict` | `verizon/models/create_target_request.py` |
| `Target` | `verizon/models/target.py` |

### client.targets.delete_target

- **Route**: `POST /targets/actions/delete`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def delete_target(body: DeleteTargetRequest | DeleteTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteTargetRequest` | `verizon/models/delete_target_request.py` |
| `DeleteTargetRequestDict` | `verizon/models/delete_target_request.py` |

### client.targets.generate_target_external_id

- **Route**: `POST /targets/actions/newextid`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def generate_target_external_id(body: GenerateExternalIdrequest | GenerateExternalIdrequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenerateExternalIdresult`
- **Returns (raw)**: `ApiResult[GenerateExternalIdresult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateExternalIdrequest` | `verizon/models/generate_external_idrequest.py` |
| `GenerateExternalIdrequestDict` | `verizon/models/generate_external_idrequest.py` |
| `GenerateExternalIdresult` | `verizon/models/generate_external_idresult.py` |

### client.targets.query_target

- **Route**: `POST /targets/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def query_target(body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[Target]`
- **Returns (raw)**: `ApiResult[list[Target], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `QueryTargetRequest` | `verizon/models/query_target_request.py` |
| `QueryTargetRequestDict` | `verizon/models/query_target_request.py` |
| `Target` | `verizon/models/target.py` |

