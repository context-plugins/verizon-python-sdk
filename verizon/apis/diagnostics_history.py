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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.history import History
from ..server.server import Server


class DiagnosticsHistory:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DiagnosticsHistoryWithRawResponse(client, server, auth)

    def get_diagnostics_history(self, *, request_options: RequestOptionsOrDict | None = None) -> list[History]:
        """This endpoint allows the user to get the history data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History search response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_diagnostics_history(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DiagnosticsHistoryWithRawResponse:
        return self._with_raw_response


class AsyncDiagnosticsHistory:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDiagnosticsHistoryWithRawResponse(client, server, auth)

    async def get_diagnostics_history(self, *, request_options: RequestOptionsOrDict | None = None) -> list[History]:
        """This endpoint allows the user to get the history data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History search response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_diagnostics_history(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiagnosticsHistoryWithRawResponse:
        return self._with_raw_response


class DiagnosticsHistoryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_diagnostics_history(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[History], RawError]:
        """This endpoint allows the user to get the history data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/history/actions/$search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[History]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDiagnosticsHistoryWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_diagnostics_history(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[History], RawError]:
        """This endpoint allows the user to get the history data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/history/actions/$search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[History]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
