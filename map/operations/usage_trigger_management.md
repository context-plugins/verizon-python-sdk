<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsageTriggerManagement — operations

Accessor: `client.usage_trigger_management` · Source: `verizon/apis/usage_trigger_management.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.usage_trigger_management.create_new_trigger

- **Route**: `POST /usage/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def create_new_trigger(*, body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UsageTriggerResponse`
- **Returns (raw)**: `ApiResult[UsageTriggerResponse, CreateNewTriggerErrorBody]`
- **Error**: `CreateNewTriggerErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsageTriggerAddRequest` | `verizon/models/usage_trigger_add_request.py` |
| `UsageTriggerAddRequestDict` | `verizon/models/usage_trigger_add_request.py` |
| `UsageTriggerResponse` | `verizon/models/usage_trigger_response.py` |
| `CreateNewTriggerErrorBody` | `verizon/errors/create_new_trigger_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.usage_trigger_management.delete_trigger

- **Route**: `DELETE /usage/accounts/{accountName}/triggers/{triggerId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def delete_trigger(account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `trigger_id`
- **Params**: `account_name` — path `accountName` · `trigger_id` — path `triggerId`
- **Returns (parsed)**: `DeviceLocationSuccessResult`
- **Returns (raw)**: `ApiResult[DeviceLocationSuccessResult, DeleteTriggerErrorBody]`
- **Error**: `DeleteTriggerErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLocationSuccessResult` | `verizon/models/device_location_success_result.py` |
| `DeleteTriggerErrorBody` | `verizon/errors/delete_trigger_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.usage_trigger_management.update_trigger

- **Route**: `POST /usage/triggers/{triggerId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `subscription_server`
- **Signature**: `def update_trigger(trigger_id: str, *, body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trigger_id`
- **Params**: `trigger_id` — path `triggerId` · `body` — JSON body
- **Returns (parsed)**: `UsageTriggerResponse`
- **Returns (raw)**: `ApiResult[UsageTriggerResponse, UpdateTriggerErrorBody]`
- **Error**: `UpdateTriggerErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsageTriggerUpdateRequest` | `verizon/models/usage_trigger_update_request.py` |
| `UsageTriggerUpdateRequestDict` | `verizon/models/usage_trigger_update_request.py` |
| `UsageTriggerResponse` | `verizon/models/usage_trigger_response.py` |
| `UpdateTriggerErrorBody` | `verizon/errors/update_trigger_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

