<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsRules — operations

Accessor: `client.sensor_insights_rules` · Source: `verizon/apis/sensor_insights_rules.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_rules.sensor_insights_list_rules_request

- **Route**: `POST /dm/v1/rules/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_rules_request(body: DtoListRulesRequest | DtoListRulesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[ResourceRule]`
- **Returns (raw)**: `ApiResult[list[ResourceRule], SensorInsightsListRulesRequestErrorBody]`
- **Error**: `SensorInsightsListRulesRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListRulesRequest` | `verizon/models/dto_list_rules_request.py` |
| `DtoListRulesRequestDict` | `verizon/models/dto_list_rules_request.py` |
| `ResourceRule` | `verizon/models/resource_rule.py` |
| `SensorInsightsListRulesRequestErrorBody` | `verizon/errors/sensor_insights_list_rules_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_rules.sensor_insights_overwrite_rule_request

- **Route**: `POST /dm/v1/rules`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_overwrite_rule_request(body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ResourceRule`
- **Returns (raw)**: `ApiResult[ResourceRule, SensorInsightsOverwriteRuleRequestErrorBody]`
- **Error**: `SensorInsightsOverwriteRuleRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoOverwriteRuleRequest` | `verizon/models/dto_overwrite_rule_request.py` |
| `DtoOverwriteRuleRequestDict` | `verizon/models/dto_overwrite_rule_request.py` |
| `ResourceRule` | `verizon/models/resource_rule.py` |
| `SensorInsightsOverwriteRuleRequestErrorBody` | `verizon/errors/sensor_insights_overwrite_rule_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

