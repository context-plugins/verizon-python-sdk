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
    json_decoder,
    param,
)
from ..errors.get_diagnostics_subscription_callback_info_error import (
    GetDiagnosticsSubscriptionCallbackInfoErrorBody,
    get_diagnostics_subscription_callback_info_error_mapper,
)
from ..errors.register_diagnostics_callback_url_error import (
    RegisterDiagnosticsCallbackUrlErrorBody,
    register_diagnostics_callback_url_error_mapper,
)
from ..errors.unregister_diagnostics_callback_error import (
    UnregisterDiagnosticsCallbackErrorBody,
    unregister_diagnostics_callback_error_mapper,
)
from ..models.device_diagnostics_callback import DeviceDiagnosticsCallback
from ..server.server import Server


class DiagnosticsCallbacks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DiagnosticsCallbacksWithRawResponse(client, server, auth)

    def get_diagnostics_subscription_callback_info(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceDiagnosticsCallback]:
        """This endpoint allows user to get the registered callback information of an existing diagnostics subscription.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceDiagnosticsResult | RawError``."""
        return self._with_raw_response.get_diagnostics_subscription_callback_info(
            account_name, request_options=request_options
        ).unwrap()

    def register_diagnostics_callback_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceDiagnosticsCallback:
        """This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceDiagnosticsResult | RawError``."""
        return self._with_raw_response.register_diagnostics_callback_url(request_options=request_options).unwrap()

    def unregister_diagnostics_callback(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceDiagnosticsCallback:
        """This endpoint allows user to delete a registered callback URL and credential.

        Args:
            account_name: Account identifier.
            service_name: Service name for callback notification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device diagnostics callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceDiagnosticsResult | RawError``."""
        return self._with_raw_response.unregister_diagnostics_callback(
            account_name, service_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DiagnosticsCallbacksWithRawResponse:
        return self._with_raw_response


class AsyncDiagnosticsCallbacks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDiagnosticsCallbacksWithRawResponse(client, server, auth)

    async def get_diagnostics_subscription_callback_info(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceDiagnosticsCallback]:
        """This endpoint allows user to get the registered callback information of an existing diagnostics subscription.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceDiagnosticsResult | RawError``."""
        return (
            await self._with_raw_response.get_diagnostics_subscription_callback_info(
                account_name, request_options=request_options
            )
        ).unwrap()

    async def register_diagnostics_callback_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceDiagnosticsCallback:
        """This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceDiagnosticsResult | RawError``."""
        return (
            await self._with_raw_response.register_diagnostics_callback_url(request_options=request_options)
        ).unwrap()

    async def unregister_diagnostics_callback(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceDiagnosticsCallback:
        """This endpoint allows user to delete a registered callback URL and credential.

        Args:
            account_name: Account identifier.
            service_name: Service name for callback notification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device diagnostics callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceDiagnosticsResult | RawError``."""
        return (
            await self._with_raw_response.unregister_diagnostics_callback(
                account_name, service_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiagnosticsCallbacksWithRawResponse:
        return self._with_raw_response


class DiagnosticsCallbacksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_diagnostics_subscription_callback_info(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceDiagnosticsCallback], GetDiagnosticsSubscriptionCallbackInfoErrorBody]:
        """This endpoint allows user to get the registered callback information of an existing diagnostics subscription.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_diagnostics("/callbacks"),
            query_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceDiagnosticsCallback]],
            error_mapper=get_diagnostics_subscription_callback_info_error_mapper,
            request_options=request_options,
        )

    def register_diagnostics_callback_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceDiagnosticsCallback, RegisterDiagnosticsCallbackUrlErrorBody]:
        """This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/callbacks"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceDiagnosticsCallback],
            error_mapper=register_diagnostics_callback_url_error_mapper,
            request_options=request_options,
        )

    def unregister_diagnostics_callback(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceDiagnosticsCallback, UnregisterDiagnosticsCallbackErrorBody]:
        """This endpoint allows user to delete a registered callback URL and credential.

        Args:
            account_name: Account identifier.
            service_name: Service name for callback notification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_diagnostics("/callbacks"),
            query_params=[param[str]("accountName", account_name), param[str]("serviceName", service_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceDiagnosticsCallback],
            error_mapper=unregister_diagnostics_callback_error_mapper,
            request_options=request_options,
        )


class AsyncDiagnosticsCallbacksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_diagnostics_subscription_callback_info(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceDiagnosticsCallback], GetDiagnosticsSubscriptionCallbackInfoErrorBody]:
        """This endpoint allows user to get the registered callback information of an existing diagnostics subscription.

        Args:
            account_name: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_diagnostics("/callbacks"),
            query_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceDiagnosticsCallback]],
            error_mapper=get_diagnostics_subscription_callback_info_error_mapper,
            request_options=request_options,
        )

    async def register_diagnostics_callback_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceDiagnosticsCallback, RegisterDiagnosticsCallbackUrlErrorBody]:
        """This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/callbacks"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceDiagnosticsCallback],
            error_mapper=register_diagnostics_callback_url_error_mapper,
            request_options=request_options,
        )

    async def unregister_diagnostics_callback(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceDiagnosticsCallback, UnregisterDiagnosticsCallbackErrorBody]:
        """This endpoint allows user to delete a registered callback URL and credential.

        Args:
            account_name: Account identifier.
            service_name: Service name for callback notification.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_diagnostics("/callbacks"),
            query_params=[param[str]("accountName", account_name), param[str]("serviceName", service_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceDiagnosticsCallback],
            error_mapper=unregister_diagnostics_callback_error_mapper,
            request_options=request_options,
        )
