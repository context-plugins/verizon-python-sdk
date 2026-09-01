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
from ..errors.cancel_scheduled_firmware_upgrade_error import (
    CancelScheduledFirmwareUpgradeErrorBody,
    cancel_scheduled_firmware_upgrade_error_mapper,
)
from ..errors.list_available_firmware_error import ListAvailableFirmwareErrorBody, list_available_firmware_error_mapper
from ..errors.list_firmware_upgrade_details_error import (
    ListFirmwareUpgradeDetailsErrorBody,
    list_firmware_upgrade_details_error_mapper,
)
from ..errors.schedule_firmware_upgrade_error import (
    ScheduleFirmwareUpgradeErrorBody,
    schedule_firmware_upgrade_error_mapper,
)
from ..errors.update_firmware_upgrade_devices_error import (
    UpdateFirmwareUpgradeDevicesErrorBody,
    update_firmware_upgrade_devices_error_mapper,
)
from ..models.firmware import Firmware
from ..models.firmware_upgrade import FirmwareUpgrade
from ..models.firmware_upgrade_change_result import FirmwareUpgradeChangeResult
from ..models.firmware_upgrade_request import FirmwareUpgradeRequest, FirmwareUpgradeRequestDict
from ..models.fota_v1_success_result import FotaV1SuccessResult
from ..server.server import Server


