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
from ..errors.deregister_callback2_error import DeregisterCallback2ErrorBody, deregister_callback2_error_mapper
from ..errors.list_registered_callbacks2_error import (
    ListRegisteredCallbacks2ErrorBody,
    list_registered_callbacks2_error_mapper,
)
from ..errors.register_callback2_error import RegisterCallback2ErrorBody, register_callback2_error_mapper
from ..models.callback_registration_result import CallbackRegistrationResult
from ..models.device_location_callback import DeviceLocationCallback
from ..models.device_location_success_result import DeviceLocationSuccessResult
from ..models.enums.callback_service_name import CallbackServiceNameOrStr
from ..models.transaction_id import TransactionId
from ..server.server import Server


class DeviceLocationCallbacks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceLocationCallbacksWithRawResponse(client, server, auth)

    def cancel_async_report(
        self, txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionId:
        """Cancel an asynchronous report request.

        Args:
            txid: The ``transactionId`` value.
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request canceled.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_async_report(txid, account_name, request_options=request_options).unwrap()

    def deregister_callback2(
        self,
        account_name: str,
        service: CallbackServiceNameOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceLocationSuccessResult:
        """Deregister a URL to stop receiving callback messages.

        Args:
            account_name: Account number.
            service: Callback service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deregistration successful.

        Raises:
            ApiError: Error response. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.deregister_callback2(
            account_name, service, request_options=request_options
        ).unwrap()

    def list_registered_callbacks2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLocationCallback]:
        """Returns a list of all registered callback URLs for the account.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of all registered callback URLs.

        Raises:
            ApiError: Error response. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.list_registered_callbacks2(
            account_name, request_options=request_options
        ).unwrap()

    def register_callback2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CallbackRegistrationResult:
        """Provide a URL to receive messages from a ThingSpace callback service.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Callback registration response.

        Raises:
            ApiError: Error response. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.register_callback2(account_name, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceLocationCallbacksWithRawResponse:
        return self._with_raw_response


class AsyncDeviceLocationCallbacks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceLocationCallbacksWithRawResponse(client, server, auth)

    async def cancel_async_report(
        self, txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionId:
        """Cancel an asynchronous report request.

        Args:
            txid: The ``transactionId`` value.
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request canceled.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_async_report(txid, account_name, request_options=request_options)
        ).unwrap()

    async def deregister_callback2(
        self,
        account_name: str,
        service: CallbackServiceNameOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceLocationSuccessResult:
        """Deregister a URL to stop receiving callback messages.

        Args:
            account_name: Account number.
            service: Callback service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deregistration successful.

        Raises:
            ApiError: Error response. ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.deregister_callback2(account_name, service, request_options=request_options)
        ).unwrap()

    async def list_registered_callbacks2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLocationCallback]:
        """Returns a list of all registered callback URLs for the account.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of all registered callback URLs.

        Raises:
            ApiError: Error response. ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.list_registered_callbacks2(account_name, request_options=request_options)
        ).unwrap()

    async def register_callback2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CallbackRegistrationResult:
        """Provide a URL to receive messages from a ThingSpace callback service.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Callback registration response.

        Raises:
            ApiError: Error response. ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.register_callback2(account_name, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceLocationCallbacksWithRawResponse:
        return self._with_raw_response


class DeviceLocationCallbacksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_async_report(
        self, txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionId, RawError]:
        """Cancel an asynchronous report request.

        Args:
            txid: The ``transactionId`` value.
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/devicelocations/{txid}"),
            path_params=[param[str]("txid", txid)],
            query_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deregister_callback2(
        self,
        account_name: str,
        service: CallbackServiceNameOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceLocationSuccessResult, DeregisterCallback2ErrorBody]:
        """Deregister a URL to stop receiving callback messages.

        Args:
            account_name: Account number.
            service: Callback service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/callbacks/{accountName}/name/{service}"),
            path_params=[param[str]("accountName", account_name), param[CallbackServiceNameOrStr]("service", service)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=deregister_callback2_error_mapper,
            request_options=request_options,
        )

    def list_registered_callbacks2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLocationCallback], ListRegisteredCallbacks2ErrorBody]:
        """Returns a list of all registered callback URLs for the account.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/callbacks/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLocationCallback]],
            error_mapper=list_registered_callbacks2_error_mapper,
            request_options=request_options,
        )

    def register_callback2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CallbackRegistrationResult, RegisterCallback2ErrorBody]:
        """Provide a URL to receive messages from a ThingSpace callback service.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/callbacks/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackRegistrationResult],
            error_mapper=register_callback2_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceLocationCallbacksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_async_report(
        self, txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionId, RawError]:
        """Cancel an asynchronous report request.

        Args:
            txid: The ``transactionId`` value.
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/devicelocations/{txid}"),
            path_params=[param[str]("txid", txid)],
            query_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deregister_callback2(
        self,
        account_name: str,
        service: CallbackServiceNameOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceLocationSuccessResult, DeregisterCallback2ErrorBody]:
        """Deregister a URL to stop receiving callback messages.

        Args:
            account_name: Account number.
            service: Callback service name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/callbacks/{accountName}/name/{service}"),
            path_params=[param[str]("accountName", account_name), param[CallbackServiceNameOrStr]("service", service)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=deregister_callback2_error_mapper,
            request_options=request_options,
        )

    async def list_registered_callbacks2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLocationCallback], ListRegisteredCallbacks2ErrorBody]:
        """Returns a list of all registered callback URLs for the account.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/callbacks/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLocationCallback]],
            error_mapper=list_registered_callbacks2_error_mapper,
            request_options=request_options,
        )

    async def register_callback2(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CallbackRegistrationResult, RegisterCallback2ErrorBody]:
        """Provide a URL to receive messages from a ThingSpace callback service.

        Args:
            account_name: Account number.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/callbacks/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackRegistrationResult],
            error_mapper=register_callback2_error_mapper,
            request_options=request_options,
        )
