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
from ..errors.cancel_campaign2_error import CancelCampaign2ErrorBody, cancel_campaign2_error_mapper
from ..errors.get_campaign_information2_error import (
    GetCampaignInformation2ErrorBody,
    get_campaign_information2_error_mapper,
)
from ..errors.schedule_campaign_firmware_upgrade2_error import (
    ScheduleCampaignFirmwareUpgrade2ErrorBody,
    schedule_campaign_firmware_upgrade2_error_mapper,
)
from ..errors.update_campaign_dates2_error import UpdateCampaignDates2ErrorBody, update_campaign_dates2_error_mapper
from ..errors.update_campaign_firmware_devices2_error import (
    UpdateCampaignFirmwareDevices2ErrorBody,
    update_campaign_firmware_devices2_error_mapper,
)
from ..models.campaign import Campaign
from ..models.campaign_firmware_upgrade import CampaignFirmwareUpgrade, CampaignFirmwareUpgradeDict
from ..models.firmware_campaign import FirmwareCampaign
from ..models.fota_v3_success_result import FotaV3SuccessResult
from ..models.v3_add_or_remove_device_request import V3AddOrRemoveDeviceRequest, V3AddOrRemoveDeviceRequestDict
from ..models.v3_add_or_remove_device_result import V3AddOrRemoveDeviceResult
from ..models.v3_change_campaign_dates_request import V3ChangeCampaignDatesRequest, V3ChangeCampaignDatesRequestDict
from ..server.server import Server


