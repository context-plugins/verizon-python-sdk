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
from ..errors.deregister_callback_error import DeregisterCallbackErrorBody, deregister_callback_error_mapper
from ..errors.list_registered_callbacks_error import (
    ListRegisteredCallbacksErrorBody,
    list_registered_callbacks_error_mapper,
)
from ..errors.register_callback_error import RegisterCallbackErrorBody, register_callback_error_mapper
from ..models.callback_action_result import CallbackActionResult
from ..models.connectivity_management_callback import ConnectivityManagementCallback
from ..models.register_callback_request import RegisterCallbackRequest, RegisterCallbackRequestDict
from ..server.server import Server


class ConnectivityCallbacks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConnectivityCallbacksWithRawResponse(client, server, auth)

    def deregister_callback(
        self, aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CallbackActionResult:
        """Stops ThingSpace from sending callback messages for the specified account and service.

        Args:
            aname: Account name.
            sname: Service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response for a request to deregister a callback.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.deregister_callback(aname, sname, request_options=request_options).unwrap()

    def list_registered_callbacks(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ConnectivityManagementCallback]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of callback listeners.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_registered_callbacks(aname, request_options=request_options).unwrap()

    def register_callback(
        self,
        aname: str,
        body: RegisterCallbackRequest | RegisterCallbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CallbackActionResult:
        """You are responsible for creating and running a listening process on your server at that URL.

        Args:
            aname: Account name.
            body: Request to register a callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response for registering a callback.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.register_callback(aname, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ConnectivityCallbacksWithRawResponse:
        return self._with_raw_response


class AsyncConnectivityCallbacks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConnectivityCallbacksWithRawResponse(client, server, auth)

    async def deregister_callback(
        self, aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CallbackActionResult:
        """Stops ThingSpace from sending callback messages for the specified account and service.

        Args:
            aname: Account name.
            sname: Service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Response for a request to deregister a callback.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.deregister_callback(aname, sname, request_options=request_options)
        ).unwrap()

    async def list_registered_callbacks(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ConnectivityManagementCallback]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of callback listeners.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_registered_callbacks(aname, request_options=request_options)
        ).unwrap()

    async def register_callback(
        self,
        aname: str,
        body: RegisterCallbackRequest | RegisterCallbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CallbackActionResult:
        """You are responsible for creating and running a listening process on your server at that URL.

        Args:
            aname: Account name.
            body: Request to register a callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response for registering a callback.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.register_callback(aname, body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncConnectivityCallbacksWithRawResponse:
        return self._with_raw_response


class ConnectivityCallbacksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def deregister_callback(
        self, aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CallbackActionResult, DeregisterCallbackErrorBody]:
        """Stops ThingSpace from sending callback messages for the specified account and service.

        Args:
            aname: Account name.
            sname: Service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/callbacks/{aname}/name/{sname}"),
            path_params=[param[str]("aname", aname), param[str]("sname", sname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackActionResult],
            error_mapper=deregister_callback_error_mapper,
            request_options=request_options,
        )

    def list_registered_callbacks(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ConnectivityManagementCallback], ListRegisteredCallbacksErrorBody]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/callbacks/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ConnectivityManagementCallback]],
            error_mapper=list_registered_callbacks_error_mapper,
            request_options=request_options,
        )

    def register_callback(
        self,
        aname: str,
        body: RegisterCallbackRequest | RegisterCallbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CallbackActionResult, RegisterCallbackErrorBody]:
        """You are responsible for creating and running a listening process on your server at that URL.

        Args:
            aname: Account name.
            body: Request to register a callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/callbacks/{aname}"),
            path_params=[param[str]("aname", aname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterCallbackRequest | RegisterCallbackRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackActionResult],
            error_mapper=register_callback_error_mapper,
            request_options=request_options,
        )


class AsyncConnectivityCallbacksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def deregister_callback(
        self, aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CallbackActionResult, DeregisterCallbackErrorBody]:
        """Stops ThingSpace from sending callback messages for the specified account and service.

        Args:
            aname: Account name.
            sname: Service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/callbacks/{aname}/name/{sname}"),
            path_params=[param[str]("aname", aname), param[str]("sname", sname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackActionResult],
            error_mapper=deregister_callback_error_mapper,
            request_options=request_options,
        )

    async def list_registered_callbacks(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ConnectivityManagementCallback], ListRegisteredCallbacksErrorBody]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/callbacks/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ConnectivityManagementCallback]],
            error_mapper=list_registered_callbacks_error_mapper,
            request_options=request_options,
        )

    async def register_callback(
        self,
        aname: str,
        body: RegisterCallbackRequest | RegisterCallbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CallbackActionResult, RegisterCallbackErrorBody]:
        """You are responsible for creating and running a listening process on your server at that URL.

        Args:
            aname: Account name.
            body: Request to register a callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/callbacks/{aname}"),
            path_params=[param[str]("aname", aname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterCallbackRequest | RegisterCallbackRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackActionResult],
            error_mapper=register_callback_error_mapper,
            request_options=request_options,
        )
