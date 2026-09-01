from __future__ import annotations

from uuid import UUID, uuid4

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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.device_reset_request import DeviceResetRequest, DeviceResetRequestDict
from ..models.diagnostics_observation_result import DiagnosticsObservationResult
from ..server.server import Server


class DiagnosticsFactoryReset:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DiagnosticsFactoryResetWithRawResponse(client, server, auth)

    def decives_restart(
        self, body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsObservationResult:
        """Performs a device reboot or a factory reset on the modem portion of the device.

        Args:
            body: A request to perform a device reboot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics observation result.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.decives_restart(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DiagnosticsFactoryResetWithRawResponse:
        return self._with_raw_response


class AsyncDiagnosticsFactoryReset:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDiagnosticsFactoryResetWithRawResponse(client, server, auth)

    async def decives_restart(
        self, body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsObservationResult:
        """Performs a device reboot or a factory reset on the modem portion of the device.

        Args:
            body: A request to perform a device reboot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics observation result.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.decives_restart(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiagnosticsFactoryResetWithRawResponse:
        return self._with_raw_response


class DiagnosticsFactoryResetWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def decives_restart(
        self, body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsObservationResult, RawError]:
        """Performs a device reboot or a factory reset on the modem portion of the device.

        Args:
            body: A request to perform a device reboot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/devices/actions/restart"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceResetRequest | DeviceResetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsObservationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDiagnosticsFactoryResetWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def decives_restart(
        self, body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsObservationResult, RawError]:
        """Performs a device reboot or a factory reset on the modem portion of the device.

        Args:
            body: A request to perform a device reboot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/devices/actions/restart"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceResetRequest | DeviceResetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsObservationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
