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
from ..errors.cancel_campaign_error import CancelCampaignErrorBody, cancel_campaign_error_mapper
from ..errors.get_campaign_information_error import (
    GetCampaignInformationErrorBody,
    get_campaign_information_error_mapper,
)
from ..errors.schedule_campaign_firmware_upgrade_error import (
    ScheduleCampaignFirmwareUpgradeErrorBody,
    schedule_campaign_firmware_upgrade_error_mapper,
)
from ..errors.schedule_file_upgrade_error import ScheduleFileUpgradeErrorBody, schedule_file_upgrade_error_mapper
from ..errors.schedule_swupgrade_http_devices_error import (
    ScheduleSwupgradeHttpDevicesErrorBody,
    schedule_swupgrade_http_devices_error_mapper,
)
from ..errors.update_campaign_dates_error import UpdateCampaignDatesErrorBody, update_campaign_dates_error_mapper
from ..errors.update_campaign_firmware_devices_error import (
    UpdateCampaignFirmwareDevicesErrorBody,
    update_campaign_firmware_devices_error_mapper,
)
from ..models.campaign_software import CampaignSoftware
from ..models.fota_v2_success_result import FotaV2SuccessResult
from ..models.schedules_software_upgrade_request import (
    SchedulesSoftwareUpgradeRequest,
    SchedulesSoftwareUpgradeRequestDict,
)
from ..models.upload_and_schedule_file_request import UploadAndScheduleFileRequest, UploadAndScheduleFileRequestDict
from ..models.upload_and_schedule_file_response import UploadAndScheduleFileResponse
from ..models.v2_add_or_remove_device_result import V2AddOrRemoveDeviceResult
from ..server.server import Server


class CampaignsV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CampaignsV2WithRawResponse(client, server, auth)

    def cancel_campaign(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2SuccessResult:
        """This endpoint allows user to cancel software upgrade. A software upgrade already started can not be
        cancelled.

        Args:
            account: Account identifier.
            campaign_id: Unique identifier of campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return cancellation status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.cancel_campaign(account, campaign_id, request_options=request_options).unwrap()

    def get_campaign_information(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CampaignSoftware:
        """This endpoint allows user to get information of a software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return software upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_campaign_information(
            account, campaign_id, request_options=request_options
        ).unwrap()

    def schedule_campaign_firmware_upgrade(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CampaignSoftware:
        """This endpoint allows user to schedule a software upgrade.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return software upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.schedule_campaign_firmware_upgrade(
            account, request_options=request_options
        ).unwrap()

    def schedule_file_upgrade(
        self,
        acc: str,
        body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadAndScheduleFileResponse:
        """You can upload configuration files and schedule them in a campaign to devices.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.schedule_file_upgrade(acc, body, request_options=request_options).unwrap()

    def schedule_sw_upgrade_http_devices(
        self,
        acc: str,
        body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadAndScheduleFileResponse:
        """Campaign time windows for downloading and installing software are available as long as the device OEM
        supports this.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.schedule_sw_upgrade_http_devices(
            acc, body, request_options=request_options
        ).unwrap()

    def update_campaign_dates(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CampaignSoftware:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated campaign information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.update_campaign_dates(
            account, campaign_id, request_options=request_options
        ).unwrap()

    def update_campaign_firmware_devices(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2AddOrRemoveDeviceResult:
        """This endpoint allows user to Add or Remove devices to an existing software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of adding or removing devices to existing software upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.update_campaign_firmware_devices(
            account, campaign_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CampaignsV2WithRawResponse:
        return self._with_raw_response


class AsyncCampaignsV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCampaignsV2WithRawResponse(client, server, auth)

    async def cancel_campaign(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2SuccessResult:
        """This endpoint allows user to cancel software upgrade. A software upgrade already started can not be
        cancelled.

        Args:
            account: Account identifier.
            campaign_id: Unique identifier of campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return cancellation status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.cancel_campaign(account, campaign_id, request_options=request_options)
        ).unwrap()

    async def get_campaign_information(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CampaignSoftware:
        """This endpoint allows user to get information of a software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return software upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_campaign_information(
                account, campaign_id, request_options=request_options
            )
        ).unwrap()

    async def schedule_campaign_firmware_upgrade(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CampaignSoftware:
        """This endpoint allows user to schedule a software upgrade.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return software upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.schedule_campaign_firmware_upgrade(account, request_options=request_options)
        ).unwrap()

    async def schedule_file_upgrade(
        self,
        acc: str,
        body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadAndScheduleFileResponse:
        """You can upload configuration files and schedule them in a campaign to devices.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.schedule_file_upgrade(acc, body, request_options=request_options)
        ).unwrap()

    async def schedule_sw_upgrade_http_devices(
        self,
        acc: str,
        body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadAndScheduleFileResponse:
        """Campaign time windows for downloading and installing software are available as long as the device OEM
        supports this.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.schedule_sw_upgrade_http_devices(acc, body, request_options=request_options)
        ).unwrap()

    async def update_campaign_dates(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CampaignSoftware:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated campaign information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.update_campaign_dates(account, campaign_id, request_options=request_options)
        ).unwrap()

    async def update_campaign_firmware_devices(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2AddOrRemoveDeviceResult:
        """This endpoint allows user to Add or Remove devices to an existing software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of adding or removing devices to existing software upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.update_campaign_firmware_devices(
                account, campaign_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCampaignsV2WithRawResponse:
        return self._with_raw_response


class CampaignsV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_campaign(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2SuccessResult, CancelCampaignErrorBody]:
        """This endpoint allows user to cancel software upgrade. A software upgrade already started can not be
        cancelled.

        Args:
            account: Account identifier.
            campaign_id: Unique identifier of campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2SuccessResult],
            error_mapper=cancel_campaign_error_mapper,
            request_options=request_options,
        )

    def get_campaign_information(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CampaignSoftware, GetCampaignInformationErrorBody]:
        """This endpoint allows user to get information of a software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CampaignSoftware],
            error_mapper=get_campaign_information_error_mapper,
            request_options=request_options,
        )

    def schedule_campaign_firmware_upgrade(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CampaignSoftware, ScheduleCampaignFirmwareUpgradeErrorBody]:
        """This endpoint allows user to schedule a software upgrade.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/campaigns/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CampaignSoftware],
            error_mapper=schedule_campaign_firmware_upgrade_error_mapper,
            request_options=request_options,
        )

    def schedule_file_upgrade(
        self,
        acc: str,
        body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadAndScheduleFileResponse, ScheduleFileUpgradeErrorBody]:
        """You can upload configuration files and schedule them in a campaign to devices.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/campaigns/files/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UploadAndScheduleFileResponse],
            error_mapper=schedule_file_upgrade_error_mapper,
            request_options=request_options,
        )

    def schedule_sw_upgrade_http_devices(
        self,
        acc: str,
        body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadAndScheduleFileResponse, ScheduleSwupgradeHttpDevicesErrorBody]:
        """Campaign time windows for downloading and installing software are available as long as the device OEM
        supports this.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/campaigns/software/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UploadAndScheduleFileResponse],
            error_mapper=schedule_swupgrade_http_devices_error_mapper,
            request_options=request_options,
        )

    def update_campaign_dates(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CampaignSoftware, UpdateCampaignDatesErrorBody]:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}/dates"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CampaignSoftware],
            error_mapper=update_campaign_dates_error_mapper,
            request_options=request_options,
        )

    def update_campaign_firmware_devices(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevicesErrorBody]:
        """This endpoint allows user to Add or Remove devices to an existing software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2AddOrRemoveDeviceResult],
            error_mapper=update_campaign_firmware_devices_error_mapper,
            request_options=request_options,
        )


