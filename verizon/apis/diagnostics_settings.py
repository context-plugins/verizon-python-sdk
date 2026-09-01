from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.diagnostic_observation_setting import DiagnosticObservationSetting
from ..server.server import Server


class DiagnosticsSettings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DiagnosticsSettingsWithRawResponse(client, server, auth)

    def list_diagnostics_settings(
        self, account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DiagnosticObservationSetting]:
        """This endpoint retrieves diagnostics settings synchronously.

        Args:
            account_name: Account identifier.
            devices: Devices list formatted as "id, kind"
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostic settings.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_diagnostics_settings(
            account_name, devices, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DiagnosticsSettingsWithRawResponse:
        return self._with_raw_response


class AsyncDiagnosticsSettings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDiagnosticsSettingsWithRawResponse(client, server, auth)

    async def list_diagnostics_settings(
        self, account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DiagnosticObservationSetting]:
        """This endpoint retrieves diagnostics settings synchronously.

        Args:
            account_name: Account identifier.
            devices: Devices list formatted as "id, kind"
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostic settings.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_diagnostics_settings(
                account_name, devices, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiagnosticsSettingsWithRawResponse:
        return self._with_raw_response


class DiagnosticsSettingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_diagnostics_settings(
        self, account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DiagnosticObservationSetting], RawError]:
        """This endpoint retrieves diagnostics settings synchronously.

        Args:
            account_name: Account identifier.
            devices: Devices list formatted as "id, kind"
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_diagnostics("/devices/settings"),
            query_params=[param[str]("accountName", account_name), param[str]("devices", devices)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DiagnosticObservationSetting]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDiagnosticsSettingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_diagnostics_settings(
        self, account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DiagnosticObservationSetting], RawError]:
        """This endpoint retrieves diagnostics settings synchronously.

        Args:
            account_name: Account identifier.
            devices: Devices list formatted as "id, kind"
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_diagnostics("/devices/settings"),
            query_params=[param[str]("accountName", account_name), param[str]("devices", devices)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DiagnosticObservationSetting]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
