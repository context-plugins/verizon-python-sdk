<!-- Generated file — do not edit; regenerated with the SDK. -->

# DevicesLocationSubscriptions — operations

Accessor: `client.devices_location_subscriptions` · Source: `verizon/apis/devices_location_subscriptions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.devices_location_subscriptions.get_location_service_subscription_status

- **Route**: `GET /subscriptions/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def get_location_service_subscription_status(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `DeviceLocationSubscription`
- **Returns (raw)**: `ApiResult[DeviceLocationSubscription, GetLocationServiceSubscriptionStatusErrorBody]`
- **Error**: `GetLocationServiceSubscriptionStatusErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceLocationSubscription` | `verizon/models/device_location_subscription.py` |
| `GetLocationServiceSubscriptionStatusErrorBody` | `verizon/errors/get_location_service_subscription_status_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

### client.devices_location_subscriptions.get_location_service_usage

- **Route**: `POST /usage`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def get_location_service_usage(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetLocationServiceUsageErrorBody]`
- **Error**: `GetLocationServiceUsageErrorBody` — **Case A (typed)**
- **Error arms**: `DeviceLocationResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetLocationServiceUsageErrorBody` | `verizon/errors/get_location_service_usage_error.py` |
| `DeviceLocationResult` | `verizon/models/device_location_result.py` |

