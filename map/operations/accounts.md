<!-- Generated file — do not edit; regenerated with the SDK. -->

# Accounts — operations

Accessor: `client.accounts` · Source: `verizon/apis/accounts.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.accounts.get_account_information

- **Route**: `GET /m2m/v1/accounts/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_account_information(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `Account`
- **Returns (raw)**: `ApiResult[Account, GetAccountInformationErrorBody]`
- **Error**: `GetAccountInformationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Account` | `verizon/models/account.py` |
| `GetAccountInformationErrorBody` | `verizon/errors/get_account_information_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.accounts.list_account_leads

- **Route**: `GET /m2m/v1/leads/{aname}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_account_leads(aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path · `next` — query
- **Returns (parsed)**: `AccountLeadsResult`
- **Returns (raw)**: `ApiResult[AccountLeadsResult, ListAccountLeadsErrorBody]`
- **Error**: `ListAccountLeadsErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountLeadsResult` | `verizon/models/account_leads_result.py` |
| `ListAccountLeadsErrorBody` | `verizon/errors/list_account_leads_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.accounts.list_account_states_and_services

- **Route**: `GET /m2m/v1/accounts/{aname}/statesandservices`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_account_states_and_services(aname: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `aname`
- **Params**: `aname` — path
- **Returns (parsed)**: `AccountStatesAndServices`
- **Returns (raw)**: `ApiResult[AccountStatesAndServices, ListAccountStatesAndServicesErrorBody]`
- **Error**: `ListAccountStatesAndServicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountStatesAndServices` | `verizon/models/account_states_and_services.py` |
| `ListAccountStatesAndServicesErrorBody` | `verizon/errors/list_account_states_and_services_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

