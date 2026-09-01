from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.activate_service_for_devices_error import (
    ActivateServiceForDevicesErrorBody,
    activate_service_for_devices_error_mapper,
)
from ..errors.add_devices_error import AddDevicesErrorBody, add_devices_error_mapper
from ..errors.billed_usage_info_error import BilledUsageInfoErrorBody, billed_usage_info_error_mapper
from ..errors.change_devices_service_plan_error import (
    ChangeDevicesServicePlanErrorBody,
    change_devices_service_plan_error_mapper,
)
from ..errors.check_devices_availability_for_activation_error import (
    CheckDevicesAvailabilityForActivationErrorBody,
    check_devices_availability_for_activation_error_mapper,
)
from ..errors.deactivate_service_for_devices_error import (
    DeactivateServiceForDevicesErrorBody,
    deactivate_service_for_devices_error_mapper,
)
from ..errors.delete_deactivated_devices_error import (
    DeleteDeactivatedDevicesErrorBody,
    delete_deactivated_devices_error_mapper,
)
from ..errors.device_upload_error import DeviceUploadErrorBody, device_upload_error_mapper
from ..errors.device_upload_status_error import DeviceUploadStatusErrorBody, device_upload_status_error_mapper
from ..errors.get_device_extended_diagnostic_information_error import (
    GetDeviceExtendedDiagnosticInformationErrorBody,
    get_device_extended_diagnostic_information_error_mapper,
)
from ..errors.get_device_service_suspension_status_error import (
    GetDeviceServiceSuspensionStatusErrorBody,
    get_device_service_suspension_status_error_mapper,
)
from ..errors.list_current_devices_prlversion_error import (
    ListCurrentDevicesPrlversionErrorBody,
    list_current_devices_prlversion_error_mapper,
)
from ..errors.list_devices_information_error import (
    ListDevicesInformationErrorBody,
    list_devices_information_error_mapper,
)
from ..errors.list_devices_provisioning_history_error import (
    ListDevicesProvisioningHistoryErrorBody,
    list_devices_provisioning_history_error_mapper,
)
from ..errors.list_devices_usage_history_error import (
    ListDevicesUsageHistoryErrorBody,
    list_devices_usage_history_error_mapper,
)
from ..errors.list_devices_with_imei_iccid_mismatch_error import (
    ListDevicesWithImeiIccidMismatchErrorBody,
    list_devices_with_imei_iccid_mismatch_error_mapper,
)
from ..errors.move_devices_within_accounts_of_profile_error import (
    MoveDevicesWithinAccountsOfProfileErrorBody,
    move_devices_within_accounts_of_profile_error_mapper,
)
from ..errors.restore_service_for_suspended_devices_error import (
    RestoreServiceForSuspendedDevicesErrorBody,
    restore_service_for_suspended_devices_error_mapper,
)
from ..errors.retrieve_aggregate_device_usage_history_error import (
    RetrieveAggregateDeviceUsageHistoryErrorBody,
    retrieve_aggregate_device_usage_history_error_mapper,
)
from ..errors.retrieve_device_connection_history_error import (
    RetrieveDeviceConnectionHistoryErrorBody,
    retrieve_device_connection_history_error_mapper,
)
from ..errors.suspend_service_for_devices_error import (
    SuspendServiceForDevicesErrorBody,
    suspend_service_for_devices_error_mapper,
)
from ..errors.update_device_id_error import UpdateDeviceIdErrorBody, update_device_id_error_mapper
from ..errors.update_devices_contact_information_error import (
    UpdateDevicesContactInformationErrorBody,
    update_devices_contact_information_error_mapper,
)
from ..errors.update_devices_cost_center_code_error import (
    UpdateDevicesCostCenterCodeErrorBody,
    update_devices_cost_center_code_error_mapper,
)
from ..errors.update_devices_custom_fields_error import (
    UpdateDevicesCustomFieldsErrorBody,
    update_devices_custom_fields_error_mapper,
)
from ..errors.update_devices_state_error import UpdateDevicesStateErrorBody, update_devices_state_error_mapper
from ..errors.upload_activate_device_error import UploadActivateDeviceErrorBody, upload_activate_device_error_mapper
from ..errors.usage_segmentation_label_association_error import (
    UsageSegmentationLabelAssociationErrorBody,
    usage_segmentation_label_association_error_mapper,
)
from ..errors.usage_segmentation_label_deletion_error import (
    UsageSegmentationLabelDeletionErrorBody,
    usage_segmentation_label_deletion_error_mapper,
)
from ..models.account_device_list_request import AccountDeviceListRequest, AccountDeviceListRequestDict
from ..models.account_device_list_result import AccountDeviceListResult
from ..models.add_devices_request import AddDevicesRequest, AddDevicesRequestDict
from ..models.add_devices_result import AddDevicesResult
from ..models.associate_label_request import AssociateLabelRequest, AssociateLabelRequestDict
from ..models.billedusage_list_request import BilledusageListRequest, BilledusageListRequestDict
from ..models.carrier_actions_request import CarrierActionsRequest, CarrierActionsRequestDict
from ..models.carrier_activate_request import CarrierActivateRequest, CarrierActivateRequestDict
from ..models.carrier_deactivate_request import CarrierDeactivateRequest, CarrierDeactivateRequestDict
from ..models.change_device_id_request import ChangeDeviceIdRequest, ChangeDeviceIdRequestDict
from ..models.check_order_status_request import CheckOrderStatusRequest, CheckOrderStatusRequestDict
from ..models.connection_history_result import ConnectionHistoryResult
from ..models.contact_info_update_request import ContactInfoUpdateRequest, ContactInfoUpdateRequestDict
from ..models.custom_fields_update_request import CustomFieldsUpdateRequest, CustomFieldsUpdateRequestDict
from ..models.delete_devices_request import DeleteDevicesRequest, DeleteDevicesRequestDict
from ..models.delete_devices_result import DeleteDevicesResult
from ..models.device_activation_request import DeviceActivationRequest, DeviceActivationRequestDict
from ..models.device_aggregate_usage_list_request import (
    DeviceAggregateUsageListRequest,
    DeviceAggregateUsageListRequestDict,
)
from ..models.device_connection_list_request import DeviceConnectionListRequest, DeviceConnectionListRequestDict
from ..models.device_cost_center_request import DeviceCostCenterRequest, DeviceCostCenterRequestDict
from ..models.device_extended_diagnostics_request import (
    DeviceExtendedDiagnosticsRequest,
    DeviceExtendedDiagnosticsRequestDict,
)
from ..models.device_extended_diagnostics_result import DeviceExtendedDiagnosticsResult
from ..models.device_management_result import DeviceManagementResult
from ..models.device_mismatch_list_request import DeviceMismatchListRequest, DeviceMismatchListRequestDict
from ..models.device_mismatch_list_result import DeviceMismatchListResult
from ..models.device_prl_list_request import DevicePrlListRequest, DevicePrlListRequestDict
from ..models.device_provisioning_history_list_request import (
    DeviceProvisioningHistoryListRequest,
    DeviceProvisioningHistoryListRequestDict,
)
from ..models.device_provisioning_history_list_result import DeviceProvisioningHistoryListResult
from ..models.device_suspension_status_request import DeviceSuspensionStatusRequest, DeviceSuspensionStatusRequestDict
from ..models.device_upload_request import DeviceUploadRequest, DeviceUploadRequestDict
from ..models.device_usage_list_request import DeviceUsageListRequest, DeviceUsageListRequestDict
from ..models.device_usage_list_result import DeviceUsageListResult
from ..models.go_to_state_request import GoToStateRequest, GoToStateRequestDict
from ..models.labels_list import LabelsList, LabelsListDict
from ..models.move_device_request import MoveDeviceRequest, MoveDeviceRequestDict
from ..models.request_response import RequestResponse
from ..models.service_plan_update_request import ServicePlanUpdateRequest, ServicePlanUpdateRequestDict
from ..models.uploads_activates_device_request import UploadsActivatesDeviceRequest, UploadsActivatesDeviceRequestDict
from ..server.server import Server


class DeviceManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceManagementWithRawResponse(client, server, auth)

    def activate_service_for_devices(
        self,
        body: CarrierActivateRequest | CarrierActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Request for activating a service on devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.activate_service_for_devices(body, request_options=request_options).unwrap()

    def add_devices(
        self, body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[AddDevicesResult]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            For each device in the request, contains device identifiers and a success or failure response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.add_devices(body, request_options=request_options).unwrap()

    def billed_usage_info(
        self,
        body: BilledusageListRequest | BilledusageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Gets billed usage for for either multiple devices or an entire billing account.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.billed_usage_info(body, request_options=request_options).unwrap()

    def change_devices_service_plan(
        self,
        body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Changes the service plan for one or more devices.

        Args:
            body: Request to change device service plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.change_devices_service_plan(body, request_options=request_options).unwrap()

    def check_devices_availability_for_activation(
        self,
        body: DeviceActivationRequest | DeviceActivationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Checks whether specified devices are registered by the manufacturer with the Verizon network and are
        available to be activated.

        Args:
            body: Request to check if devices can be activated or not.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.check_devices_availability_for_activation(
            body, request_options=request_options
        ).unwrap()

    def deactivate_service_for_devices(
        self,
        body: CarrierDeactivateRequest | CarrierDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Deactivating service for a device may result in an early termination fee (ETF) being charged to the account,
        depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use
        one for a particular deactivation, set the etfWaiver value to True.

        Args:
            body: Request to deactivate service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.deactivate_service_for_devices(body, request_options=request_options).unwrap()

    def delete_deactivated_devices(
        self,
        body: DeleteDevicesRequest | DeleteDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DeleteDevicesResult]:
        """Use this API to remove unneeded devices from an account.

        Args:
            body: Devices to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            For each device in the request, contains device identifiers and a success or failure response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.delete_deactivated_devices(body, request_options=request_options).unwrap()

    def device_upload(
        self,
        body: DeviceUploadRequest | DeviceUploadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Upload a device record

        Args:
            body: Device Upload Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.device_upload(body, request_options=request_options).unwrap()

    def device_upload_status(
        self,
        body: CheckOrderStatusRequest | CheckOrderStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Checks the status of an activation order and lists where the order is in the provisioning process.

        Args:
            body: The request body identifies the device and reporting period that you want included in the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.device_upload_status(body, request_options=request_options).unwrap()

    def get_device_extended_diagnostic_information(
        self,
        body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceExtendedDiagnosticsResult:
        """Returns extended diagnostic information about a specified device, including connectivity, provisioning,
        billing and location status.

        Args:
            body: Request to query extended diagnostics information for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device diagnostic information.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.get_device_extended_diagnostic_information(
            body, request_options=request_options
        ).unwrap()

    def get_device_service_suspension_status(
        self,
        body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Returns DeviceSuspensionStatus callback messages containing the current device state and information on how
        many days a device has been suspended and can continue to be suspended.

        Args:
            body: Request to obtain service suspenstion status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.get_device_service_suspension_status(
            body, request_options=request_options
        ).unwrap()

    def list_current_devices_prl_version(
        self,
        body: DevicePrlListRequest | DevicePrlListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """4G and GSM devices do not have a PRL.

        Args:
            body: Request to query device PRL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_current_devices_prl_version(body, request_options=request_options).unwrap()

    def list_devices_information(
        self,
        body: AccountDeviceListRequest | AccountDeviceListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountDeviceListResult:
        """Returns information about a single device or information about all devices that match the given parameters.
        Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

        Args:
            body: Device information query.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of devices that match the request parameters, ordered by device creation date, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_devices_information(body, request_options=request_options).unwrap()

    def list_devices_provisioning_history(
        self,
        body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DeviceProvisioningHistoryListResult]:
        """Returns the provisioning history of a specified device during a specified time period.

        Args:
            body: Query to obtain device provisioning history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Device Provision History events, sorted by the timestamp, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_devices_provisioning_history(body, request_options=request_options).unwrap()

    def list_devices_usage_history(
        self,
        body: DeviceUsageListRequest | DeviceUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceUsageListResult:
        """Returns the network data usage history of a device during a specified time period.

        Args:
            body: Request to obtain usage history for a specific device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of device usage events, sorted by the timestamp, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_devices_usage_history(body, request_options=request_options).unwrap()

    def list_devices_with_imei_iccid_mismatch(
        self,
        body: DeviceMismatchListRequest | DeviceMismatchListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceMismatchListResult:
        """Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware)
        during a specified time frame.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of devices that have mismatched IMEIs and ICCIDs.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_devices_with_imei_iccid_mismatch(
            body, request_options=request_options
        ).unwrap()

    def move_devices_within_accounts_of_profile(
        self, body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceManagementResult:
        """Move active devices from one billing account to another within a customer profile.

        Args:
            body: Request to move devices between accounts.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.move_devices_within_accounts_of_profile(
            body, request_options=request_options
        ).unwrap()

    def restore_service_for_suspended_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Restores service to one or more suspended devices.

        Args:
            body: Request to restore services of one or more suspended devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.restore_service_for_suspended_devices(
            body, request_options=request_options
        ).unwrap()

    def retrieve_aggregate_device_usage_history(
        self,
        body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """The information is returned in a callback response, so you must register a URL for DeviceUsage callback
        messages using the POST /callbacks API.

        Args:
            body: A request to retrieve aggregated device usage history information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A unique string that associates the request with the results that are sent via a callback service.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.retrieve_aggregate_device_usage_history(
            body, request_options=request_options
        ).unwrap()

    def retrieve_device_connection_history(
        self,
        body: DeviceConnectionListRequest | DeviceConnectionListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectionHistoryResult:
        """Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times,
        adjusting the earliest value each time to start where the previous request finished.

        Args:
            body: Query to retrieve device connection history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of device connection events, sorted by the occurredAt timestamp, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.retrieve_device_connection_history(
            body, request_options=request_options
        ).unwrap()

    def suspend_service_for_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Suspends service for one or more devices.

        Args:
            body: Request to suspend service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.suspend_service_for_devices(body, request_options=request_options).unwrap()

    def update_device_id(
        self,
        service_type: str,
        body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this
        request to transfer the line of service and the MDN to new hardware, or to change the MDN.

        Args:
            service_type: Identifier type.
            body: Request to update device id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A unique string that associates the request with the results that are sent via a callback service.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.update_device_id(service_type, body, request_options=request_options).unwrap()

    def update_devices_contact_information(
        self,
        body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Sends a CarrierService callback message for each device in the request when the contact information has been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update contact information for devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID returned in a success response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.update_devices_contact_information(
            body, request_options=request_options
        ).unwrap()

    def update_devices_cost_center_code(
        self,
        body: DeviceCostCenterRequest | DeviceCostCenterRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or
        more devices.

        Args:
            body: Request to update cost center code value for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.update_devices_cost_center_code(body, request_options=request_options).unwrap()

    def update_devices_custom_fields(
        self,
        body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Sends a CarrierService callback message for each device in the request when the custom fields have been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update custom field of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.update_devices_custom_fields(body, request_options=request_options).unwrap()

    def update_devices_state(
        self, body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceManagementResult:
        """Changes the provisioning state of one or more devices to a specified customer-defined service and state.

        Args:
            body: Request to change device state to one defined by the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.update_devices_state(body, request_options=request_options).unwrap()

    def upload_activate_device(
        self,
        body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Uploads and activates device identifiers and SKUs for new devices from OEMs to Verizon.

        Args:
            body: Request to Upload and Activate device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.upload_activate_device(body, request_options=request_options).unwrap()

    def usage_segmentation_label_association(
        self,
        body: AssociateLabelRequest | AssociateLabelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Allows you to associate your own usage segmentation label with a device.

        Args:
            body: Request to associate a label to a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.usage_segmentation_label_association(
            body, request_options=request_options
        ).unwrap()

    def usage_segmentation_label_deletion(
        self,
        account_name: str,
        label_list: LabelsList | LabelsListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Allow customers to remove the associated label from a device.

        Args:
            account_name: The numeric name of the account.
            label_list: A list of the Label IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.usage_segmentation_label_deletion(
            account_name, label_list, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DeviceManagementWithRawResponse:
        return self._with_raw_response


class AsyncDeviceManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceManagementWithRawResponse(client, server, auth)

    async def activate_service_for_devices(
        self,
        body: CarrierActivateRequest | CarrierActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Request for activating a service on devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.activate_service_for_devices(body, request_options=request_options)
        ).unwrap()

    async def add_devices(
        self, body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[AddDevicesResult]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            For each device in the request, contains device identifiers and a success or failure response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.add_devices(body, request_options=request_options)).unwrap()

    async def billed_usage_info(
        self,
        body: BilledusageListRequest | BilledusageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Gets billed usage for for either multiple devices or an entire billing account.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.billed_usage_info(body, request_options=request_options)).unwrap()

    async def change_devices_service_plan(
        self,
        body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Changes the service plan for one or more devices.

        Args:
            body: Request to change device service plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.change_devices_service_plan(body, request_options=request_options)
        ).unwrap()

    async def check_devices_availability_for_activation(
        self,
        body: DeviceActivationRequest | DeviceActivationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Checks whether specified devices are registered by the manufacturer with the Verizon network and are
        available to be activated.

        Args:
            body: Request to check if devices can be activated or not.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.check_devices_availability_for_activation(
                body, request_options=request_options
            )
        ).unwrap()

    async def deactivate_service_for_devices(
        self,
        body: CarrierDeactivateRequest | CarrierDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Deactivating service for a device may result in an early termination fee (ETF) being charged to the account,
        depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use
        one for a particular deactivation, set the etfWaiver value to True.

        Args:
            body: Request to deactivate service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.deactivate_service_for_devices(body, request_options=request_options)
        ).unwrap()

    async def delete_deactivated_devices(
        self,
        body: DeleteDevicesRequest | DeleteDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DeleteDevicesResult]:
        """Use this API to remove unneeded devices from an account.

        Args:
            body: Devices to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            For each device in the request, contains device identifiers and a success or failure response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.delete_deactivated_devices(body, request_options=request_options)
        ).unwrap()

    async def device_upload(
        self,
        body: DeviceUploadRequest | DeviceUploadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Upload a device record

        Args:
            body: Device Upload Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return (await self._with_raw_response.device_upload(body, request_options=request_options)).unwrap()

    async def device_upload_status(
        self,
        body: CheckOrderStatusRequest | CheckOrderStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Checks the status of an activation order and lists where the order is in the provisioning process.

        Args:
            body: The request body identifies the device and reporting period that you want included in the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.device_upload_status(body, request_options=request_options)).unwrap()

    async def get_device_extended_diagnostic_information(
        self,
        body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceExtendedDiagnosticsResult:
        """Returns extended diagnostic information about a specified device, including connectivity, provisioning,
        billing and location status.

        Args:
            body: Request to query extended diagnostics information for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device diagnostic information.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.get_device_extended_diagnostic_information(
                body, request_options=request_options
            )
        ).unwrap()

    async def get_device_service_suspension_status(
        self,
        body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Returns DeviceSuspensionStatus callback messages containing the current device state and information on how
        many days a device has been suspended and can continue to be suspended.

        Args:
            body: Request to obtain service suspenstion status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.get_device_service_suspension_status(body, request_options=request_options)
        ).unwrap()

    async def list_current_devices_prl_version(
        self,
        body: DevicePrlListRequest | DevicePrlListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """4G and GSM devices do not have a PRL.

        Args:
            body: Request to query device PRL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_current_devices_prl_version(body, request_options=request_options)
        ).unwrap()

    async def list_devices_information(
        self,
        body: AccountDeviceListRequest | AccountDeviceListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountDeviceListResult:
        """Returns information about a single device or information about all devices that match the given parameters.
        Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

        Args:
            body: Device information query.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of devices that match the request parameters, ordered by device creation date, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.list_devices_information(body, request_options=request_options)).unwrap()

    async def list_devices_provisioning_history(
        self,
        body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DeviceProvisioningHistoryListResult]:
        """Returns the provisioning history of a specified device during a specified time period.

        Args:
            body: Query to obtain device provisioning history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Device Provision History events, sorted by the timestamp, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_devices_provisioning_history(body, request_options=request_options)
        ).unwrap()

    async def list_devices_usage_history(
        self,
        body: DeviceUsageListRequest | DeviceUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceUsageListResult:
        """Returns the network data usage history of a device during a specified time period.

        Args:
            body: Request to obtain usage history for a specific device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of device usage events, sorted by the timestamp, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_devices_usage_history(body, request_options=request_options)
        ).unwrap()

    async def list_devices_with_imei_iccid_mismatch(
        self,
        body: DeviceMismatchListRequest | DeviceMismatchListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceMismatchListResult:
        """Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware)
        during a specified time frame.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of devices that have mismatched IMEIs and ICCIDs.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_devices_with_imei_iccid_mismatch(body, request_options=request_options)
        ).unwrap()

    async def move_devices_within_accounts_of_profile(
        self, body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceManagementResult:
        """Move active devices from one billing account to another within a customer profile.

        Args:
            body: Request to move devices between accounts.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.move_devices_within_accounts_of_profile(body, request_options=request_options)
        ).unwrap()

    async def restore_service_for_suspended_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Restores service to one or more suspended devices.

        Args:
            body: Request to restore services of one or more suspended devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.restore_service_for_suspended_devices(body, request_options=request_options)
        ).unwrap()

    async def retrieve_aggregate_device_usage_history(
        self,
        body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """The information is returned in a callback response, so you must register a URL for DeviceUsage callback
        messages using the POST /callbacks API.

        Args:
            body: A request to retrieve aggregated device usage history information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A unique string that associates the request with the results that are sent via a callback service.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.retrieve_aggregate_device_usage_history(body, request_options=request_options)
        ).unwrap()

    async def retrieve_device_connection_history(
        self,
        body: DeviceConnectionListRequest | DeviceConnectionListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectionHistoryResult:
        """Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times,
        adjusting the earliest value each time to start where the previous request finished.

        Args:
            body: Query to retrieve device connection history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of device connection events, sorted by the occurredAt timestamp, oldest first.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.retrieve_device_connection_history(body, request_options=request_options)
        ).unwrap()

    async def suspend_service_for_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Suspends service for one or more devices.

        Args:
            body: Request to suspend service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.suspend_service_for_devices(body, request_options=request_options)
        ).unwrap()

    async def update_device_id(
        self,
        service_type: str,
        body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this
        request to transfer the line of service and the MDN to new hardware, or to change the MDN.

        Args:
            service_type: Identifier type.
            body: Request to update device id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A unique string that associates the request with the results that are sent via a callback service.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.update_device_id(service_type, body, request_options=request_options)
        ).unwrap()

    async def update_devices_contact_information(
        self,
        body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Sends a CarrierService callback message for each device in the request when the contact information has been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update contact information for devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID returned in a success response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.update_devices_contact_information(body, request_options=request_options)
        ).unwrap()

    async def update_devices_cost_center_code(
        self,
        body: DeviceCostCenterRequest | DeviceCostCenterRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or
        more devices.

        Args:
            body: Request to update cost center code value for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.update_devices_cost_center_code(body, request_options=request_options)
        ).unwrap()

    async def update_devices_custom_fields(
        self,
        body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Sends a CarrierService callback message for each device in the request when the custom fields have been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update custom field of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.update_devices_custom_fields(body, request_options=request_options)
        ).unwrap()

    async def update_devices_state(
        self, body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceManagementResult:
        """Changes the provisioning state of one or more devices to a specified customer-defined service and state.

        Args:
            body: Request to change device state to one defined by the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.update_devices_state(body, request_options=request_options)).unwrap()

    async def upload_activate_device(
        self,
        body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Uploads and activates device identifiers and SKUs for new devices from OEMs to Verizon.

        Args:
            body: Request to Upload and Activate device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.upload_activate_device(body, request_options=request_options)).unwrap()

    async def usage_segmentation_label_association(
        self,
        body: AssociateLabelRequest | AssociateLabelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Allows you to associate your own usage segmentation label with a device.

        Args:
            body: Request to associate a label to a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.usage_segmentation_label_association(body, request_options=request_options)
        ).unwrap()

    async def usage_segmentation_label_deletion(
        self,
        account_name: str,
        label_list: LabelsList | LabelsListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Allow customers to remove the associated label from a device.

        Args:
            account_name: The numeric name of the account.
            label_list: A list of the Label IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.usage_segmentation_label_deletion(
                account_name, label_list, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceManagementWithRawResponse:
        return self._with_raw_response


class DeviceManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_service_for_devices(
        self,
        body: CarrierActivateRequest | CarrierActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, ActivateServiceForDevicesErrorBody]:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Request for activating a service on devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierActivateRequest | CarrierActivateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=activate_service_for_devices_error_mapper,
            request_options=request_options,
        )

    def add_devices(
        self, body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[AddDevicesResult], AddDevicesErrorBody]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/add"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddDevicesRequest | AddDevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[AddDevicesResult]],
            error_mapper=add_devices_error_mapper,
            request_options=request_options,
        )

    def billed_usage_info(
        self,
        body: BilledusageListRequest | BilledusageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, BilledUsageInfoErrorBody]:
        """Gets billed usage for for either multiple devices or an entire billing account.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/billedusage/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BilledusageListRequest | BilledusageListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=billed_usage_info_error_mapper,
            request_options=request_options,
        )

    def change_devices_service_plan(
        self,
        body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, ChangeDevicesServicePlanErrorBody]:
        """Changes the service plan for one or more devices.

        Args:
            body: Request to change device service plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/plan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePlanUpdateRequest | ServicePlanUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=change_devices_service_plan_error_mapper,
            request_options=request_options,
        )

    def check_devices_availability_for_activation(
        self,
        body: DeviceActivationRequest | DeviceActivationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, CheckDevicesAvailabilityForActivationErrorBody]:
        """Checks whether specified devices are registered by the manufacturer with the Verizon network and are
        available to be activated.

        Args:
            body: Request to check if devices can be activated or not.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/availability/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceActivationRequest | DeviceActivationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=check_devices_availability_for_activation_error_mapper,
            request_options=request_options,
        )

    def deactivate_service_for_devices(
        self,
        body: CarrierDeactivateRequest | CarrierDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DeactivateServiceForDevicesErrorBody]:
        """Deactivating service for a device may result in an early termination fee (ETF) being charged to the account,
        depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use
        one for a particular deactivation, set the etfWaiver value to True.

        Args:
            body: Request to deactivate service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierDeactivateRequest | CarrierDeactivateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=deactivate_service_for_devices_error_mapper,
            request_options=request_options,
        )

    def delete_deactivated_devices(
        self,
        body: DeleteDevicesRequest | DeleteDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DeleteDevicesResult], DeleteDeactivatedDevicesErrorBody]:
        """Use this API to remove unneeded devices from an account.

        Args:
            body: Devices to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteDevicesRequest | DeleteDevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeleteDevicesResult]],
            error_mapper=delete_deactivated_devices_error_mapper,
            request_options=request_options,
        )

    def device_upload(
        self,
        body: DeviceUploadRequest | DeviceUploadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DeviceUploadErrorBody]:
        """Upload a device record

        Args:
            body: Device Upload Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/upload"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceUploadRequest | DeviceUploadRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=device_upload_error_mapper,
            request_options=request_options,
        )

    def device_upload_status(
        self,
        body: CheckOrderStatusRequest | CheckOrderStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DeviceUploadStatusErrorBody]:
        """Checks the status of an activation order and lists where the order is in the provisioning process.

        Args:
            body: The request body identifies the device and reporting period that you want included in the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/requests/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CheckOrderStatusRequest | CheckOrderStatusRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=device_upload_status_error_mapper,
            request_options=request_options,
        )

    def get_device_extended_diagnostic_information(
        self,
        body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceExtendedDiagnosticsResult, GetDeviceExtendedDiagnosticInformationErrorBody]:
        """Returns extended diagnostic information about a specified device, including connectivity, provisioning,
        billing and location status.

        Args:
            body: Request to query extended diagnostics information for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/extendeddiagnostics/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceExtendedDiagnosticsResult],
            error_mapper=get_device_extended_diagnostic_information_error_mapper,
            request_options=request_options,
        )

    def get_device_service_suspension_status(
        self,
        body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, GetDeviceServiceSuspensionStatusErrorBody]:
        """Returns DeviceSuspensionStatus callback messages containing the current device state and information on how
        many days a device has been suspended and can continue to be suspended.

        Args:
            body: Request to obtain service suspenstion status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/suspension/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=get_device_service_suspension_status_error_mapper,
            request_options=request_options,
        )

    def list_current_devices_prl_version(
        self,
        body: DevicePrlListRequest | DevicePrlListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, ListCurrentDevicesPrlversionErrorBody]:
        """4G and GSM devices do not have a PRL.

        Args:
            body: Request to query device PRL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/prl/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DevicePrlListRequest | DevicePrlListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=list_current_devices_prlversion_error_mapper,
            request_options=request_options,
        )

    def list_devices_information(
        self,
        body: AccountDeviceListRequest | AccountDeviceListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountDeviceListResult, ListDevicesInformationErrorBody]:
        """Returns information about a single device or information about all devices that match the given parameters.
        Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

        Args:
            body: Device information query.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountDeviceListRequest | AccountDeviceListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountDeviceListResult],
            error_mapper=list_devices_information_error_mapper,
            request_options=request_options,
        )

    def list_devices_provisioning_history(
        self,
        body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DeviceProvisioningHistoryListResult], ListDevicesProvisioningHistoryErrorBody]:
        """Returns the provisioning history of a specified device during a specified time period.

        Args:
            body: Query to obtain device provisioning history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/history/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceProvisioningHistoryListResult]],
            error_mapper=list_devices_provisioning_history_error_mapper,
            request_options=request_options,
        )

    def list_devices_usage_history(
        self,
        body: DeviceUsageListRequest | DeviceUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceUsageListResult, ListDevicesUsageHistoryErrorBody]:
        """Returns the network data usage history of a device during a specified time period.

        Args:
            body: Request to obtain usage history for a specific device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceUsageListRequest | DeviceUsageListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceUsageListResult],
            error_mapper=list_devices_usage_history_error_mapper,
            request_options=request_options,
        )

    def list_devices_with_imei_iccid_mismatch(
        self,
        body: DeviceMismatchListRequest | DeviceMismatchListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceMismatchListResult, ListDevicesWithImeiIccidMismatchErrorBody]:
        """Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware)
        during a specified time frame.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/list/imeiiccidmismatch"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceMismatchListRequest | DeviceMismatchListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceMismatchListResult],
            error_mapper=list_devices_with_imei_iccid_mismatch_error_mapper,
            request_options=request_options,
        )

    def move_devices_within_accounts_of_profile(
        self, body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceManagementResult, MoveDevicesWithinAccountsOfProfileErrorBody]:
        """Move active devices from one billing account to another within a customer profile.

        Args:
            body: Request to move devices between accounts.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/move"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MoveDeviceRequest | MoveDeviceRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=move_devices_within_accounts_of_profile_error_mapper,
            request_options=request_options,
        )

    def restore_service_for_suspended_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, RestoreServiceForSuspendedDevicesErrorBody]:
        """Restores service to one or more suspended devices.

        Args:
            body: Request to restore services of one or more suspended devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/restore"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierActionsRequest | CarrierActionsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=restore_service_for_suspended_devices_error_mapper,
            request_options=request_options,
        )

    def retrieve_aggregate_device_usage_history(
        self,
        body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, RetrieveAggregateDeviceUsageHistoryErrorBody]:
        """The information is returned in a callback response, so you must register a URL for DeviceUsage callback
        messages using the POST /callbacks API.

        Args:
            body: A request to retrieve aggregated device usage history information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/list/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=retrieve_aggregate_device_usage_history_error_mapper,
            request_options=request_options,
        )

    def retrieve_device_connection_history(
        self,
        body: DeviceConnectionListRequest | DeviceConnectionListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectionHistoryResult, RetrieveDeviceConnectionHistoryErrorBody]:
        """Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times,
        adjusting the earliest value each time to start where the previous request finished.

        Args:
            body: Query to retrieve device connection history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/connections/actions/listHistory"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceConnectionListRequest | DeviceConnectionListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectionHistoryResult],
            error_mapper=retrieve_device_connection_history_error_mapper,
            request_options=request_options,
        )

    def suspend_service_for_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, SuspendServiceForDevicesErrorBody]:
        """Suspends service for one or more devices.

        Args:
            body: Request to suspend service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/suspend"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierActionsRequest | CarrierActionsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=suspend_service_for_devices_error_mapper,
            request_options=request_options,
        )

    def update_device_id(
        self,
        service_type: str,
        body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDeviceIdErrorBody]:
        """Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this
        request to transfer the line of service and the MDN to new hardware, or to change the MDN.

        Args:
            service_type: Identifier type.
            body: Request to update device id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/{serviceType}/actions/deviceId"),
            path_params=[param[str]("serviceType", service_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangeDeviceIdRequest | ChangeDeviceIdRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_device_id_error_mapper,
            request_options=request_options,
        )

    def update_devices_contact_information(
        self,
        body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesContactInformationErrorBody]:
        """Sends a CarrierService callback message for each device in the request when the contact information has been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update contact information for devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/contactInfo"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ContactInfoUpdateRequest | ContactInfoUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_contact_information_error_mapper,
            request_options=request_options,
        )

    def update_devices_cost_center_code(
        self,
        body: DeviceCostCenterRequest | DeviceCostCenterRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesCostCenterCodeErrorBody]:
        """Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or
        more devices.

        Args:
            body: Request to update cost center code value for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/costCenter"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceCostCenterRequest | DeviceCostCenterRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_cost_center_code_error_mapper,
            request_options=request_options,
        )

    def update_devices_custom_fields(
        self,
        body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesCustomFieldsErrorBody]:
        """Sends a CarrierService callback message for each device in the request when the custom fields have been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update custom field of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/customFields"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_custom_fields_error_mapper,
            request_options=request_options,
        )

    def update_devices_state(
        self, body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesStateErrorBody]:
        """Changes the provisioning state of one or more devices to a specified customer-defined service and state.

        Args:
            body: Request to change device state to one defined by the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/gotostate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GoToStateRequest | GoToStateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_state_error_mapper,
            request_options=request_options,
        )

    def upload_activate_device(
        self,
        body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UploadActivateDeviceErrorBody]:
        """Uploads and activates device identifiers and SKUs for new devices from OEMs to Verizon.

        Args:
            body: Request to Upload and Activate device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/uploadactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=upload_activate_device_error_mapper,
            request_options=request_options,
        )

    def usage_segmentation_label_association(
        self,
        body: AssociateLabelRequest | AssociateLabelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UsageSegmentationLabelAssociationErrorBody]:
        """Allows you to associate your own usage segmentation label with a device.

        Args:
            body: Request to associate a label to a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/usagesegmentationlabels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssociateLabelRequest | AssociateLabelRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=usage_segmentation_label_association_error_mapper,
            request_options=request_options,
        )

    def usage_segmentation_label_deletion(
        self,
        account_name: str,
        label_list: LabelsList | LabelsListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UsageSegmentationLabelDeletionErrorBody]:
        """Allow customers to remove the associated label from a device.

        Args:
            account_name: The numeric name of the account.
            label_list: A list of the Label IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/usagesegmentationlabels"),
            query_params=[
                param[str]("accountName", account_name), param[LabelsList | LabelsListDict]("LabelList", label_list)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=usage_segmentation_label_deletion_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_service_for_devices(
        self,
        body: CarrierActivateRequest | CarrierActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, ActivateServiceForDevicesErrorBody]:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Request for activating a service on devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierActivateRequest | CarrierActivateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=activate_service_for_devices_error_mapper,
            request_options=request_options,
        )

    async def add_devices(
        self, body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[AddDevicesResult], AddDevicesErrorBody]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/add"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddDevicesRequest | AddDevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[AddDevicesResult]],
            error_mapper=add_devices_error_mapper,
            request_options=request_options,
        )

    async def billed_usage_info(
        self,
        body: BilledusageListRequest | BilledusageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, BilledUsageInfoErrorBody]:
        """Gets billed usage for for either multiple devices or an entire billing account.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/billedusage/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BilledusageListRequest | BilledusageListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=billed_usage_info_error_mapper,
            request_options=request_options,
        )

    async def change_devices_service_plan(
        self,
        body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, ChangeDevicesServicePlanErrorBody]:
        """Changes the service plan for one or more devices.

        Args:
            body: Request to change device service plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/plan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePlanUpdateRequest | ServicePlanUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=change_devices_service_plan_error_mapper,
            request_options=request_options,
        )

    async def check_devices_availability_for_activation(
        self,
        body: DeviceActivationRequest | DeviceActivationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, CheckDevicesAvailabilityForActivationErrorBody]:
        """Checks whether specified devices are registered by the manufacturer with the Verizon network and are
        available to be activated.

        Args:
            body: Request to check if devices can be activated or not.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/availability/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceActivationRequest | DeviceActivationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=check_devices_availability_for_activation_error_mapper,
            request_options=request_options,
        )

    async def deactivate_service_for_devices(
        self,
        body: CarrierDeactivateRequest | CarrierDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DeactivateServiceForDevicesErrorBody]:
        """Deactivating service for a device may result in an early termination fee (ETF) being charged to the account,
        depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use
        one for a particular deactivation, set the etfWaiver value to True.

        Args:
            body: Request to deactivate service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierDeactivateRequest | CarrierDeactivateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=deactivate_service_for_devices_error_mapper,
            request_options=request_options,
        )

    async def delete_deactivated_devices(
        self,
        body: DeleteDevicesRequest | DeleteDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DeleteDevicesResult], DeleteDeactivatedDevicesErrorBody]:
        """Use this API to remove unneeded devices from an account.

        Args:
            body: Devices to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteDevicesRequest | DeleteDevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeleteDevicesResult]],
            error_mapper=delete_deactivated_devices_error_mapper,
            request_options=request_options,
        )

    async def device_upload(
        self,
        body: DeviceUploadRequest | DeviceUploadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DeviceUploadErrorBody]:
        """Upload a device record

        Args:
            body: Device Upload Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/upload"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceUploadRequest | DeviceUploadRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=device_upload_error_mapper,
            request_options=request_options,
        )

    async def device_upload_status(
        self,
        body: CheckOrderStatusRequest | CheckOrderStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DeviceUploadStatusErrorBody]:
        """Checks the status of an activation order and lists where the order is in the provisioning process.

        Args:
            body: The request body identifies the device and reporting period that you want included in the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/requests/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CheckOrderStatusRequest | CheckOrderStatusRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=device_upload_status_error_mapper,
            request_options=request_options,
        )

    async def get_device_extended_diagnostic_information(
        self,
        body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceExtendedDiagnosticsResult, GetDeviceExtendedDiagnosticInformationErrorBody]:
        """Returns extended diagnostic information about a specified device, including connectivity, provisioning,
        billing and location status.

        Args:
            body: Request to query extended diagnostics information for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/extendeddiagnostics/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceExtendedDiagnosticsResult],
            error_mapper=get_device_extended_diagnostic_information_error_mapper,
            request_options=request_options,
        )

    async def get_device_service_suspension_status(
        self,
        body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, GetDeviceServiceSuspensionStatusErrorBody]:
        """Returns DeviceSuspensionStatus callback messages containing the current device state and information on how
        many days a device has been suspended and can continue to be suspended.

        Args:
            body: Request to obtain service suspenstion status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/suspension/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=get_device_service_suspension_status_error_mapper,
            request_options=request_options,
        )

    async def list_current_devices_prl_version(
        self,
        body: DevicePrlListRequest | DevicePrlListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, ListCurrentDevicesPrlversionErrorBody]:
        """4G and GSM devices do not have a PRL.

        Args:
            body: Request to query device PRL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/prl/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DevicePrlListRequest | DevicePrlListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=list_current_devices_prlversion_error_mapper,
            request_options=request_options,
        )

    async def list_devices_information(
        self,
        body: AccountDeviceListRequest | AccountDeviceListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountDeviceListResult, ListDevicesInformationErrorBody]:
        """Returns information about a single device or information about all devices that match the given parameters.
        Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

        Args:
            body: Device information query.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountDeviceListRequest | AccountDeviceListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountDeviceListResult],
            error_mapper=list_devices_information_error_mapper,
            request_options=request_options,
        )

    async def list_devices_provisioning_history(
        self,
        body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DeviceProvisioningHistoryListResult], ListDevicesProvisioningHistoryErrorBody]:
        """Returns the provisioning history of a specified device during a specified time period.

        Args:
            body: Query to obtain device provisioning history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/history/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceProvisioningHistoryListResult]],
            error_mapper=list_devices_provisioning_history_error_mapper,
            request_options=request_options,
        )

    async def list_devices_usage_history(
        self,
        body: DeviceUsageListRequest | DeviceUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceUsageListResult, ListDevicesUsageHistoryErrorBody]:
        """Returns the network data usage history of a device during a specified time period.

        Args:
            body: Request to obtain usage history for a specific device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceUsageListRequest | DeviceUsageListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceUsageListResult],
            error_mapper=list_devices_usage_history_error_mapper,
            request_options=request_options,
        )

    async def list_devices_with_imei_iccid_mismatch(
        self,
        body: DeviceMismatchListRequest | DeviceMismatchListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceMismatchListResult, ListDevicesWithImeiIccidMismatchErrorBody]:
        """Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware)
        during a specified time frame.

        Args:
            body: Request to list devices with mismatched IMEIs and ICCIDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/list/imeiiccidmismatch"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceMismatchListRequest | DeviceMismatchListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceMismatchListResult],
            error_mapper=list_devices_with_imei_iccid_mismatch_error_mapper,
            request_options=request_options,
        )

    async def move_devices_within_accounts_of_profile(
        self, body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceManagementResult, MoveDevicesWithinAccountsOfProfileErrorBody]:
        """Move active devices from one billing account to another within a customer profile.

        Args:
            body: Request to move devices between accounts.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/move"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MoveDeviceRequest | MoveDeviceRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=move_devices_within_accounts_of_profile_error_mapper,
            request_options=request_options,
        )

    async def restore_service_for_suspended_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, RestoreServiceForSuspendedDevicesErrorBody]:
        """Restores service to one or more suspended devices.

        Args:
            body: Request to restore services of one or more suspended devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/restore"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierActionsRequest | CarrierActionsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=restore_service_for_suspended_devices_error_mapper,
            request_options=request_options,
        )

    async def retrieve_aggregate_device_usage_history(
        self,
        body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, RetrieveAggregateDeviceUsageHistoryErrorBody]:
        """The information is returned in a callback response, so you must register a URL for DeviceUsage callback
        messages using the POST /callbacks API.

        Args:
            body: A request to retrieve aggregated device usage history information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/list/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=retrieve_aggregate_device_usage_history_error_mapper,
            request_options=request_options,
        )

    async def retrieve_device_connection_history(
        self,
        body: DeviceConnectionListRequest | DeviceConnectionListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectionHistoryResult, RetrieveDeviceConnectionHistoryErrorBody]:
        """Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times,
        adjusting the earliest value each time to start where the previous request finished.

        Args:
            body: Query to retrieve device connection history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/connections/actions/listHistory"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceConnectionListRequest | DeviceConnectionListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectionHistoryResult],
            error_mapper=retrieve_device_connection_history_error_mapper,
            request_options=request_options,
        )

    async def suspend_service_for_devices(
        self,
        body: CarrierActionsRequest | CarrierActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, SuspendServiceForDevicesErrorBody]:
        """Suspends service for one or more devices.

        Args:
            body: Request to suspend service for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/suspend"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CarrierActionsRequest | CarrierActionsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=suspend_service_for_devices_error_mapper,
            request_options=request_options,
        )

    async def update_device_id(
        self,
        service_type: str,
        body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDeviceIdErrorBody]:
        """Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this
        request to transfer the line of service and the MDN to new hardware, or to change the MDN.

        Args:
            service_type: Identifier type.
            body: Request to update device id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/{serviceType}/actions/deviceId"),
            path_params=[param[str]("serviceType", service_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangeDeviceIdRequest | ChangeDeviceIdRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_device_id_error_mapper,
            request_options=request_options,
        )

    async def update_devices_contact_information(
        self,
        body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesContactInformationErrorBody]:
        """Sends a CarrierService callback message for each device in the request when the contact information has been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update contact information for devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/contactInfo"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ContactInfoUpdateRequest | ContactInfoUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_contact_information_error_mapper,
            request_options=request_options,
        )

    async def update_devices_cost_center_code(
        self,
        body: DeviceCostCenterRequest | DeviceCostCenterRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesCostCenterCodeErrorBody]:
        """Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or
        more devices.

        Args:
            body: Request to update cost center code value for one or more devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/costCenter"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceCostCenterRequest | DeviceCostCenterRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_cost_center_code_error_mapper,
            request_options=request_options,
        )

    async def update_devices_custom_fields(
        self,
        body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesCustomFieldsErrorBody]:
        """Sends a CarrierService callback message for each device in the request when the custom fields have been
        changed, or if there was a problem and the change could not be completed.

        Args:
            body: Request to update custom field of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/customFields"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_custom_fields_error_mapper,
            request_options=request_options,
        )

    async def update_devices_state(
        self, body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceManagementResult, UpdateDevicesStateErrorBody]:
        """Changes the provisioning state of one or more devices to a specified customer-defined service and state.

        Args:
            body: Request to change device state to one defined by the user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/gotostate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GoToStateRequest | GoToStateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=update_devices_state_error_mapper,
            request_options=request_options,
        )

    async def upload_activate_device(
        self,
        body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UploadActivateDeviceErrorBody]:
        """Uploads and activates device identifiers and SKUs for new devices from OEMs to Verizon.

        Args:
            body: Request to Upload and Activate device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/uploadactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=upload_activate_device_error_mapper,
            request_options=request_options,
        )

    async def usage_segmentation_label_association(
        self,
        body: AssociateLabelRequest | AssociateLabelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UsageSegmentationLabelAssociationErrorBody]:
        """Allows you to associate your own usage segmentation label with a device.

        Args:
            body: Request to associate a label to a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/usagesegmentationlabels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssociateLabelRequest | AssociateLabelRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=usage_segmentation_label_association_error_mapper,
            request_options=request_options,
        )

    async def usage_segmentation_label_deletion(
        self,
        account_name: str,
        label_list: LabelsList | LabelsListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, UsageSegmentationLabelDeletionErrorBody]:
        """Allow customers to remove the associated label from a device.

        Args:
            account_name: The numeric name of the account.
            label_list: A list of the Label IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/usagesegmentationlabels"),
            query_params=[
                param[str]("accountName", account_name), param[LabelsList | LabelsListDict]("LabelList", label_list)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=usage_segmentation_label_deletion_error_mapper,
            request_options=request_options,
        )
