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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.deregister_callback6_error import DeregisterCallback6ErrorBody, deregister_callback6_error_mapper
from ..errors.list_registered_callbacks6_error import (
    ListRegisteredCallbacks6ErrorBody,
    list_registered_callbacks6_error_mapper,
)
from ..errors.register_callback6_error import RegisterCallback6ErrorBody, register_callback6_error_mapper
from ..models.callback_created import CallbackCreated
from ..models.callback_registered import CallbackRegistered
from ..models.hyper_precise_location_callback import HyperPreciseLocationCallback, HyperPreciseLocationCallbackDict
from ..server.server import Server


class HyperPreciseLocationCallbacks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = HyperPreciseLocationCallbacksWithRawResponse(client, server, auth)

    def deregister_callback6(
        self, account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Stops ThingSpace from sending callback messages for the specified account and listener name.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            service: The name of the callback service that will be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response (no content).

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.deregister_callback6(
            account_number, service, request_options=request_options
        ).unwrap()

    def list_registered_callbacks6(
        self, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CallbackCreated]:
        """Find registered callback listener for account by account number.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response will display the billing account number (``accountName``), the name of the callback
            service (``name``) and the address of the callback listening service (``url``).

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.list_registered_callbacks6(
            account_number, request_options=request_options
        ).unwrap()

    def register_callback6(
        self,
        account_number: str,
        body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CallbackRegistered:
        """Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace
        Platform callback service. The messages are REST messages. You are responsible for creating and running a
        listening process on your server at that URL to receive and parse the messages.

        Args:
            account_number: A unique identifier for an account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response will display the billing account number (``accountName``), the name of the callback
            service (``name``) and the address of the callback listening service (``url``).

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.register_callback6(
            account_number, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> HyperPreciseLocationCallbacksWithRawResponse:
        return self._with_raw_response


class AsyncHyperPreciseLocationCallbacks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncHyperPreciseLocationCallbacksWithRawResponse(client, server, auth)

    async def deregister_callback6(
        self, account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Stops ThingSpace from sending callback messages for the specified account and listener name.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            service: The name of the callback service that will be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response (no content).

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.deregister_callback6(account_number, service, request_options=request_options)
        ).unwrap()

    async def list_registered_callbacks6(
        self, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CallbackCreated]:
        """Find registered callback listener for account by account number.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response will display the billing account number (``accountName``), the name of the callback
            service (``name``) and the address of the callback listening service (``url``).

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.list_registered_callbacks6(account_number, request_options=request_options)
        ).unwrap()

    async def register_callback6(
        self,
        account_number: str,
        body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CallbackRegistered:
        """Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace
        Platform callback service. The messages are REST messages. You are responsible for creating and running a
        listening process on your server at that URL to receive and parse the messages.

        Args:
            account_number: A unique identifier for an account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response will display the billing account number (``accountName``), the name of the callback
            service (``name``) and the address of the callback listening service (``url``).

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.register_callback6(account_number, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncHyperPreciseLocationCallbacksWithRawResponse:
        return self._with_raw_response


class HyperPreciseLocationCallbacksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def deregister_callback6(
        self, account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeregisterCallback6ErrorBody]:
        """Stops ThingSpace from sending callback messages for the specified account and listener name.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            service: The name of the callback service that will be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_location("/callbacks"),
            query_params=[param[str]("accountNumber", account_number), param[str]("service", service)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=deregister_callback6_error_mapper,
            request_options=request_options,
        )

    def list_registered_callbacks6(
        self, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CallbackCreated], ListRegisteredCallbacks6ErrorBody]:
        """Find registered callback listener for account by account number.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_location("/callbacks"),
            query_params=[param[str]("accountNumber", account_number)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[CallbackCreated]],
            error_mapper=list_registered_callbacks6_error_mapper,
            request_options=request_options,
        )

    def register_callback6(
        self,
        account_number: str,
        body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CallbackRegistered, RegisterCallback6ErrorBody]:
        """Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace
        Platform callback service. The messages are REST messages. You are responsible for creating and running a
        listening process on your server at that URL to receive and parse the messages.

        Args:
            account_number: A unique identifier for an account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/callbacks"),
            query_params=[param[str]("accountNumber", account_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackRegistered],
            error_mapper=register_callback6_error_mapper,
            request_options=request_options,
        )


class AsyncHyperPreciseLocationCallbacksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def deregister_callback6(
        self, account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeregisterCallback6ErrorBody]:
        """Stops ThingSpace from sending callback messages for the specified account and listener name.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            service: The name of the callback service that will be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_location("/callbacks"),
            query_params=[param[str]("accountNumber", account_number), param[str]("service", service)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=deregister_callback6_error_mapper,
            request_options=request_options,
        )

    async def list_registered_callbacks6(
        self, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CallbackCreated], ListRegisteredCallbacks6ErrorBody]:
        """Find registered callback listener for account by account number.

        Args:
            account_number: The numeric ID of the account and must include leading zeroes. This value is indentical to
                ``accountName``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_location("/callbacks"),
            query_params=[param[str]("accountNumber", account_number)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[CallbackCreated]],
            error_mapper=list_registered_callbacks6_error_mapper,
            request_options=request_options,
        )

    async def register_callback6(
        self,
        account_number: str,
        body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CallbackRegistered, RegisterCallback6ErrorBody]:
        """Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace
        Platform callback service. The messages are REST messages. You are responsible for creating and running a
        listening process on your server at that URL to receive and parse the messages.

        Args:
            account_number: A unique identifier for an account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/callbacks"),
            query_params=[param[str]("accountNumber", account_number)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackRegistered],
            error_mapper=register_callback6_error_mapper,
            request_options=request_options,
        )