class CampaignsV3:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CampaignsV3WithRawResponse(client, server, auth)

    def cancel_campaign2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3SuccessResult:
        """This endpoint allows user to cancel a firmware campaign. A firmware campaign already started can not be
        cancelled.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns cancellation status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.cancel_campaign2(
            account_name, campaign_id, request_options=request_options
        ).unwrap()

    def get_campaign_information2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Campaign:
        """This endpoint allows the user to retrieve campaign level information for a specified campaign.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns firmware upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_campaign_information2(
            account_name, campaign_id, request_options=request_options
        ).unwrap()

    def schedule_campaign_firmware_upgrade2(
        self,
        account_name: str,
        body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FirmwareCampaign:
        """This endpoint allows a user to schedule a firmware upgrade for a list of devices.

        Args:
            account_name: Account identifier.
            body: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.schedule_campaign_firmware_upgrade2(
            account_name, body, request_options=request_options
        ).unwrap()

    def update_campaign_dates2(
        self,
        acc: str,
        campaign_id: str,
        body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FirmwareCampaign:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            acc: Account identifier.
            campaign_id: Firmware upgrade information.
            body: New dates and time windows.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated campaign information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.update_campaign_dates2(
            acc, campaign_id, body, request_options=request_options
        ).unwrap()

    def update_campaign_firmware_devices2(
        self,
        acc: str,
        campaign_id: str,
        body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3AddOrRemoveDeviceResult:
        """This endpoint allows user to Add or Remove devices to an existing campaign.

        Args:
            acc: Account identifier.
            campaign_id: Unique identifier of a campaign.
            body: Add or remove device to existing upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns add or remove devices to existing upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.update_campaign_firmware_devices2(
            acc, campaign_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CampaignsV3WithRawResponse:
        return self._with_raw_response


class AsyncCampaignsV3:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCampaignsV3WithRawResponse(client, server, auth)

    async def cancel_campaign2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3SuccessResult:
        """This endpoint allows user to cancel a firmware campaign. A firmware campaign already started can not be
        cancelled.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns cancellation status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.cancel_campaign2(account_name, campaign_id, request_options=request_options)
        ).unwrap()

    async def get_campaign_information2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Campaign:
        """This endpoint allows the user to retrieve campaign level information for a specified campaign.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns firmware upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_campaign_information2(
                account_name, campaign_id, request_options=request_options
            )
        ).unwrap()

    async def schedule_campaign_firmware_upgrade2(
        self,
        account_name: str,
        body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FirmwareCampaign:
        """This endpoint allows a user to schedule a firmware upgrade for a list of devices.

        Args:
            account_name: Account identifier.
            body: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.schedule_campaign_firmware_upgrade2(
                account_name, body, request_options=request_options
            )
        ).unwrap()

    async def update_campaign_dates2(
        self,
        acc: str,
        campaign_id: str,
        body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FirmwareCampaign:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            acc: Account identifier.
            campaign_id: Firmware upgrade information.
            body: New dates and time windows.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated campaign information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.update_campaign_dates2(
                acc, campaign_id, body, request_options=request_options
            )
        ).unwrap()

    async def update_campaign_firmware_devices2(
        self,
        acc: str,
        campaign_id: str,
        body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3AddOrRemoveDeviceResult:
        """This endpoint allows user to Add or Remove devices to an existing campaign.

        Args:
            acc: Account identifier.
            campaign_id: Unique identifier of a campaign.
            body: Add or remove device to existing upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns add or remove devices to existing upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.update_campaign_firmware_devices2(
                acc, campaign_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCampaignsV3WithRawResponse:
        return self._with_raw_response


class CampaignsV3WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_campaign2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3SuccessResult, CancelCampaign2ErrorBody]:
        """This endpoint allows user to cancel a firmware campaign. A firmware campaign already started can not be
        cancelled.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v3("/campaigns/{accountName}/{campaignId}"),
            path_params=[param[str]("accountName", account_name), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3SuccessResult],
            error_mapper=cancel_campaign2_error_mapper,
            request_options=request_options,
        )

    def get_campaign_information2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Campaign, GetCampaignInformation2ErrorBody]:
        """This endpoint allows the user to retrieve campaign level information for a specified campaign.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/campaigns/{accountName}/{campaignId}"),
            path_params=[param[str]("accountName", account_name), param[str]("campaignId", campaign_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Campaign],
            error_mapper=get_campaign_information2_error_mapper,
            request_options=request_options,
        )

    def schedule_campaign_firmware_upgrade2(
        self,
        account_name: str,
        body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FirmwareCampaign, ScheduleCampaignFirmwareUpgrade2ErrorBody]:
        """This endpoint allows a user to schedule a firmware upgrade for a list of devices.

        Args:
            account_name: Account identifier.
            body: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/campaigns/firmware/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareCampaign],
            error_mapper=schedule_campaign_firmware_upgrade2_error_mapper,
            request_options=request_options,
        )

    def update_campaign_dates2(
        self,
        acc: str,
        campaign_id: str,
        body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FirmwareCampaign, UpdateCampaignDates2ErrorBody]:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            acc: Account identifier.
            campaign_id: Firmware upgrade information.
            body: New dates and time windows.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/campaigns/firmware/{acc}/{campaignId}/dates"),
            path_params=[param[str]("acc", acc), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareCampaign],
            error_mapper=update_campaign_dates2_error_mapper,
            request_options=request_options,
        )

    def update_campaign_firmware_devices2(
        self,
        acc: str,
        campaign_id: str,
        body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevices2ErrorBody]:
        """This endpoint allows user to Add or Remove devices to an existing campaign.

        Args:
            acc: Account identifier.
            campaign_id: Unique identifier of a campaign.
            body: Add or remove device to existing upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/campaigns/firmware/{acc}/{campaignId}"),
            path_params=[param[str]("acc", acc), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3AddOrRemoveDeviceResult],
            error_mapper=update_campaign_firmware_devices2_error_mapper,
            request_options=request_options,
        )


class AsyncCampaignsV3WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_campaign2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3SuccessResult, CancelCampaign2ErrorBody]:
        """This endpoint allows user to cancel a firmware campaign. A firmware campaign already started can not be
        cancelled.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v3("/campaigns/{accountName}/{campaignId}"),
            path_params=[param[str]("accountName", account_name), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3SuccessResult],
            error_mapper=cancel_campaign2_error_mapper,
            request_options=request_options,
        )

    async def get_campaign_information2(
        self, account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Campaign, GetCampaignInformation2ErrorBody]:
        """This endpoint allows the user to retrieve campaign level information for a specified campaign.

        Args:
            account_name: Account identifier.
            campaign_id: Firmware upgrade identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/campaigns/{accountName}/{campaignId}"),
            path_params=[param[str]("accountName", account_name), param[str]("campaignId", campaign_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Campaign],
            error_mapper=get_campaign_information2_error_mapper,
            request_options=request_options,
        )

    async def schedule_campaign_firmware_upgrade2(
        self,
        account_name: str,
        body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FirmwareCampaign, ScheduleCampaignFirmwareUpgrade2ErrorBody]:
        """This endpoint allows a user to schedule a firmware upgrade for a list of devices.

        Args:
            account_name: Account identifier.
            body: Firmware upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/campaigns/firmware/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareCampaign],
            error_mapper=schedule_campaign_firmware_upgrade2_error_mapper,
            request_options=request_options,
        )

    async def update_campaign_dates2(
        self,
        acc: str,
        campaign_id: str,
        body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FirmwareCampaign, UpdateCampaignDates2ErrorBody]:
        """This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged
        should be also provided.

        Args:
            acc: Account identifier.
            campaign_id: Firmware upgrade information.
            body: New dates and time windows.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/campaigns/firmware/{acc}/{campaignId}/dates"),
            path_params=[param[str]("acc", acc), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareCampaign],
            error_mapper=update_campaign_dates2_error_mapper,
            request_options=request_options,
        )

    async def update_campaign_firmware_devices2(
        self,
        acc: str,
        campaign_id: str,
        body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevices2ErrorBody]:
        """This endpoint allows user to Add or Remove devices to an existing campaign.

        Args:
            acc: Account identifier.
            campaign_id: Unique identifier of a campaign.
            body: Add or remove device to existing upgrade information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/campaigns/firmware/{acc}/{campaignId}"),
            path_params=[param[str]("acc", acc), param[str]("campaignId", campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3AddOrRemoveDeviceResult],
            error_mapper=update_campaign_firmware_devices2_error_mapper,
            request_options=request_options,
        )
