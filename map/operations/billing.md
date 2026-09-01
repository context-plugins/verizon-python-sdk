<!-- Generated file — do not edit; regenerated with the SDK. -->

# Billing — operations

Accessor: `client.billing` · Source: `verizon/apis/billing.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.billing.add_account

- **Route**: `POST /managedaccounts/actions/add`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def add_account(body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ManagedAccountsAddResponse`
- **Returns (raw)**: `ApiResult[ManagedAccountsAddResponse, AddAccountErrorBody]`
- **Error**: `AddAccountErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManagedAccountsAddRequest` | `verizon/models/managed_accounts_add_request.py` |
| `ManagedAccountsAddRequestDict` | `verizon/models/managed_accounts_add_request.py` |
| `ManagedAccountsAddResponse` | `verizon/models/managed_accounts_add_response.py` |
| `AddAccountErrorBody` | `verizon/errors/add_account_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.billing.cancel_managed_account_action

- **Route**: `POST /managedaccounts/actions/cancel`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def cancel_managed_account_action(body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ManagedAccountCancelResponse`
- **Returns (raw)**: `ApiResult[ManagedAccountCancelResponse, CancelManagedAccountActionErrorBody]`
- **Error**: `CancelManagedAccountActionErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManagedAccountCancelRequest` | `verizon/models/managed_account_cancel_request.py` |
| `ManagedAccountCancelRequestDict` | `verizon/models/managed_account_cancel_request.py` |
| `ManagedAccountCancelResponse` | `verizon/models/managed_account_cancel_response.py` |
| `CancelManagedAccountActionErrorBody` | `verizon/errors/cancel_managed_account_action_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.billing.list_managed_account

- **Route**: `GET /managedaccounts/{accountName}/service/{serviceName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def list_managed_account(account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `service_name`
- **Params**: `account_name` — path `accountName` · `service_name` — path `serviceName`
- **Returns (parsed)**: `ManagedAccountsGetAllResponse`
- **Returns (raw)**: `ApiResult[ManagedAccountsGetAllResponse, ListManagedAccountErrorBody]`
- **Error**: `ListManagedAccountErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManagedAccountsGetAllResponse` | `verizon/models/managed_accounts_get_all_response.py` |
| `ListManagedAccountErrorBody` | `verizon/errors/list_managed_account_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.billing.managed_account_action

- **Route**: `POST /managedaccounts/actions/provision`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def managed_account_action(body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ManagedAccountsProvisionResponse`
- **Returns (raw)**: `ApiResult[ManagedAccountsProvisionResponse, ManagedAccountActionErrorBody]`
- **Error**: `ManagedAccountActionErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ManagedAccountsProvisionRequest` | `verizon/models/managed_accounts_provision_request.py` |
| `ManagedAccountsProvisionRequestDict` | `verizon/models/managed_accounts_provision_request.py` |
| `ManagedAccountsProvisionResponse` | `verizon/models/managed_accounts_provision_response.py` |
| `ManagedAccountActionErrorBody` | `verizon/errors/managed_account_action_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

