<!-- Generated file — do not edit; regenerated with the SDK. -->

# RetrieveTheTriggers — operations

Accessor: `client.retrieve_the_triggers` · Source: `verizon/apis/retrieve_the_triggers.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.retrieve_the_triggers.get_all_available_triggers

- **Route**: `GET /m2m/v2/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_all_available_triggers(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TriggerValueResponse`
- **Returns (raw)**: `ApiResult[TriggerValueResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TriggerValueResponse` | `verizon/models/trigger_value_response.py` |

### client.retrieve_the_triggers.get_all_triggers_by_account_name

- **Route**: `GET /m2m/v2/triggers/accounts/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_all_triggers_by_account_name(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `TriggerValueResponse`
- **Returns (raw)**: `ApiResult[TriggerValueResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TriggerValueResponse` | `verizon/models/trigger_value_response.py` |

### client.retrieve_the_triggers.get_all_triggers_by_trigger_category

- **Route**: `GET /m2m/v2/triggers/categories/PromoAlerts`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_all_triggers_by_trigger_category(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TriggerValueResponse2`
- **Returns (raw)**: `ApiResult[TriggerValueResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TriggerValueResponse2` | `verizon/models/trigger_value_response2.py` |

### client.retrieve_the_triggers.get_triggers_by_id

- **Route**: `GET /m2m/v2/triggers/{triggerId}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_triggers_by_id(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `trigger_id`
- **Params**: `trigger_id` — path `triggerId`
- **Returns (parsed)**: `TriggerValueResponse2`
- **Returns (raw)**: `ApiResult[TriggerValueResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TriggerValueResponse2` | `verizon/models/trigger_value_response2.py` |

