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
from ..errors.get_device_check_in_history_error import (
    GetDeviceCheckInHistoryErrorBody,
    get_device_check_in_history_error_mapper,
)
from ..models.check_in_history_item import CheckInHistoryItem
from ..server.server import Server


class ServerLogging:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ServerLoggingWithRawResponse(client, server, auth)

    def get_device_check_in_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CheckInHistoryItem]:
        """Check-in history can be retrieved for any device belonging to the account, not necessarily with logging
        enabled.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of check-in history entries.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_device_check_in_history(
            account, device_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ServerLoggingWithRawResponse:
        return self._with_raw_response


class AsyncServerLogging:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncServerLoggingWithRawResponse(client, server, auth)

    async def get_device_check_in_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CheckInHistoryItem]:
        """Check-in history can be retrieved for any device belonging to the account, not necessarily with logging
        enabled.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of check-in history entries.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_device_check_in_history(
                account, device_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncServerLoggingWithRawResponse:
        return self._with_raw_response


class ServerLoggingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_device_check_in_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CheckInHistoryItem], GetDeviceCheckInHistoryErrorBody]:
        """Check-in history can be retrieved for any device belonging to the account, not necessarily with logging
        enabled.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}/checkInHistory"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[CheckInHistoryItem]],
            error_mapper=get_device_check_in_history_error_mapper,
            request_options=request_options,
        )


class AsyncServerLoggingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_device_check_in_history(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CheckInHistoryItem], GetDeviceCheckInHistoryErrorBody]:
        """Check-in history can be retrieved for any device belonging to the account, not necessarily with logging
        enabled.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}/checkInHistory"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[CheckInHistoryItem]],
            error_mapper=get_device_check_in_history_error_mapper,
            request_options=request_options,
        )