class FirmwareV1:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FirmwareV1WithRawResponse(client, server, auth)

    def cancel_scheduled_firmware_upgrade(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV1SuccessResult:
        """Cancel a scheduled firmware upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the scheduled upgrade that you want to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upgrade canceled.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.cancel_scheduled_firmware_upgrade(
            account_name, upgrade_id, request_options=request_options
        ).unwrap()

    def list_available_firmware(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Firmware]:
        """Lists all device firmware images available for an account, based on the devices registered to that account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of available firmware.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.list_available_firmware(account, request_options=request_options).unwrap()

    def list_firmware_upgrade_details(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FirmwareUpgrade:
        """Returns information about a specified upgrade, include the target date of the upgrade, the list of devices in
        the upgrade, and the status of the upgrade for each device.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Firmware upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.list_firmware_upgrade_details(
            account_name, upgrade_id, request_options=request_options
        ).unwrap()

    def schedule_firmware_upgrade(
        self,
        body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FirmwareUpgrade:
        """Schedules a firmware upgrade for devices.

        Args:
            body: Details of the firmware upgrade request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Confirmation of successful firmware upgrade.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.schedule_firmware_upgrade(body, request_options=request_options).unwrap()

    def update_firmware_upgrade_devices(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FirmwareUpgradeChangeResult:
        """Add or remove devices from a scheduled upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.update_firmware_upgrade_devices(
            account_name, upgrade_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> FirmwareV1WithRawResponse:
        return self._with_raw_response


class AsyncFirmwareV1:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFirmwareV1WithRawResponse(client, server, auth)

    async def cancel_scheduled_firmware_upgrade(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV1SuccessResult:
        """Cancel a scheduled firmware upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the scheduled upgrade that you want to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upgrade canceled.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.cancel_scheduled_firmware_upgrade(
                account_name, upgrade_id, request_options=request_options
            )
        ).unwrap()

    async def list_available_firmware(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Firmware]:
        """Lists all device firmware images available for an account, based on the devices registered to that account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of available firmware.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.list_available_firmware(account, request_options=request_options)
        ).unwrap()

    async def list_firmware_upgrade_details(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FirmwareUpgrade:
        """Returns information about a specified upgrade, include the target date of the upgrade, the list of devices in
        the upgrade, and the status of the upgrade for each device.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Firmware upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.list_firmware_upgrade_details(
                account_name, upgrade_id, request_options=request_options
            )
        ).unwrap()

    async def schedule_firmware_upgrade(
        self,
        body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FirmwareUpgrade:
        """Schedules a firmware upgrade for devices.

        Args:
            body: Details of the firmware upgrade request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Confirmation of successful firmware upgrade.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (await self._with_raw_response.schedule_firmware_upgrade(body, request_options=request_options)).unwrap()

    async def update_firmware_upgrade_devices(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FirmwareUpgradeChangeResult:
        """Add or remove devices from a scheduled upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upgrade information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.update_firmware_upgrade_devices(
                account_name, upgrade_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFirmwareV1WithRawResponse:
        return self._with_raw_response


class FirmwareV1WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_scheduled_firmware_upgrade(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV1SuccessResult, CancelScheduledFirmwareUpgradeErrorBody]:
        """Cancel a scheduled firmware upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the scheduled upgrade that you want to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v1("/upgrades/{accountName}/upgrade/{upgradeId}"),
            path_params=[param[str]("accountName", account_name), param[str]("upgradeId", upgrade_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV1SuccessResult],
            error_mapper=cancel_scheduled_firmware_upgrade_error_mapper,
            request_options=request_options,
        )

    def list_available_firmware(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Firmware], ListAvailableFirmwareErrorBody]:
        """Lists all device firmware images available for an account, based on the devices registered to that account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/firmware/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Firmware]],
            error_mapper=list_available_firmware_error_mapper,
            request_options=request_options,
        )

    def list_firmware_upgrade_details(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FirmwareUpgrade, ListFirmwareUpgradeDetailsErrorBody]:
        """Returns information about a specified upgrade, include the target date of the upgrade, the list of devices in
        the upgrade, and the status of the upgrade for each device.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/upgrades/{accountName}/upgrade/{upgradeId}"),
            path_params=[param[str]("accountName", account_name), param[str]("upgradeId", upgrade_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareUpgrade],
            error_mapper=list_firmware_upgrade_details_error_mapper,
            request_options=request_options,
        )

    def schedule_firmware_upgrade(
        self,
        body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FirmwareUpgrade, ScheduleFirmwareUpgradeErrorBody]:
        """Schedules a firmware upgrade for devices.

        Args:
            body: Details of the firmware upgrade request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/upgrades"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FirmwareUpgradeRequest | FirmwareUpgradeRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareUpgrade],
            error_mapper=schedule_firmware_upgrade_error_mapper,
            request_options=request_options,
        )

    def update_firmware_upgrade_devices(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FirmwareUpgradeChangeResult, UpdateFirmwareUpgradeDevicesErrorBody]:
        """Add or remove devices from a scheduled upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v1("/upgrades/{accountName}/upgrade/{upgradeId}"),
            path_params=[param[str]("accountName", account_name), param[str]("upgradeId", upgrade_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareUpgradeChangeResult],
            error_mapper=update_firmware_upgrade_devices_error_mapper,
            request_options=request_options,
        )


class AsyncFirmwareV1WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_scheduled_firmware_upgrade(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV1SuccessResult, CancelScheduledFirmwareUpgradeErrorBody]:
        """Cancel a scheduled firmware upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the scheduled upgrade that you want to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v1("/upgrades/{accountName}/upgrade/{upgradeId}"),
            path_params=[param[str]("accountName", account_name), param[str]("upgradeId", upgrade_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV1SuccessResult],
            error_mapper=cancel_scheduled_firmware_upgrade_error_mapper,
            request_options=request_options,
        )

    async def list_available_firmware(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Firmware], ListAvailableFirmwareErrorBody]:
        """Lists all device firmware images available for an account, based on the devices registered to that account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/firmware/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Firmware]],
            error_mapper=list_available_firmware_error_mapper,
            request_options=request_options,
        )

    async def list_firmware_upgrade_details(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FirmwareUpgrade, ListFirmwareUpgradeDetailsErrorBody]:
        """Returns information about a specified upgrade, include the target date of the upgrade, the list of devices in
        the upgrade, and the status of the upgrade for each device.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/upgrades/{accountName}/upgrade/{upgradeId}"),
            path_params=[param[str]("accountName", account_name), param[str]("upgradeId", upgrade_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareUpgrade],
            error_mapper=list_firmware_upgrade_details_error_mapper,
            request_options=request_options,
        )

    async def schedule_firmware_upgrade(
        self,
        body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FirmwareUpgrade, ScheduleFirmwareUpgradeErrorBody]:
        """Schedules a firmware upgrade for devices.

        Args:
            body: Details of the firmware upgrade request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/upgrades"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FirmwareUpgradeRequest | FirmwareUpgradeRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareUpgrade],
            error_mapper=schedule_firmware_upgrade_error_mapper,
            request_options=request_options,
        )

    async def update_firmware_upgrade_devices(
        self, account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FirmwareUpgradeChangeResult, UpdateFirmwareUpgradeDevicesErrorBody]:
        """Add or remove devices from a scheduled upgrade.

        Args:
            account_name: Account identifier in "##########-#####".
            upgrade_id: The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v1("/upgrades/{accountName}/upgrade/{upgradeId}"),
            path_params=[param[str]("accountName", account_name), param[str]("upgradeId", upgrade_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FirmwareUpgradeChangeResult],
            error_mapper=update_firmware_upgrade_devices_error_mapper,
            request_options=request_options,
        )
