<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsGateways — operations

Accessor: `client.sensor_insights_gateways` · Source: `verizon/apis/sensor_insights_gateways.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_gateways.sensor_insights_list_gateway_devices_request

- **Route**: `POST /dm/v1/devices/gateways/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_gateway_devices_request(body: DtoListDevicesRequest | DtoListDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[ResourceDevice]`
- **Returns (raw)**: `ApiResult[list[ResourceDevice], SensorInsightsListGatewayDevicesRequestErrorBody]`
- **Error**: `SensorInsightsListGatewayDevicesRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListDevicesRequest` | `verizon/models/dto_list_devices_request.py` |
| `DtoListDevicesRequestDict` | `verizon/models/dto_list_devices_request.py` |
| `ResourceDevice` | `verizon/models/resource_device.py` |
| `SensorInsightsListGatewayDevicesRequestErrorBody` | `verizon/errors/sensor_insights_list_gateway_devices_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

