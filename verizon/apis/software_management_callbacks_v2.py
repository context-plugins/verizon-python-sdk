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
from ..errors.deregister_callback4_error import DeregisterCallback4ErrorBody, deregister_callback4_error_mapper
from ..errors.list_registered_callbacks4_error import (
    ListRegisteredCallbacks4ErrorBody,
    list_registered_callbacks4_error_mapper,
)
from ..errors.register_callback4_error import RegisterCallback4ErrorBody, register_callback4_error_mapper
from ..errors.update_callback_error import UpdateCallbackErrorBody, update_callback_error_mapper
from ..models.callback_summary import CallbackSummary
from ..models.fota_v2_callback_registration_result import FotaV2CallbackRegistrationResult
from ..models.fota_v2_success_result import FotaV2SuccessResult
from ..server.server import Server


class SoftwareManagementCallbacksV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementCallbacksV2WithRawResponse(client, server, auth)

    def deregister_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2SuccessResult:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of deregistering a callback.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.deregister_callback4(account, request_options=request_options).unwrap()

    def list_registered_callbacks4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CallbackSummary:
        """This endpoint allows user to get the registered callback information.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.list_registered_callbacks4(account, request_options=request_options).unwrap()

    def register_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2CallbackRegistrationResult:
        """This endpoint allows user to create the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.register_callback4(account, request_options=request_options).unwrap()

    def update_callback(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2CallbackRegistrationResult:
        """This endpoint allows user to update the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.update_callback(account, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementCallbacksV2WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementCallbacksV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementCallbacksV2WithRawResponse(client, server, auth)

    async def deregister_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2SuccessResult:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of deregistering a callback.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (await self._with_raw_response.deregister_callback4(account, request_options=request_options)).unwrap()

    async def list_registered_callbacks4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CallbackSummary:
        """This endpoint allows user to get the registered callback information.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.list_registered_callbacks4(account, request_options=request_options)
        ).unwrap()

    async def register_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2CallbackRegistrationResult:
        """This endpoint allows user to create the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (await self._with_raw_response.register_callback4(account, request_options=request_options)).unwrap()

    async def update_callback(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2CallbackRegistrationResult:
        """This endpoint allows user to update the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (await self._with_raw_response.update_callback(account, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementCallbacksV2WithRawResponse:
        return self._with_raw_response


class SoftwareManagementCallbacksV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def deregister_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2SuccessResult, DeregisterCallback4ErrorBody]:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2SuccessResult],
            error_mapper=deregister_callback4_error_mapper,
            request_options=request_options,
        )

    def list_registered_callbacks4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CallbackSummary, ListRegisteredCallbacks4ErrorBody]:
        """This endpoint allows user to get the registered callback information.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackSummary],
            error_mapper=list_registered_callbacks4_error_mapper,
            request_options=request_options,
        )

    def register_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2CallbackRegistrationResult, RegisterCallback4ErrorBody]:
        """This endpoint allows user to create the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2CallbackRegistrationResult],
            error_mapper=register_callback4_error_mapper,
            request_options=request_options,
        )

    def update_callback(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2CallbackRegistrationResult, UpdateCallbackErrorBody]:
        """This endpoint allows user to update the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2CallbackRegistrationResult],
            error_mapper=update_callback_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementCallbacksV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def deregister_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2SuccessResult, DeregisterCallback4ErrorBody]:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2SuccessResult],
            error_mapper=deregister_callback4_error_mapper,
            request_options=request_options,
        )

    async def list_registered_callbacks4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CallbackSummary, ListRegisteredCallbacks4ErrorBody]:
        """This endpoint allows user to get the registered callback information.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CallbackSummary],
            error_mapper=list_registered_callbacks4_error_mapper,
            request_options=request_options,
        )

    async def register_callback4(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2CallbackRegistrationResult, RegisterCallback4ErrorBody]:
        """This endpoint allows user to create the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2CallbackRegistrationResult],
            error_mapper=register_callback4_error_mapper,
            request_options=request_options,
        )

    async def update_callback(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2CallbackRegistrationResult, UpdateCallbackErrorBody]:
        """This endpoint allows user to update the HTTPS callback address.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2CallbackRegistrationResult],
            error_mapper=update_callback_error_mapper,
            request_options=request_options,
        )
