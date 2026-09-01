<!-- Generated file — do not edit; regenerated with the SDK. -->

# RetrieveRatePlanList — operations

Accessor: `client.retrieve_rate_plan_list` · Source: `verizon/apis/retrieve_rate_plan_list.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.retrieve_rate_plan_list.get_rate_plan_list

- **Route**: `GET /v2/triggers/rateplanlist/{ecpdId}`
- **Auth**: `thingspace_oauth1` OR `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_rate_plan_list(ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ecpd_id`
- **Params**: `ecpd_id` — path `ecpdId`
- **Returns (parsed)**: `Rateplan`
- **Returns (raw)**: `ApiResult[Rateplan, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Rateplan` | `verizon/models/rateplan.py` |

