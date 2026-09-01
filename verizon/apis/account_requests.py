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
from ..errors.get_current_asynchronous_request_status_error import (
    GetCurrentAsynchronousRequestStatusErrorBody,
    get_current_asynchronous_request_status_error_mapper,
)
from ..models.asynchronous_request_result import AsynchronousRequestResult
from ..server.server import Server


class AccountRequests:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountRequestsWithRawResponse(client, server, auth)

    def get_current_asynchronous_request_status(
        self, aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsynchronousRequestResult:
        """Returns the current status of an asynchronous request that was made for a single device.

        Args:
            aname: Account name.
            request_id: UUID from synchronous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The asynchronous request status.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.get_current_asynchronous_request_status(
            aname, request_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountRequestsWithRawResponse:
        return self._with_raw_response


class AsyncAccountRequests:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountRequestsWithRawResponse(client, server, auth)

    async def get_current_asynchronous_request_status(
        self, aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsynchronousRequestResult:
        """Returns the current status of an asynchronous request that was made for a single device.

        Args:
            aname: Account name.
            request_id: UUID from synchronous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The asynchronous request status.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.get_current_asynchronous_request_status(
                aname, request_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountRequestsWithRawResponse:
        return self._with_raw_response


class AccountRequestsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_current_asynchronous_request_status(
        self, aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsynchronousRequestResult, GetCurrentAsynchronousRequestStatusErrorBody]:
        """Returns the current status of an asynchronous request that was made for a single device.

        Args:
            aname: Account name.
            request_id: UUID from synchronous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/accounts/{aname}/requests/{requestId}/status"),
            path_params=[param[str]("aname", aname), param[str]("requestId", request_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AsynchronousRequestResult],
            error_mapper=get_current_asynchronous_request_status_error_mapper,
            request_options=request_options,
        )


class AsyncAccountRequestsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_current_asynchronous_request_status(
        self, aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsynchronousRequestResult, GetCurrentAsynchronousRequestStatusErrorBody]:
        """Returns the current status of an asynchronous request that was made for a single device.

        Args:
            aname: Account name.
            request_id: UUID from synchronous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/accounts/{aname}/requests/{requestId}/status"),
            path_params=[param[str]("aname", aname), param[str]("requestId", request_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AsynchronousRequestResult],
            error_mapper=get_current_asynchronous_request_status_error_mapper,
            request_options=request_options,
        )
