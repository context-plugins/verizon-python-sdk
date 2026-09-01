<!-- Generated file — do not edit; regenerated with the SDK. -->

# UpdateTriggers — operations

Accessor: `client.update_triggers` · Source: `verizon/apis/update_triggers.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.update_triggers.update_all_available_triggers

- **Route**: `PUT /m2m/v2/triggers`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_all_available_triggers(*, body: RequestTrigger | RequestTriggerDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SuccessModel`
- **Returns (raw)**: `ApiResult[SuccessModel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RequestTrigger` | `verizon/models/request_trigger.py` |
| `RequestTriggerDict` | `verizon/models/request_trigger.py` |
| `SuccessModel` | `verizon/models/success_model.py` |

