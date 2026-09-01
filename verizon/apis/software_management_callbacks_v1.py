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
from ..errors.deregister_callback3_error import DeregisterCallback3ErrorBody, deregister_callback3_error_mapper
from ..errors.list_registered_callbacks3_error import (
    ListRegisteredCallbacks3ErrorBody,
    list_registered_callbacks3_error_mapper,
)
from ..errors.register_callback3_error import RegisterCallback3ErrorBody, register_callback3_error_mapper
from ..models.enums.callback_service import CallbackServiceOrStr
from ..models.fota_v1_callback_registration_request import (
    FotaV1CallbackRegistrationRequest,
    FotaV1CallbackRegistrationRequestDict,
)
from ..models.fota_v1_callback_registration_result import FotaV1CallbackRegistrationResult
from ..models.registered_callbacks import RegisteredCallbacks
from ..server.server import Server


class SoftwareManagementCallbacksV1:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementCallbacksV1WithRawResponse(client, server, auth)

    def deregister_callback3(
        self, account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified
        account.

        Args:
            account: Account identifier in "##########-#####".
            service: Callback type. Must be 'Fota' for Software Management Services API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Callback successfully deregistered.

        Raises:
            ApiError: Unexpected error. ``error`` is ``RawError``."""
        return self._with_raw_response.deregister_callback3(account, service, request_options=request_options).unwrap()

    def list_registered_callbacks3(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[RegisteredCallbacks]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of callbacks.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.list_registered_callbacks3(account, request_options=request_options).unwrap()

    def register_callback3(
        self,
        account: str,
        body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FotaV1CallbackRegistrationResult:
        """Registers a URL to receive RESTful messages from a callback service when new firmware versions are available
        and when upgrades start and finish.

        Args:
            account: Account identifier in "##########-#####".
            body: Callback details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of registering a callback.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.register_callback3(account, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementCallbacksV1WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementCallbacksV1:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementCallbacksV1WithRawResponse(client, server, auth)

    async def deregister_callback3(
        self, account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified
        account.

        Args:
            account: Account identifier in "##########-#####".
            service: Callback type. Must be 'Fota' for Software Management Services API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Callback successfully deregistered.

        Raises:
            ApiError: Unexpected error. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deregister_callback3(account, service, request_options=request_options)
        ).unwrap()

    async def list_registered_callbacks3(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[RegisteredCallbacks]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of callbacks.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.list_registered_callbacks3(account, request_options=request_options)
        ).unwrap()

    async def register_callback3(
        self,
        account: str,
        body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FotaV1CallbackRegistrationResult:
        """Registers a URL to receive RESTful messages from a callback service when new firmware versions are available
        and when upgrades start and finish.

        Args:
            account: Account identifier in "##########-#####".
            body: Callback details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of registering a callback.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.register_callback3(account, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementCallbacksV1WithRawResponse:
        return self._with_raw_response


class SoftwareManagementCallbacksV1WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def deregister_callback3(
        self, account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeregisterCallback3ErrorBody]:
        """Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified
        account.

        Args:
            account: Account identifier in "##########-#####".
            service: Callback type. Must be 'Fota' for Software Management Services API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v1("/callbacks/{account}/name/{service}"),
            path_params=[param[str]("account", account), param[CallbackServiceOrStr]("service", service)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=deregister_callback3_error_mapper,
            request_options=request_options,
        )

    def list_registered_callbacks3(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[RegisteredCallbacks], ListRegisteredCallbacks3ErrorBody]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[RegisteredCallbacks]],
            error_mapper=list_registered_callbacks3_error_mapper,
            request_options=request_options,
        )

    def register_callback3(
        self,
        account: str,
        body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FotaV1CallbackRegistrationResult, RegisterCallback3ErrorBody]:
        """Registers a URL to receive RESTful messages from a callback service when new firmware versions are available
        and when upgrades start and finish.

        Args:
            account: Account identifier in "##########-#####".
            body: Callback details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV1CallbackRegistrationResult],
            error_mapper=register_callback3_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementCallbacksV1WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def deregister_callback3(
        self, account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeregisterCallback3ErrorBody]:
        """Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified
        account.

        Args:
            account: Account identifier in "##########-#####".
            service: Callback type. Must be 'Fota' for Software Management Services API.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v1("/callbacks/{account}/name/{service}"),
            path_params=[param[str]("account", account), param[CallbackServiceOrStr]("service", service)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=deregister_callback3_error_mapper,
            request_options=request_options,
        )

    async def list_registered_callbacks3(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[RegisteredCallbacks], ListRegisteredCallbacks3ErrorBody]:
        """Returns the name and endpoint URL of the callback listening services registered for a given account.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[RegisteredCallbacks]],
            error_mapper=list_registered_callbacks3_error_mapper,
            request_options=request_options,
        )

    async def register_callback3(
        self,
        account: str,
        body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FotaV1CallbackRegistrationResult, RegisterCallback3ErrorBody]:
        """Registers a URL to receive RESTful messages from a callback service when new firmware versions are available
        and when upgrades start and finish.

        Args:
            account: Account identifier in "##########-#####".
            body: Callback details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/callbacks/{account}"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV1CallbackRegistrationResult],
            error_mapper=register_callback3_error_mapper,
            request_options=request_options,
        )