class AsyncCampaignsV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_campaign(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2SuccessResult, CancelCampaignErrorBody]:
        """This endpoint allows user to cancel software upgrade. A software upgrade already started can not be
        cancelled.

        Args:
            account: Account identifier.
            campaign_id: Unique identifier of campaign.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2SuccessResult],
            error_mapper=cancel_campaign_error_mapper,
            request_options=request_options,
        )

    async def get_campaign_information(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CampaignSoftware, GetCampaignInformationErrorBody]:
        """This endpoint allows user to get information of a software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CampaignSoftware],
            error_mapper=get_campaign_information_error_mapper,
            request_options=request_options,
        )

    async def schedule_campaign_firmware_upgrade(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CampaignSoftware, ScheduleCampaignFirmwareUpgradeErrorBody]:
        """This endpoint allows user to schedule a software upgrade.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/campaigns/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CampaignSoftware],
            error_mapper=schedule_campaign_firmware_upgrade_error_mapper,
            request_options=request_options,
        )

    async def schedule_file_upgrade(
        self,
        acc: str,
        body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadAndScheduleFileResponse, ScheduleFileUpgradeErrorBody]:
        """You can upload configuration files and schedule them in a campaign to devices.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/campaigns/files/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UploadAndScheduleFileResponse],
            error_mapper=schedule_file_upgrade_error_mapper,
            request_options=request_options,
        )

    async def schedule_sw_upgrade_http_devices(
        self,
        acc: str,
        body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadAndScheduleFileResponse, ScheduleSwupgradeHttpDevicesErrorBody]:
        """Campaign time windows for downloading and installing software are available as long as the device OEM
        supports this.

        Args:
            acc: Account identifier.
            body: Device logging information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/campaigns/software/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UploadAndScheduleFileResponse],
            error_mapper=schedule_swupgrade_http_devices_error_mapper,
            request_options=request_options,
        )

    async def update_campaign_dates(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CampaignSoftware, UpdateCampaignDatesErrorBody]:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}/dates"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CampaignSoftware],
            error_mapper=update_campaign_dates_error_mapper,
            request_options=request_options,
        )

    async def update_campaign_firmware_devices(
        self, account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevicesErrorBody]:
        """This endpoint allows user to Add or Remove devices to an existing software upgrade.

        Args:
            account: Account identifier.
            campaign_id: Software upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/campaigns/{account}/{campaignId}"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2AddOrRemoveDeviceResult],
            error_mapper=update_campaign_firmware_devices_error_mapper,
            request_options=request_options,
        )
