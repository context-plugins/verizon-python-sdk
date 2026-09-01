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
from ..models.diagnostics_subscription import DiagnosticsSubscription
from ..server.server import Server


class DiagnosticsSubscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DiagnosticsSubscriptionsWithRawResponse(client, server, auth)

    def get_diagnostics_subscription(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsSubscription:
        """This endpoint retrieves a diagnostics subscription by account.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics subscription response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_diagnostics_subscription(
            account_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DiagnosticsSubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncDiagnosticsSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDiagnosticsSubscriptionsWithRawResponse(client, server, auth)

    async def get_diagnostics_subscription(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsSubscription:
        """This endpoint retrieves a diagnostics subscription by account.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics subscription response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_diagnostics_subscription(account_name, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiagnosticsSubscriptionsWithRawResponse:
        return self._with_raw_response


class DiagnosticsSubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_diagnostics_subscription(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsSubscription, RawError]:
        """This endpoint retrieves a diagnostics subscription by account.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_diagnostics("/subscriptions"),
            query_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsSubscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDiagnosticsSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_diagnostics_subscription(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsSubscription, RawError]:
        """This endpoint retrieves a diagnostics subscription by account.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_diagnostics("/subscriptions"),
            query_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsSubscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
