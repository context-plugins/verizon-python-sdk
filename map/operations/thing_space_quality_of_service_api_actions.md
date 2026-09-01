<!-- Generated file — do not edit; regenerated with the SDK. -->

# ThingSpaceQualityOfServiceApiActions — operations

Accessor: `client.thing_space_quality_of_service_api_actions` · Source: `verizon/apis/thing_space_quality_of_service_api_actions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.thing_space_quality_of_service_api_actions.create_a_thing_space_quality_of_service_api_subscription

- **Route**: `POST /m2m/v1/devices/actions/enhanceQoS`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def create_a_thing_space_quality_of_service_api_subscription(body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Success201`
- **Returns (raw)**: `ApiResult[Success201, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SubscribeRequest` | `verizon/models/subscribe_request.py` |
| `SubscribeRequestDict` | `verizon/models/subscribe_request.py` |
| `Success201` | `verizon/models/success201.py` |

### client.thing_space_quality_of_service_api_actions.stop_a_thing_space_quality_of_service_api_subscription

- **Route**: `DELETE /m2m/v1/devices/actions/enhanceQoS`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def stop_a_thing_space_quality_of_service_api_subscription(account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `qos_subscription_id`
- **Params**: `account_name` — query `accountName` · `qos_subscription_id` — query `qosSubscriptionId`
- **Returns (parsed)**: `Success201`
- **Returns (raw)**: `ApiResult[Success201, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Success201` | `verizon/models/success201.py` |

