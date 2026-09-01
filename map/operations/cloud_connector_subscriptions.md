<!-- Generated file — do not edit; regenerated with the SDK. -->

# CloudConnectorSubscriptions — operations

Accessor: `client.cloud_connector_subscriptions` · Source: `verizon/apis/cloud_connector_subscriptions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cloud_connector_subscriptions.create_subscription

- **Route**: `POST /subscriptions`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def create_subscription(body: CreateSubscriptionRequest | CreateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Subscription`
- **Returns (raw)**: `ApiResult[Subscription, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateSubscriptionRequest` | `verizon/models/create_subscription_request.py` |
| `CreateSubscriptionRequestDict` | `verizon/models/create_subscription_request.py` |
| `Subscription` | `verizon/models/subscription.py` |

### client.cloud_connector_subscriptions.delete_subscription

- **Route**: `POST /subscriptions/actions/delete`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def delete_subscription(body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteSubscriptionRequest` | `verizon/models/delete_subscription_request.py` |
| `DeleteSubscriptionRequestDict` | `verizon/models/delete_subscription_request.py` |

### client.cloud_connector_subscriptions.query_subscription

- **Route**: `POST /subscriptions/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `cloud_connector`
- **Signature**: `def query_subscription(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[Subscription]`
- **Returns (raw)**: `ApiResult[list[Subscription], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `QuerySubscriptionRequest` | `verizon/models/query_subscription_request.py` |
| `QuerySubscriptionRequestDict` | `verizon/models/query_subscription_request.py` |
| `Subscription` | `verizon/models/subscription.py` |

