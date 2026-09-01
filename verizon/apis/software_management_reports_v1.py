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
from ..errors.get_device_firmware_upgrade_history_error import (
    GetDeviceFirmwareUpgradeHistoryErrorBody,
    get_device_firmware_upgrade_history_error_mapper,
)
from ..errors.list_account_devices_error import ListAccountDevicesErrorBody, list_account_devices_error_mapper
from ..errors.list_upgrades_for_specified_status_error import (
    ListUpgradesForSpecifiedStatusErrorBody,
    list_upgrades_for_specified_status_error_mapper,
)
from ..models.device_list_query_result import DeviceListQueryResult
from ..models.device_upgrade_history import DeviceUpgradeHistory
from ..models.enums.upgrade_status import UpgradeStatusOrStr
from ..models.upgrade_list_query_result import UpgradeListQueryResult
from ..server.server import Server


class SoftwareManagementReportsV1:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementReportsV1WithRawResponse(client, server, auth)

    def get_device_firmware_upgrade_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceUpgradeHistory]:
        """Returns the upgrade history of the specified device from the previous six months.

        Args:
            account: Account identifier in "##########-#####".
            device_id: The IMEI of the device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device upgrade history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.get_device_firmware_upgrade_history(
            account, device_id, request_options=request_options
        ).unwrap()

    def list_account_devices(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceListQueryResult:
        """Returns an array of all devices in the specified account. Each device object includes information needed for
        managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

        Args:
            account: Account identifier in "##########-#####".
            start_index: Only return devices with IMEIs larger than this value. Use 0 for the first request. If
                ``hasMoreData``=true in the response, use the ``lastSeenDeviceId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of all devices in the specified account.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.list_account_devices(
            account, start_index, request_options=request_options
        ).unwrap()

    def list_upgrades_for_specified_status(
        self,
        account: str,
        upgrade_status: UpgradeStatusOrStr,
        start_index: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpgradeListQueryResult:
        """Returns a list of all upgrades with a specified status.

        Args:
            account: Account identifier in "##########-#####".
            upgrade_status: The status of the upgrades that you want to retrieve.
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                ``hasMoreFlag``=true in the response, use the ``lastSeenUpgradeId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of all upgrades with a specified status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.list_upgrades_for_specified_status(
            account, upgrade_status, start_index, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementReportsV1WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementReportsV1:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementReportsV1WithRawResponse(client, server, auth)

    async def get_device_firmware_upgrade_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceUpgradeHistory]:
        """Returns the upgrade history of the specified device from the previous six months.

        Args:
            account: Account identifier in "##########-#####".
            device_id: The IMEI of the device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device upgrade history.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.get_device_firmware_upgrade_history(
                account, device_id, request_options=request_options
            )
        ).unwrap()

    async def list_account_devices(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceListQueryResult:
        """Returns an array of all devices in the specified account. Each device object includes information needed for
        managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

        Args:
            account: Account identifier in "##########-#####".
            start_index: Only return devices with IMEIs larger than this value. Use 0 for the first request. If
                ``hasMoreData``=true in the response, use the ``lastSeenDeviceId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of all devices in the specified account.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.list_account_devices(account, start_index, request_options=request_options)
        ).unwrap()

    async def list_upgrades_for_specified_status(
        self,
        account: str,
        upgrade_status: UpgradeStatusOrStr,
        start_index: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpgradeListQueryResult:
        """Returns a list of all upgrades with a specified status.

        Args:
            account: Account identifier in "##########-#####".
            upgrade_status: The status of the upgrades that you want to retrieve.
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                ``hasMoreFlag``=true in the response, use the ``lastSeenUpgradeId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of all upgrades with a specified status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.list_upgrades_for_specified_status(
                account, upgrade_status, start_index, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementReportsV1WithRawResponse:
        return self._with_raw_response


class SoftwareManagementReportsV1WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_device_firmware_upgrade_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceUpgradeHistory], GetDeviceFirmwareUpgradeHistoryErrorBody]:
        """Returns the upgrade history of the specified device from the previous six months.

        Args:
            account: Account identifier in "##########-#####".
            device_id: The IMEI of the device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/reports/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceUpgradeHistory]],
            error_mapper=get_device_firmware_upgrade_history_error_mapper,
            request_options=request_options,
        )

    def list_account_devices(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceListQueryResult, ListAccountDevicesErrorBody]:
        """Returns an array of all devices in the specified account. Each device object includes information needed for
        managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

        Args:
            account: Account identifier in "##########-#####".
            start_index: Only return devices with IMEIs larger than this value. Use 0 for the first request. If
                ``hasMoreData``=true in the response, use the ``lastSeenDeviceId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/devices/{account}/index/{startIndex}"),
            path_params=[param[str]("account", account), param[str]("startIndex", start_index)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceListQueryResult],
            error_mapper=list_account_devices_error_mapper,
            request_options=request_options,
        )

    def list_upgrades_for_specified_status(
        self,
        account: str,
        upgrade_status: UpgradeStatusOrStr,
        start_index: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpgradeListQueryResult, ListUpgradesForSpecifiedStatusErrorBody]:
        """Returns a list of all upgrades with a specified status.

        Args:
            account: Account identifier in "##########-#####".
            upgrade_status: The status of the upgrades that you want to retrieve.
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                ``hasMoreFlag``=true in the response, use the ``lastSeenUpgradeId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1(
                "/reports/{account}/status/{upgradeStatus}/index/{startIndex}"
            ),
            path_params=[
                param[str]("account", account),
                param[UpgradeStatusOrStr]("upgradeStatus", upgrade_status),
                param[str]("startIndex", start_index),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UpgradeListQueryResult],
            error_mapper=list_upgrades_for_specified_status_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementReportsV1WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_device_firmware_upgrade_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceUpgradeHistory], GetDeviceFirmwareUpgradeHistoryErrorBody]:
        """Returns the upgrade history of the specified device from the previous six months.

        Args:
            account: Account identifier in "##########-#####".
            device_id: The IMEI of the device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/reports/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceUpgradeHistory]],
            error_mapper=get_device_firmware_upgrade_history_error_mapper,
            request_options=request_options,
        )

    async def list_account_devices(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceListQueryResult, ListAccountDevicesErrorBody]:
        """Returns an array of all devices in the specified account. Each device object includes information needed for
        managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

        Args:
            account: Account identifier in "##########-#####".
            start_index: Only return devices with IMEIs larger than this value. Use 0 for the first request. If
                ``hasMoreData``=true in the response, use the ``lastSeenDeviceId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/devices/{account}/index/{startIndex}"),
            path_params=[param[str]("account", account), param[str]("startIndex", start_index)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceListQueryResult],
            error_mapper=list_account_devices_error_mapper,
            request_options=request_options,
        )

    async def list_upgrades_for_specified_status(
        self,
        account: str,
        upgrade_status: UpgradeStatusOrStr,
        start_index: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpgradeListQueryResult, ListUpgradesForSpecifiedStatusErrorBody]:
        """Returns a list of all upgrades with a specified status.

        Args:
            account: Account identifier in "##########-#####".
            upgrade_status: The status of the upgrades that you want to retrieve.
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                ``hasMoreFlag``=true in the response, use the ``lastSeenUpgradeId`` value from the response as the
                startIndex in the next request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1(
                "/reports/{account}/status/{upgradeStatus}/index/{startIndex}"
            ),
            path_params=[
                param[str]("account", account),
                param[UpgradeStatusOrStr]("upgradeStatus", upgrade_status),
                param[str]("startIndex", start_index),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UpgradeListQueryResult],
            error_mapper=list_upgrades_for_specified_status_error_mapper,
            request_options=request_options,
        )
