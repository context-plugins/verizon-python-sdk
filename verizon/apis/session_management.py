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
from ..errors.end_connectivity_management_session_error import (
    EndConnectivityManagementSessionErrorBody,
    end_connectivity_management_session_error_mapper,
)
from ..errors.reset_connectivity_management_password_error import (
    ResetConnectivityManagementPasswordErrorBody,
    reset_connectivity_management_password_error_mapper,
)
from ..errors.start_connectivity_management_session_error import (
    StartConnectivityManagementSessionErrorBody,
    start_connectivity_management_session_error_mapper,
)
from ..models.log_in_request import LogInRequest, LogInRequestDict
from ..models.log_in_result import LogInResult
from ..models.log_out_request import LogOutRequest
from ..models.session_reset_password_request import SessionResetPasswordRequest, SessionResetPasswordRequestDict
from ..models.session_reset_password_result import SessionResetPasswordResult
from ..server.server import Server


class SessionManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SessionManagementWithRawResponse(client, server, auth)

    def end_connectivity_management_session(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> LogOutRequest:
        """Ends a Connectivity Management session.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VZ-M2M session token.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.end_connectivity_management_session(request_options=request_options).unwrap()

    def reset_connectivity_management_password(
        self,
        body: SessionResetPasswordRequest | SessionResetPasswordRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SessionResetPasswordResult:
        """The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your
        password every 90 days.

        Args:
            body: Request with current password that needs to be reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns a new, randomly generated password for the current username.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.reset_connectivity_management_password(
            body, request_options=request_options
        ).unwrap()

    def start_connectivity_management_session(
        self,
        *,
        body: LogInRequest | LogInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LogInResult:
        """Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent
        API requests.

        Args:
            body: Request to initiate a session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VZ-M2M session token.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.start_connectivity_management_session(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SessionManagementWithRawResponse:
        return self._with_raw_response


class AsyncSessionManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSessionManagementWithRawResponse(client, server, auth)

    async def end_connectivity_management_session(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> LogOutRequest:
        """Ends a Connectivity Management session.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VZ-M2M session token.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.end_connectivity_management_session(request_options=request_options)
        ).unwrap()

    async def reset_connectivity_management_password(
        self,
        body: SessionResetPasswordRequest | SessionResetPasswordRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SessionResetPasswordResult:
        """The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your
        password every 90 days.

        Args:
            body: Request with current password that needs to be reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns a new, randomly generated password for the current username.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.reset_connectivity_management_password(body, request_options=request_options)
        ).unwrap()

    async def start_connectivity_management_session(
        self,
        *,
        body: LogInRequest | LogInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LogInResult:
        """Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent
        API requests.

        Args:
            body: Request to initiate a session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            VZ-M2M session token.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.start_connectivity_management_session(
                body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSessionManagementWithRawResponse:
        return self._with_raw_response


class SessionManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def end_connectivity_management_session(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LogOutRequest, EndConnectivityManagementSessionErrorBody]:
        """Ends a Connectivity Management session.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/session/logout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[LogOutRequest],
            error_mapper=end_connectivity_management_session_error_mapper,
            request_options=request_options,
        )

    def reset_connectivity_management_password(
        self,
        body: SessionResetPasswordRequest | SessionResetPasswordRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SessionResetPasswordResult, ResetConnectivityManagementPasswordErrorBody]:
        """The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your
        password every 90 days.

        Args:
            body: Request with current password that needs to be reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/session/password/actions/reset"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SessionResetPasswordRequest | SessionResetPasswordRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SessionResetPasswordResult],
            error_mapper=reset_connectivity_management_password_error_mapper,
            request_options=request_options,
        )

    def start_connectivity_management_session(
        self,
        *,
        body: LogInRequest | LogInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LogInResult, StartConnectivityManagementSessionErrorBody]:
        """Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent
        API requests.

        Args:
            body: Request to initiate a session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/session/login"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LogInRequest | LogInRequestDict | None](body),
            auth_scheme=self._auth.thingspace_oauth,
            decoder=json_decoder[LogInResult],
            error_mapper=start_connectivity_management_session_error_mapper,
            request_options=request_options,
        )


class AsyncSessionManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def end_connectivity_management_session(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LogOutRequest, EndConnectivityManagementSessionErrorBody]:
        """Ends a Connectivity Management session.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/session/logout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[LogOutRequest],
            error_mapper=end_connectivity_management_session_error_mapper,
            request_options=request_options,
        )

    async def reset_connectivity_management_password(
        self,
        body: SessionResetPasswordRequest | SessionResetPasswordRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SessionResetPasswordResult, ResetConnectivityManagementPasswordErrorBody]:
        """The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your
        password every 90 days.

        Args:
            body: Request with current password that needs to be reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/session/password/actions/reset"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SessionResetPasswordRequest | SessionResetPasswordRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SessionResetPasswordResult],
            error_mapper=reset_connectivity_management_password_error_mapper,
            request_options=request_options,
        )

    async def start_connectivity_management_session(
        self,
        *,
        body: LogInRequest | LogInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LogInResult, StartConnectivityManagementSessionErrorBody]:
        """Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent
        API requests.

        Args:
            body: Request to initiate a session.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/session/login"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LogInRequest | LogInRequestDict | None](body),
            auth_scheme=self._auth.thingspace_oauth,
            decoder=json_decoder[LogInResult],
            error_mapper=start_connectivity_management_session_error_mapper,
            request_options=request_options,
        )
