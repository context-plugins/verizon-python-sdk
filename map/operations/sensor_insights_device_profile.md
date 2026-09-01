<!-- Generated file — do not edit; regenerated with the SDK. -->

# SensorInsightsDeviceProfile — operations

Accessor: `client.sensor_insights_device_profile` · Source: `verizon/apis/sensor_insights_device_profile.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sensor_insights_device_profile.create_a_profile

- **Route**: `POST /dm/v1/deviceConfigurationProfiles`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def create_a_profile(body: DtoConfigurationProfile | DtoConfigurationProfileDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DtoProfileResponse]`
- **Returns (raw)**: `ApiResult[list[DtoProfileResponse], CreateAprofileErrorBody]`
- **Error**: `CreateAprofileErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoConfigurationProfile` | `verizon/models/dto_configuration_profile.py` |
| `DtoConfigurationProfileDict` | `verizon/models/dto_configuration_profile.py` |
| `DtoProfileResponse` | `verizon/models/dto_profile_response.py` |
| `CreateAprofileErrorBody` | `verizon/errors/create_aprofile_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_device_profile.delete_a_profile

- **Route**: `DELETE /dm/v1/deviceConfigurationProfiles`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def delete_a_profile(deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `deleterequest`
- **Params**: `deleterequest` — header
- **Returns (parsed)**: `list[DtoProfileResponse]`
- **Returns (raw)**: `ApiResult[list[DtoProfileResponse], DeleteAprofileErrorBody]`
- **Error**: `DeleteAprofileErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoConfigurationProfileDelete` | `verizon/models/dto_configuration_profile_delete.py` |
| `DtoConfigurationProfileDeleteDict` | `verizon/models/dto_configuration_profile_delete.py` |
| `DtoProfileResponse` | `verizon/models/dto_profile_response.py` |
| `DeleteAprofileErrorBody` | `verizon/errors/delete_aprofile_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_device_profile.query_a_profile

- **Route**: `POST /dm/v1/deviceConfigurationProfiles/actions/query`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def query_a_profile(body: ResourceResourceQuery | ResourceResourceQueryDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DtoProfileResponse]`
- **Returns (raw)**: `ApiResult[list[DtoProfileResponse], QueryAprofileErrorBody]`
- **Error**: `QueryAprofileErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ResourceResourceQuery` | `verizon/models/resource_resource_query.py` |
| `ResourceResourceQueryDict` | `verizon/models/resource_resource_query.py` |
| `DtoProfileResponse` | `verizon/models/dto_profile_response.py` |
| `QueryAprofileErrorBody` | `verizon/errors/query_aprofile_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

### client.sensor_insights_device_profile.update_a_profile

- **Route**: `PATCH /dm/v1/deviceConfigurationProfiles`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_a_profile(body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DtoProfileResponse]`
- **Returns (raw)**: `ApiResult[list[DtoProfileResponse], UpdateAprofileErrorBody]`
- **Error**: `UpdateAprofileErrorBody` — **Case A (typed)**
- **Error arms**: `ManagementError400` [400] · `ManagementError` [401] · `ManagementError403` [403] · `ManagementError500` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DtoConfigurationProfilePath` | `verizon/models/dto_configuration_profile_path.py` |
| `DtoConfigurationProfilePathDict` | `verizon/models/dto_configuration_profile_path.py` |
| `DtoProfileResponse` | `verizon/models/dto_profile_response.py` |
| `UpdateAprofileErrorBody` | `verizon/errors/update_aprofile_error.py` |
| `ManagementError400` | `verizon/models/management_error400.py` |
| `ManagementError` | `verizon/models/management_error.py` |
| `ManagementError403` | `verizon/models/management_error403.py` |
| `ManagementError500` | `verizon/models/management_error500.py` |

