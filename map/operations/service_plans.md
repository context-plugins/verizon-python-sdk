<!-- Generated file — do not edit; regenerated with the SDK. -->

# ServicePlans — operations

Accessor: `client.service_plans` · Source: `verizon/apis/service_plans.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.service_plans.list_account_service_plans

- **Route**: `GET /m2m/v1/plans/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_account_service_plans(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `list[ServicePlan]`
- **Returns (raw)**: `ApiResult[list[ServicePlan], ListAccountServicePlansErrorBody]`
- **Error**: `ListAccountServicePlansErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServicePlan` | `verizon/models/service_plan.py` |
| `ListAccountServicePlansErrorBody` | `verizon/errors/list_account_service_plans_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

