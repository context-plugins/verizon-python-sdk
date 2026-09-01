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
from ..errors.get_campaign_device_status_error import (
    GetCampaignDeviceStatusErrorBody,
    get_campaign_device_status_error_mapper,
)
from ..errors.get_campaign_history_by_status_error import (
    GetCampaignHistoryByStatusErrorBody,
    get_campaign_history_by_status_error_mapper,
)
from ..errors.get_device_firmware_upgrade_history2_error import (
    GetDeviceFirmwareUpgradeHistory2ErrorBody,
    get_device_firmware_upgrade_history2_error_mapper,
)
from ..errors.list_account_devices2_error import ListAccountDevices2ErrorBody, list_account_devices2_error_mapper
from ..errors.list_available_software_error import ListAvailableSoftwareErrorBody, list_available_software_error_mapper
from ..models.device_software_upgrade import DeviceSoftwareUpgrade
from ..models.software_package import SoftwarePackage
from ..models.v2_account_device_list import V2AccountDeviceList
from ..models.v2_campaign_device import V2CampaignDevice
from ..models.v2_campaign_history import V2CampaignHistory
from ..server.server import Server


class SoftwareManagementReportsV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementReportsV2WithRawResponse(client, server, auth)

    def get_campaign_device_status(
        self,
        account: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2CampaignDevice:
        """The report endpoint allows user to get the full list of device of a campaign.

        Args:
            account: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return list of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_campaign_device_status(
            account, campaign_id, last_seen_device_id=last_seen_device_id, request_options=request_options
        ).unwrap()

    def get_campaign_history_by_status(
        self,
        account: str,
        campaign_status: str,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2CampaignHistory:
        """The report endpoint allows user to get campaign history of an account for specified status.

        Args:
            account: Account identifier.
            campaign_status: Status of the campaign.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return list of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_campaign_history_by_status(
            account, campaign_status, last_seen_campaign_id=last_seen_campaign_id, request_options=request_options
        ).unwrap()

    def get_device_firmware_upgrade_history2(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceSoftwareUpgrade]:
        """The endpoint allows user to get software upgrade history of a device based on device IMEI.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of upgrades.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_device_firmware_upgrade_history2(
            account, device_id, request_options=request_options
        ).unwrap()

    def list_account_devices2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        distribution_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2AccountDeviceList:
        """The device endpoint gets devices information of an account.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            distribution_type: Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.list_account_devices2(
            account,
            last_seen_device_id=last_seen_device_id,
            distribution_type=distribution_type,
            request_options=request_options,
        ).unwrap()

    def list_available_software(
        self, account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[SoftwarePackage]:
        """This endpoint allows user to list a certain type of software of an account.

        Args:
            account: Account identifier.
            distribution_type: Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of software.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.list_available_software(
            account, distribution_type=distribution_type, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementReportsV2WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementReportsV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementReportsV2WithRawResponse(client, server, auth)

    async def get_campaign_device_status(
        self,
        account: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2CampaignDevice:
        """The report endpoint allows user to get the full list of device of a campaign.

        Args:
            account: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return list of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_campaign_device_status(
                account, campaign_id, last_seen_device_id=last_seen_device_id, request_options=request_options
            )
        ).unwrap()

    async def get_campaign_history_by_status(
        self,
        account: str,
        campaign_status: str,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2CampaignHistory:
        """The report endpoint allows user to get campaign history of an account for specified status.

        Args:
            account: Account identifier.
            campaign_status: Status of the campaign.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return list of campaign history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_campaign_history_by_status(
                account, campaign_status, last_seen_campaign_id=last_seen_campaign_id, request_options=request_options
            )
        ).unwrap()

    async def get_device_firmware_upgrade_history2(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceSoftwareUpgrade]:
        """The endpoint allows user to get software upgrade history of a device based on device IMEI.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of upgrades.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_device_firmware_upgrade_history2(
                account, device_id, request_options=request_options
            )
        ).unwrap()

    async def list_account_devices2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        distribution_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2AccountDeviceList:
        """The device endpoint gets devices information of an account.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            distribution_type: Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.list_account_devices2(
                account,
                last_seen_device_id=last_seen_device_id,
                distribution_type=distribution_type,
                request_options=request_options,
            )
        ).unwrap()

    async def list_available_software(
        self, account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[SoftwarePackage]:
        """This endpoint allows user to list a certain type of software of an account.

        Args:
            account: Account identifier.
            distribution_type: Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return array of software.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.list_available_software(
                account, distribution_type=distribution_type, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementReportsV2WithRawResponse:
        return self._with_raw_response


class SoftwareManagementReportsV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_campaign_device_status(
        self,
        account: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2CampaignDevice, GetCampaignDeviceStatusErrorBody]:
        """The report endpoint allows user to get the full list of device of a campaign.

        Args:
            account: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/reports/{account}/campaigns/{campaignId}/devices"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2CampaignDevice],
            error_mapper=get_campaign_device_status_error_mapper,
            request_options=request_options,
        )

    def get_campaign_history_by_status(
        self,
        account: str,
        campaign_status: str,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2CampaignHistory, GetCampaignHistoryByStatusErrorBody]:
        """The report endpoint allows user to get campaign history of an account for specified status.

        Args:
            account: Account identifier.
            campaign_status: Status of the campaign.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/reports/{account}/campaigns"),
            path_params=[param[str]("account", account)],
            query_params=[
                param[str]("campaignStatus", campaign_status),
                param[str | None]("lastSeenCampaignId", last_seen_campaign_id),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2CampaignHistory],
            error_mapper=get_campaign_history_by_status_error_mapper,
            request_options=request_options,
        )

    def get_device_firmware_upgrade_history2(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceSoftwareUpgrade], GetDeviceFirmwareUpgradeHistory2ErrorBody]:
        """The endpoint allows user to get software upgrade history of a device based on device IMEI.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/reports/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceSoftwareUpgrade]],
            error_mapper=get_device_firmware_upgrade_history2_error_mapper,
            request_options=request_options,
        )

    def list_account_devices2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        distribution_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2AccountDeviceList, ListAccountDevices2ErrorBody]:
        """The device endpoint gets devices information of an account.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            distribution_type: Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/devices/{account}"),
            path_params=[param[str]("account", account)],
            query_params=[
                param[str | None]("lastSeenDeviceId", last_seen_device_id),
                param[str | None]("distributionType", distribution_type),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2AccountDeviceList],
            error_mapper=list_account_devices2_error_mapper,
            request_options=request_options,
        )

    def list_available_software(
        self, account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SoftwarePackage], ListAvailableSoftwareErrorBody]:
        """This endpoint allows user to list a certain type of software of an account.

        Args:
            account: Account identifier.
            distribution_type: Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/software/{account}"),
            path_params=[param[str]("account", account)],
            query_params=[param[str | None]("distributionType", distribution_type)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[SoftwarePackage]],
            error_mapper=list_available_software_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementReportsV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_campaign_device_status(
        self,
        account: str,
        campaign_id: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2CampaignDevice, GetCampaignDeviceStatusErrorBody]:
        """The report endpoint allows user to get the full list of device of a campaign.

        Args:
            account: Account identifier.
            campaign_id: Campaign identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/reports/{account}/campaigns/{campaignId}/devices"),
            path_params=[param[str]("account", account), param[str]("campaignId", campaign_id)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2CampaignDevice],
            error_mapper=get_campaign_device_status_error_mapper,
            request_options=request_options,
        )

    async def get_campaign_history_by_status(
        self,
        account: str,
        campaign_status: str,
        *,
        last_seen_campaign_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2CampaignHistory, GetCampaignHistoryByStatusErrorBody]:
        """The report endpoint allows user to get campaign history of an account for specified status.

        Args:
            account: Account identifier.
            campaign_status: Status of the campaign.
            last_seen_campaign_id: Last seen campaign Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/reports/{account}/campaigns"),
            path_params=[param[str]("account", account)],
            query_params=[
                param[str]("campaignStatus", campaign_status),
                param[str | None]("lastSeenCampaignId", last_seen_campaign_id),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2CampaignHistory],
            error_mapper=get_campaign_history_by_status_error_mapper,
            request_options=request_options,
        )

    async def get_device_firmware_upgrade_history2(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceSoftwareUpgrade], GetDeviceFirmwareUpgradeHistory2ErrorBody]:
        """The endpoint allows user to get software upgrade history of a device based on device IMEI.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/reports/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceSoftwareUpgrade]],
            error_mapper=get_device_firmware_upgrade_history2_error_mapper,
            request_options=request_options,
        )

    async def list_account_devices2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        distribution_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2AccountDeviceList, ListAccountDevices2ErrorBody]:
        """The device endpoint gets devices information of an account.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            distribution_type: Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/devices/{account}"),
            path_params=[param[str]("account", account)],
            query_params=[
                param[str | None]("lastSeenDeviceId", last_seen_device_id),
                param[str | None]("distributionType", distribution_type),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2AccountDeviceList],
            error_mapper=list_account_devices2_error_mapper,
            request_options=request_options,
        )

    async def list_available_software(
        self, account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SoftwarePackage], ListAvailableSoftwareErrorBody]:
        """This endpoint allows user to list a certain type of software of an account.

        Args:
            account: Account identifier.
            distribution_type: Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/software/{account}"),
            path_params=[param[str]("account", account)],
            query_params=[param[str | None]("distributionType", distribution_type)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[SoftwarePackage]],
            error_mapper=list_available_software_error_mapper,
            request_options=request_options,
        )
