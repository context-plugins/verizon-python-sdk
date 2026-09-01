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
from ..errors.deregister_callback5_error import DeregisterCallback5ErrorBody, deregister_callback5_error_mapper
from ..errors.list_registered_callbacks5_error import (
    ListRegisteredCallbacks5ErrorBody,
    list_registered_callbacks5_error_mapper,
)
from ..errors.register_callback5_error import RegisterCallback5ErrorBody, register_callback5_error_mapper
from ..errors.update_callback2_error import UpdateCallback2ErrorBody, update_callback2_error_mapper
from ..models.fota_v3_callback_registration_request import (
    FotaV3CallbackRegistrationRequest,
    FotaV3CallbackRegistrationRequestDict,
)
from ..models.fota_v3_callback_registration_result import FotaV3CallbackRegistrationResult
from ..models.fota_v3_callback_summary import FotaV3CallbackSummary
from ..models.fota_v3_success_result import FotaV3SuccessResult
from ..server.server import Server


class SoftwareManagementCallbacksV3:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementCallbacksV3WithRawResponse(client, server, auth)

    def deregister_callback5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3SuccessResult:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete request result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.deregister_callback5(acc, request_options=request_options).unwrap()

    def list_registered_callbacks5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3CallbackSummary:
        """This endpoint allows user to get the registered callback information.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.list_registered_callbacks5(acc, request_options=request_options).unwrap()

    def register_callback5(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FotaV3CallbackRegistrationResult:
        """This endpoint allows the user to create the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.register_callback5(acc, body, request_options=request_options).unwrap()

    def update_callback2(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FotaV3CallbackRegistrationResult:
        """This endpoint allows the user to update the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.update_callback2(acc, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementCallbacksV3WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementCallbacksV3:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementCallbacksV3WithRawResponse(client, server, auth)

    async def deregister_callback5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3SuccessResult:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete request result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (await self._with_raw_response.deregister_callback5(acc, request_options=request_options)).unwrap()

    async def list_registered_callbacks5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3CallbackSummary:
        """This endpoint allows user to get the registered callback information.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (await self._with_raw_response.list_registered_callbacks5(acc, request_options=request_options)).unwrap()

    async def register_callback5(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FotaV3CallbackRegistrationResult:
        """This endpoint allows the user to create the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (await self._with_raw_response.register_callback5(acc, body, request_options=request_options)).unwrap()

    async def update_callback2(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FotaV3CallbackRegistrationResult:
        """This endpoint allows the user to update the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return callback registration.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (await self._with_raw_response.update_callback2(acc, body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementCallbacksV3WithRawResponse:
        return self._with_raw_response


class SoftwareManagementCallbacksV3WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def deregister_callback5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3SuccessResult, DeregisterCallback5ErrorBody]:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3SuccessResult],
            error_mapper=deregister_callback5_error_mapper,
            request_options=request_options,
        )

    def list_registered_callbacks5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3CallbackSummary, ListRegisteredCallbacks5ErrorBody]:
        """This endpoint allows user to get the registered callback information.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3CallbackSummary],
            error_mapper=list_registered_callbacks5_error_mapper,
            request_options=request_options,
        )

    def register_callback5(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FotaV3CallbackRegistrationResult, RegisterCallback5ErrorBody]:
        """This endpoint allows the user to create the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3CallbackRegistrationResult],
            error_mapper=register_callback5_error_mapper,
            request_options=request_options,
        )

    def update_callback2(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FotaV3CallbackRegistrationResult, UpdateCallback2ErrorBody]:
        """This endpoint allows the user to update the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3CallbackRegistrationResult],
            error_mapper=update_callback2_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementCallbacksV3WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def deregister_callback5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3SuccessResult, DeregisterCallback5ErrorBody]:
        """This endpoint allows user to delete a previously registered callback URL.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3SuccessResult],
            error_mapper=deregister_callback5_error_mapper,
            request_options=request_options,
        )

    async def list_registered_callbacks5(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3CallbackSummary, ListRegisteredCallbacks5ErrorBody]:
        """This endpoint allows user to get the registered callback information.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3CallbackSummary],
            error_mapper=list_registered_callbacks5_error_mapper,
            request_options=request_options,
        )

    async def register_callback5(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FotaV3CallbackRegistrationResult, RegisterCallback5ErrorBody]:
        """This endpoint allows the user to create the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3CallbackRegistrationResult],
            error_mapper=register_callback5_error_mapper,
            request_options=request_options,
        )

    async def update_callback2(
        self,
        acc: str,
        body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FotaV3CallbackRegistrationResult, UpdateCallback2ErrorBody]:
        """This endpoint allows the user to update the HTTPS callback address.

        Args:
            acc: Account identifier.
            body: Callback URL registration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/callbacks/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3CallbackRegistrationResult],
            error_mapper=update_callback2_error_mapper,
            request_options=request_options,
        )
