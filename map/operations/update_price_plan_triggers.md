<!-- Generated file — do not edit; regenerated with the SDK. -->

# UpdatePricePlanTriggers — operations

Accessor: `client.update_price_plan_triggers` · Source: `verizon/apis/update_price_plan_triggers.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.update_price_plan_triggers.update_trigger_rules

- **Route**: `PUT /v2/triggers`
- **Auth**: `thingspace_oauth1` OR `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_trigger_rules(body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TriggerResponse`
- **Returns (raw)**: `ApiResult[TriggerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V2TriggersRequest1` | `verizon/models/unions/v2_triggers_request1.py` |
| `V2TriggersRequest1Dict` | `verizon/models/unions/v2_triggers_request1.py` |
| `TriggerResponse` | `verizon/models/trigger_response.py` |

