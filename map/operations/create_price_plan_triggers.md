<!-- Generated file — do not edit; regenerated with the SDK. -->

# CreatePricePlanTriggers — operations

Accessor: `client.create_price_plan_triggers` · Source: `verizon/apis/create_price_plan_triggers.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.create_price_plan_triggers.create_trigger_rules

- **Route**: `POST /v2/triggers`
- **Auth**: `thingspace_oauth1` OR `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def create_trigger_rules(body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TriggerResponse`
- **Returns (raw)**: `ApiResult[TriggerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V2TriggersRequest` | `verizon/models/unions/v2_triggers_request.py` |
| `V2TriggersRequestDict` | `verizon/models/unions/v2_triggers_request.py` |
| `TriggerResponse` | `verizon/models/trigger_response.py` |

