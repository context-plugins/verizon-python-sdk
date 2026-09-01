<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceManagement — operations

Accessor: `client.device_management` · Source: `verizon/apis/device_management.py` · 29 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_management.activate_service_for_devices

- **Route**: `POST /m2m/v1/devices/actions/activate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def activate_service_for_devices(body: CarrierActivateRequest | CarrierActivateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, ActivateServiceForDevicesErrorBody]`
- **Error**: `ActivateServiceForDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CarrierActivateRequest` | `verizon/models/carrier_activate_request.py` |
| `CarrierActivateRequestDict` | `verizon/models/carrier_activate_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `ActivateServiceForDevicesErrorBody` | `verizon/errors/activate_service_for_devices_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.add_devices

- **Route**: `POST /m2m/v1/devices/actions/add`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def add_devices(body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[AddDevicesResult]`
- **Returns (raw)**: `ApiResult[list[AddDevicesResult], AddDevicesErrorBody]`
- **Error**: `AddDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddDevicesRequest` | `verizon/models/add_devices_request.py` |
| `AddDevicesRequestDict` | `verizon/models/add_devices_request.py` |
| `AddDevicesResult` | `verizon/models/add_devices_result.py` |
| `AddDevicesErrorBody` | `verizon/errors/add_devices_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.billed_usage_info

- **Route**: `POST /m2m/v1/devices/usage/actions/billedusage/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def billed_usage_info(body: BilledusageListRequest | BilledusageListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, BilledUsageInfoErrorBody]`
- **Error**: `BilledUsageInfoErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BilledusageListRequest` | `verizon/models/billedusage_list_request.py` |
| `BilledusageListRequestDict` | `verizon/models/billedusage_list_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `BilledUsageInfoErrorBody` | `verizon/errors/billed_usage_info_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.change_devices_service_plan

- **Route**: `PUT /m2m/v1/devices/actions/plan`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def change_devices_service_plan(body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, ChangeDevicesServicePlanErrorBody]`
- **Error**: `ChangeDevicesServicePlanErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServicePlanUpdateRequest` | `verizon/models/service_plan_update_request.py` |
| `ServicePlanUpdateRequestDict` | `verizon/models/service_plan_update_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `ChangeDevicesServicePlanErrorBody` | `verizon/errors/change_devices_service_plan_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.check_devices_availability_for_activation

- **Route**: `POST /m2m/v1/devices/availability/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def check_devices_availability_for_activation(body: DeviceActivationRequest | DeviceActivationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, CheckDevicesAvailabilityForActivationErrorBody]`
- **Error**: `CheckDevicesAvailabilityForActivationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceActivationRequest` | `verizon/models/device_activation_request.py` |
| `DeviceActivationRequestDict` | `verizon/models/device_activation_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `CheckDevicesAvailabilityForActivationErrorBody` | `verizon/errors/check_devices_availability_for_activation_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.deactivate_service_for_devices

- **Route**: `POST /m2m/v1/devices/actions/deactivate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def deactivate_service_for_devices(body: CarrierDeactivateRequest | CarrierDeactivateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, DeactivateServiceForDevicesErrorBody]`
- **Error**: `DeactivateServiceForDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CarrierDeactivateRequest` | `verizon/models/carrier_deactivate_request.py` |
| `CarrierDeactivateRequestDict` | `verizon/models/carrier_deactivate_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `DeactivateServiceForDevicesErrorBody` | `verizon/errors/deactivate_service_for_devices_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.delete_deactivated_devices

- **Route**: `POST /m2m/v1/devices/actions/delete`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def delete_deactivated_devices(body: DeleteDevicesRequest | DeleteDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DeleteDevicesResult]`
- **Returns (raw)**: `ApiResult[list[DeleteDevicesResult], DeleteDeactivatedDevicesErrorBody]`
- **Error**: `DeleteDeactivatedDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteDevicesRequest` | `verizon/models/delete_devices_request.py` |
| `DeleteDevicesRequestDict` | `verizon/models/delete_devices_request.py` |
| `DeleteDevicesResult` | `verizon/models/delete_devices_result.py` |
| `DeleteDeactivatedDevicesErrorBody` | `verizon/errors/delete_deactivated_devices_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.device_upload

- **Route**: `POST /m2m/v1/devices/actions/upload`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_upload(body: DeviceUploadRequest | DeviceUploadRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RequestResponse`
- **Returns (raw)**: `ApiResult[RequestResponse, DeviceUploadErrorBody]`
- **Error**: `DeviceUploadErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceUploadRequest` | `verizon/models/device_upload_request.py` |
| `DeviceUploadRequestDict` | `verizon/models/device_upload_request.py` |
| `RequestResponse` | `verizon/models/request_response.py` |
| `DeviceUploadErrorBody` | `verizon/errors/device_upload_error.py` |
| `RestErrorResponse` | `verizon/models/rest_error_response.py` |

### client.device_management.device_upload_status

- **Route**: `POST /m2m/v1/devices/requests/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def device_upload_status(body: CheckOrderStatusRequest | CheckOrderStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, DeviceUploadStatusErrorBody]`
- **Error**: `DeviceUploadStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckOrderStatusRequest` | `verizon/models/check_order_status_request.py` |
| `CheckOrderStatusRequestDict` | `verizon/models/check_order_status_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `DeviceUploadStatusErrorBody` | `verizon/errors/device_upload_status_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.get_device_extended_diagnostic_information

- **Route**: `POST /m2m/v1/devices/extendeddiagnostics/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_device_extended_diagnostic_information(body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceExtendedDiagnosticsResult`
- **Returns (raw)**: `ApiResult[DeviceExtendedDiagnosticsResult, GetDeviceExtendedDiagnosticInformationErrorBody]`
- **Error**: `GetDeviceExtendedDiagnosticInformationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceExtendedDiagnosticsRequest` | `verizon/models/device_extended_diagnostics_request.py` |
| `DeviceExtendedDiagnosticsRequestDict` | `verizon/models/device_extended_diagnostics_request.py` |
| `DeviceExtendedDiagnosticsResult` | `verizon/models/device_extended_diagnostics_result.py` |
| `GetDeviceExtendedDiagnosticInformationErrorBody` | `verizon/errors/get_device_extended_diagnostic_information_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.get_device_service_suspension_status

- **Route**: `POST /m2m/v1/devices/suspension/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_device_service_suspension_status(body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, GetDeviceServiceSuspensionStatusErrorBody]`
- **Error**: `GetDeviceServiceSuspensionStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceSuspensionStatusRequest` | `verizon/models/device_suspension_status_request.py` |
| `DeviceSuspensionStatusRequestDict` | `verizon/models/device_suspension_status_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `GetDeviceServiceSuspensionStatusErrorBody` | `verizon/errors/get_device_service_suspension_status_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.list_current_devices_prl_version

- **Route**: `POST /m2m/v1/devices/prl/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_current_devices_prl_version(body: DevicePrlListRequest | DevicePrlListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, ListCurrentDevicesPrlversionErrorBody]`
- **Error**: `ListCurrentDevicesPrlversionErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DevicePrlListRequest` | `verizon/models/device_prl_list_request.py` |
| `DevicePrlListRequestDict` | `verizon/models/device_prl_list_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `ListCurrentDevicesPrlversionErrorBody` | `verizon/errors/list_current_devices_prlversion_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.list_devices_information

- **Route**: `POST /m2m/v1/devices/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_devices_information(body: AccountDeviceListRequest | AccountDeviceListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountDeviceListResult`
- **Returns (raw)**: `ApiResult[AccountDeviceListResult, ListDevicesInformationErrorBody]`
- **Error**: `ListDevicesInformationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountDeviceListRequest` | `verizon/models/account_device_list_request.py` |
| `AccountDeviceListRequestDict` | `verizon/models/account_device_list_request.py` |
| `AccountDeviceListResult` | `verizon/models/account_device_list_result.py` |
| `ListDevicesInformationErrorBody` | `verizon/errors/list_devices_information_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.list_devices_provisioning_history

- **Route**: `POST /m2m/v1/devices/history/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_devices_provisioning_history(body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[DeviceProvisioningHistoryListResult]`
- **Returns (raw)**: `ApiResult[list[DeviceProvisioningHistoryListResult], ListDevicesProvisioningHistoryErrorBody]`
- **Error**: `ListDevicesProvisioningHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceProvisioningHistoryListRequest` | `verizon/models/device_provisioning_history_list_request.py` |
| `DeviceProvisioningHistoryListRequestDict` | `verizon/models/device_provisioning_history_list_request.py` |
| `DeviceProvisioningHistoryListResult` | `verizon/models/device_provisioning_history_list_result.py` |
| `ListDevicesProvisioningHistoryErrorBody` | `verizon/errors/list_devices_provisioning_history_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.list_devices_usage_history

- **Route**: `POST /m2m/v1/devices/usage/actions/list`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_devices_usage_history(body: DeviceUsageListRequest | DeviceUsageListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceUsageListResult`
- **Returns (raw)**: `ApiResult[DeviceUsageListResult, ListDevicesUsageHistoryErrorBody]`
- **Error**: `ListDevicesUsageHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceUsageListRequest` | `verizon/models/device_usage_list_request.py` |
| `DeviceUsageListRequestDict` | `verizon/models/device_usage_list_request.py` |
| `DeviceUsageListResult` | `verizon/models/device_usage_list_result.py` |
| `ListDevicesUsageHistoryErrorBody` | `verizon/errors/list_devices_usage_history_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.list_devices_with_imei_iccid_mismatch

- **Route**: `POST /m2m/v1/devices/actions/list/imeiiccidmismatch`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def list_devices_with_imei_iccid_mismatch(body: DeviceMismatchListRequest | DeviceMismatchListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceMismatchListResult`
- **Returns (raw)**: `ApiResult[DeviceMismatchListResult, ListDevicesWithImeiIccidMismatchErrorBody]`
- **Error**: `ListDevicesWithImeiIccidMismatchErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceMismatchListRequest` | `verizon/models/device_mismatch_list_request.py` |
| `DeviceMismatchListRequestDict` | `verizon/models/device_mismatch_list_request.py` |
| `DeviceMismatchListResult` | `verizon/models/device_mismatch_list_result.py` |
| `ListDevicesWithImeiIccidMismatchErrorBody` | `verizon/errors/list_devices_with_imei_iccid_mismatch_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.move_devices_within_accounts_of_profile

- **Route**: `PUT /m2m/v1/devices/actions/move`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def move_devices_within_accounts_of_profile(body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, MoveDevicesWithinAccountsOfProfileErrorBody]`
- **Error**: `MoveDevicesWithinAccountsOfProfileErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MoveDeviceRequest` | `verizon/models/move_device_request.py` |
| `MoveDeviceRequestDict` | `verizon/models/move_device_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `MoveDevicesWithinAccountsOfProfileErrorBody` | `verizon/errors/move_devices_within_accounts_of_profile_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.restore_service_for_suspended_devices

- **Route**: `POST /m2m/v1/devices/actions/restore`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def restore_service_for_suspended_devices(body: CarrierActionsRequest | CarrierActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, RestoreServiceForSuspendedDevicesErrorBody]`
- **Error**: `RestoreServiceForSuspendedDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CarrierActionsRequest` | `verizon/models/carrier_actions_request.py` |
| `CarrierActionsRequestDict` | `verizon/models/carrier_actions_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `RestoreServiceForSuspendedDevicesErrorBody` | `verizon/errors/restore_service_for_suspended_devices_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.retrieve_aggregate_device_usage_history

- **Route**: `POST /m2m/v1/devices/usage/actions/list/aggregate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_aggregate_device_usage_history(body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, RetrieveAggregateDeviceUsageHistoryErrorBody]`
- **Error**: `RetrieveAggregateDeviceUsageHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceAggregateUsageListRequest` | `verizon/models/device_aggregate_usage_list_request.py` |
| `DeviceAggregateUsageListRequestDict` | `verizon/models/device_aggregate_usage_list_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `RetrieveAggregateDeviceUsageHistoryErrorBody` | `verizon/errors/retrieve_aggregate_device_usage_history_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.retrieve_device_connection_history

- **Route**: `POST /m2m/v1/devices/connections/actions/listHistory`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_device_connection_history(body: DeviceConnectionListRequest | DeviceConnectionListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ConnectionHistoryResult`
- **Returns (raw)**: `ApiResult[ConnectionHistoryResult, RetrieveDeviceConnectionHistoryErrorBody]`
- **Error**: `RetrieveDeviceConnectionHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceConnectionListRequest` | `verizon/models/device_connection_list_request.py` |
| `DeviceConnectionListRequestDict` | `verizon/models/device_connection_list_request.py` |
| `ConnectionHistoryResult` | `verizon/models/connection_history_result.py` |
| `RetrieveDeviceConnectionHistoryErrorBody` | `verizon/errors/retrieve_device_connection_history_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.suspend_service_for_devices

- **Route**: `POST /m2m/v1/devices/actions/suspend`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def suspend_service_for_devices(body: CarrierActionsRequest | CarrierActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, SuspendServiceForDevicesErrorBody]`
- **Error**: `SuspendServiceForDevicesErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CarrierActionsRequest` | `verizon/models/carrier_actions_request.py` |
| `CarrierActionsRequestDict` | `verizon/models/carrier_actions_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `SuspendServiceForDevicesErrorBody` | `verizon/errors/suspend_service_for_devices_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.update_device_id

- **Route**: `PUT /m2m/v1/devices/{serviceType}/actions/deviceId`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_device_id(service_type: str, body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `service_type`, `body`
- **Params**: `service_type` — path `serviceType` · `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UpdateDeviceIdErrorBody]`
- **Error**: `UpdateDeviceIdErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChangeDeviceIdRequest` | `verizon/models/change_device_id_request.py` |
| `ChangeDeviceIdRequestDict` | `verizon/models/change_device_id_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UpdateDeviceIdErrorBody` | `verizon/errors/update_device_id_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.update_devices_contact_information

- **Route**: `PUT /m2m/v1/devices/actions/contactInfo`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_devices_contact_information(body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UpdateDevicesContactInformationErrorBody]`
- **Error**: `UpdateDevicesContactInformationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ContactInfoUpdateRequest` | `verizon/models/contact_info_update_request.py` |
| `ContactInfoUpdateRequestDict` | `verizon/models/contact_info_update_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UpdateDevicesContactInformationErrorBody` | `verizon/errors/update_devices_contact_information_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.update_devices_cost_center_code

- **Route**: `PUT /m2m/v1/devices/costCenter`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_devices_cost_center_code(body: DeviceCostCenterRequest | DeviceCostCenterRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UpdateDevicesCostCenterCodeErrorBody]`
- **Error**: `UpdateDevicesCostCenterCodeErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceCostCenterRequest` | `verizon/models/device_cost_center_request.py` |
| `DeviceCostCenterRequestDict` | `verizon/models/device_cost_center_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UpdateDevicesCostCenterCodeErrorBody` | `verizon/errors/update_devices_cost_center_code_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.update_devices_custom_fields

- **Route**: `PUT /m2m/v1/devices/actions/customFields`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_devices_custom_fields(body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UpdateDevicesCustomFieldsErrorBody]`
- **Error**: `UpdateDevicesCustomFieldsErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CustomFieldsUpdateRequest` | `verizon/models/custom_fields_update_request.py` |
| `CustomFieldsUpdateRequestDict` | `verizon/models/custom_fields_update_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UpdateDevicesCustomFieldsErrorBody` | `verizon/errors/update_devices_custom_fields_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.update_devices_state

- **Route**: `PUT /m2m/v1/devices/actions/gotostate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def update_devices_state(body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UpdateDevicesStateErrorBody]`
- **Error**: `UpdateDevicesStateErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GoToStateRequest` | `verizon/models/go_to_state_request.py` |
| `GoToStateRequestDict` | `verizon/models/go_to_state_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UpdateDevicesStateErrorBody` | `verizon/errors/update_devices_state_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.upload_activate_device

- **Route**: `POST /m2m/v1/devices/actions/uploadactivate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def upload_activate_device(body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UploadActivateDeviceErrorBody]`
- **Error**: `UploadActivateDeviceErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadsActivatesDeviceRequest` | `verizon/models/uploads_activates_device_request.py` |
| `UploadsActivatesDeviceRequestDict` | `verizon/models/uploads_activates_device_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UploadActivateDeviceErrorBody` | `verizon/errors/upload_activate_device_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.usage_segmentation_label_association

- **Route**: `POST /m2m/v1/devices/actions/usagesegmentationlabels`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def usage_segmentation_label_association(body: AssociateLabelRequest | AssociateLabelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UsageSegmentationLabelAssociationErrorBody]`
- **Error**: `UsageSegmentationLabelAssociationErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AssociateLabelRequest` | `verizon/models/associate_label_request.py` |
| `AssociateLabelRequestDict` | `verizon/models/associate_label_request.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UsageSegmentationLabelAssociationErrorBody` | `verizon/errors/usage_segmentation_label_association_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

### client.device_management.usage_segmentation_label_deletion

- **Route**: `DELETE /m2m/v1/devices/actions/usagesegmentationlabels`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def usage_segmentation_label_deletion(account_name: str, label_list: LabelsList | LabelsListDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `label_list`
- **Params**: `account_name` — query `accountName` · `label_list` — query `LabelList`
- **Returns (parsed)**: `DeviceManagementResult`
- **Returns (raw)**: `ApiResult[DeviceManagementResult, UsageSegmentationLabelDeletionErrorBody]`
- **Error**: `UsageSegmentationLabelDeletionErrorBody` — **Case A (typed)**
- **Error arms**: `ConnectivityManagementResult` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LabelsList` | `verizon/models/labels_list.py` |
| `LabelsListDict` | `verizon/models/labels_list.py` |
| `DeviceManagementResult` | `verizon/models/device_management_result.py` |
| `UsageSegmentationLabelDeletionErrorBody` | `verizon/errors/usage_segmentation_label_deletion_error.py` |
| `ConnectivityManagementResult` | `verizon/models/connectivity_management_result.py` |

