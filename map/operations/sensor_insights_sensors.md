<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsSensors — operations

Accessor: `client.sensor_insights_sensors` · Source: `verizon/apis/sensor_insights_sensors.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_sensors.sensor_insights_list_sensor_devices_request

- **Route**: `POST /dm/v1/devices/sensors/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_list_sensor_devices_request(body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[ResourceDevice]`
- **Returns (raw)**: `ApiResult[list[ResourceDevice], SensorInsightsListSensorDevicesRequestErrorBody]`
- **Error**: `SensorInsightsListSensorDevicesRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoListSensorDevicesRequest` | `verizon/models/dto_list_sensor_devices_request.py` |
| `DtoListSensorDevicesRequestDict` | `verizon/models/dto_list_sensor_devices_request.py` |
| `ResourceDevice` | `verizon/models/resource_device.py` |
| `SensorInsightsListSensorDevicesRequestErrorBody` | `verizon/errors/sensor_insights_list_sensor_devices_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_sensors.sensor_insights_off_board_sensor_request

- **Route**: `POST /dm/v1/devices/sensors/offboard`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_off_board_sensor_request(body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SensorInsightsOffBoardSensorRequestErrorBody]`
- **Error**: `SensorInsightsOffBoardSensorRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoOffBoardSensorRequest` | `verizon/models/dto_off_board_sensor_request.py` |
| `DtoOffBoardSensorRequestDict` | `verizon/models/dto_off_board_sensor_request.py` |
| `SensorInsightsOffBoardSensorRequestErrorBody` | `verizon/errors/sensor_insights_off_board_sensor_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |

### client.sensor_insights_sensors.sensor_insights_on_board_sensor_request

- **Route**: `POST /dm/v1/devices/sensors/onboard`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_on_board_sensor_request(body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SensorInsightsOnBoardSensorRequestErrorBody]`
- **Error**: `SensorInsightsOnBoardSensorRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoOnBoardSensorRequest` | `verizon/models/dto_on_board_sensor_request.py` |
| `DtoOnBoardSensorRequestDict` | `verizon/models/dto_on_board_sensor_request.py` |
| `SensorInsightsOnBoardSensorRequestErrorBody` | `verizon/errors/sensor_insights_on_board_sensor_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_sensors.sensor_insights_sensor_off_boarding_status_request

- **Route**: `POST /dm/v1/devices/sensors/offboard/status/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_sensor_off_boarding_status_request(body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoSensorOffBoardingStatusResponse`
- **Returns (raw)**: `ApiResult[DtoSensorOffBoardingStatusResponse, SensorInsightsSensorOffBoardingStatusRequestErrorBody]`
- **Error**: `SensorInsightsSensorOffBoardingStatusRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoSensorOffBoardStatusRequest` | `verizon/models/dto_sensor_off_board_status_request.py` |
| `DtoSensorOffBoardStatusRequestDict` | `verizon/models/dto_sensor_off_board_status_request.py` |
| `DtoSensorOffBoardingStatusResponse` | `verizon/models/dto_sensor_off_boarding_status_response.py` |
| `SensorInsightsSensorOffBoardingStatusRequestErrorBody` | `verizon/errors/sensor_insights_sensor_off_boarding_status_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_sensors.sensor_insights_sensor_on_board_status_request

- **Route**: `POST /dm/v1/devices/sensors/onboard/status/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def sensor_insights_sensor_on_board_status_request(body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DtoSensorOnBoardingStatusResponse`
- **Returns (raw)**: `ApiResult[DtoSensorOnBoardingStatusResponse, SensorInsightsSensorOnBoardStatusRequestErrorBody]`
- **Error**: `SensorInsightsSensorOnBoardStatusRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401, 406, 415, 429] · `ManagementError403` [403] · `ManagementError404` [404] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoSensorOnBoardStatusRequest` | `verizon/models/dto_sensor_on_board_status_request.py` |
| `DtoSensorOnBoardStatusRequestDict` | `verizon/models/dto_sensor_on_board_status_request.py` |
| `DtoSensorOnBoardingStatusResponse` | `verizon/models/dto_sensor_on_boarding_status_response.py` |
| `SensorInsightsSensorOnBoardStatusRequestErrorBody` | `verizon/errors/sensor_insights_sensor_on_board_status_request_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError404` | `verizon/models/management_error404.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

