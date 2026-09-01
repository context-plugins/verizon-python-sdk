from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_campaign_device_status2_error import (
    GetCampaignDeviceStatus2ErrorBody,
    get_campaign_device_status2_error_mapper,
)
from ..errors.get_campaign_history_by_status2_error import (
    GetCampaignHistoryByStatus2ErrorBody,
    get_campaign_history_by_status2_error_mapper,
)
from ..errors.get_device_firmware_upgrade_history3_error import (
    GetDeviceFirmwareUpgradeHistory3ErrorBody,
    get_device_firmware_upgrade_history3_error_mapper,
)
from ..models.device_firmware_upgrade import DeviceFirmwareUpgrade
from ..models.enums.campaign_status import CampaignStatusOrStr
from ..models.v3_campaign_device import V3CampaignDevice
from ..models.v3_campaign_history import V3CampaignHistory
from ..server.server import Server


class SoftwareManagementReportsV3:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementReportsV3WithRawResponse(client, server, auth)

    def get_campaign_device_status2(
        self,
        acc: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3CampaignDevice:
        """Retrieve a list of all devices in a campaign and the status of each device.

        Args:
            acc: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_campaign_device_status2(
            acc, campaign_id, last_seen_device_id=last_seen_device_id, request_options=request_options
        ).unwrap()

    def get_campaign_history_by_status2(
        self,
        acc: str,
        campaign_status: CampaignStatusOrStr,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3CampaignHistory:
        """Retrieve a list of campaigns for an account that have a specified campaign status.

        Args:
            acc: Account identifier.
            campaign_status: Campaign status.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_campaign_history_by_status2(
            acc, campaign_status, last_seen_campaign_id=last_seen_campaign_id, request_options=request_options
        ).unwrap()

    def get_device_firmware_upgrade_history3(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceFirmwareUpgrade]:
        """Retrieve campaign history for a specific device.

        Args:
            acc: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns a list of firmware upgrades.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_device_firmware_upgrade_history3(
            acc, device_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementReportsV3WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementReportsV3:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementReportsV3WithRawResponse(client, server, auth)

    async def get_campaign_device_status2(
        self,
        acc: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3CampaignDevice:
        """Retrieve a list of all devices in a campaign and the status of each device.

        Args:
            acc: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_campaign_device_status2(
                acc, campaign_id, last_seen_device_id=last_seen_device_id, request_options=request_options
            )
        ).unwrap()

    async def get_campaign_history_by_status2(
        self,
        acc: str,
        campaign_status: CampaignStatusOrStr,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3CampaignHistory:
        """Retrieve a list of campaigns for an account that have a specified campaign status.

        Args:
            acc: Account identifier.
            campaign_status: Campaign status.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_campaign_history_by_status2(
                acc, campaign_status, last_seen_campaign_id=last_seen_campaign_id, request_options=request_options
            )
        ).unwrap()

    async def get_device_firmware_upgrade_history3(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceFirmwareUpgrade]:
        """Retrieve campaign history for a specific device.

        Args:
            acc: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns a list of firmware upgrades.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_device_firmware_upgrade_history3(
                acc, device_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementReportsV3WithRawResponse:
        return self._with_raw_response


class SoftwareManagementReportsV3WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_campaign_device_status2(
        self,
        acc: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3CampaignDevice, GetCampaignDeviceStatus2ErrorBody]:
        """Retrieve a list of all devices in a campaign and the status of each device.

        Args:
            acc: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/reports/{acc}/campaigns/{campaignId}/devices"),
            path_params=[param[str]("acc", acc), param[str]("campaignId", campaign_id)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3CampaignDevice],
            error_mapper=get_campaign_device_status2_error_mapper,
            request_options=request_options,
        )

    def get_campaign_history_by_status2(
        self,
        acc: str,
        campaign_status: CampaignStatusOrStr,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3CampaignHistory, GetCampaignHistoryByStatus2ErrorBody]:
        """Retrieve a list of campaigns for an account that have a specified campaign status.

        Args:
            acc: Account identifier.
            campaign_status: Campaign status.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/reports/{acc}/firmware/campaigns"),
            path_params=[param[str]("acc", acc)],
            query_params=[
                param[CampaignStatusOrStr]("campaignStatus", campaign_status),
                param[str | None]("lastSeenCampaignId", last_seen_campaign_id),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3CampaignHistory],
            error_mapper=get_campaign_history_by_status2_error_mapper,
            request_options=request_options,
        )

    def get_device_firmware_upgrade_history3(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceFirmwareUpgrade], GetDeviceFirmwareUpgradeHistory3ErrorBody]:
        """Retrieve campaign history for a specific device.

        Args:
            acc: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/reports/{acc}/devices/{deviceId}"),
            path_params=[param[str]("acc", acc), param[str]("deviceId", device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceFirmwareUpgrade]],
            error_mapper=get_device_firmware_upgrade_history3_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementReportsV3WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_campaign_device_status2(
        self,
        acc: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3CampaignDevice, GetCampaignDeviceStatus2ErrorBody]:
        """Retrieve a list of all devices in a campaign and the status of each device.

        Args:
            acc: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/reports/{acc}/campaigns/{campaignId}/devices"),
            path_params=[param[str]("acc", acc), param[str]("campaignId", campaign_id)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3CampaignDevice],
            error_mapper=get_campaign_device_status2_error_mapper,
            request_options=request_options,
        )

    async def get_campaign_history_by_status2(
        self,
        acc: str,
        campaign_status: CampaignStatusOrStr,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3CampaignHistory, GetCampaignHistoryByStatus2ErrorBody]:
        """Retrieve a list of campaigns for an account that have a specified campaign status.

        Args:
            acc: Account identifier.
            campaign_status: Campaign status.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/reports/{acc}/firmware/campaigns"),
            path_params=[param[str]("acc", acc)],
            query_params=[
                param[CampaignStatusOrStr]("campaignStatus", campaign_status),
                param[str | None]("lastSeenCampaignId", last_seen_campaign_id),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3CampaignHistory],
            error_mapper=get_campaign_history_by_status2_error_mapper,
            request_options=request_options,
        )

    async def get_device_firmware_upgrade_history3(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceFirmwareUpgrade], GetDeviceFirmwareUpgradeHistory3ErrorBody]:
        """Retrieve campaign history for a specific device.

        Args:
            acc: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/reports/{acc}/devices/{deviceId}"),
            path_params=[param[str]("acc", acc), param[str]("deviceId", device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceFirmwareUpgrade]],
            error_mapper=get_device_firmware_upgrade_history3_error_mapper,
            request_options=request_options,
        )
