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
from ..errors.activate_device_through_profile_error import (
    ActivateDeviceThroughProfileErrorBody,
    activate_device_through_profile_error_mapper,
)
from ..errors.profile_to_activate_device_error import (
    ProfileToActivateDeviceErrorBody,
    profile_to_activate_device_error_mapper,
)
from ..errors.profile_to_deactivate_device_error import (
    ProfileToDeactivateDeviceErrorBody,
    profile_to_deactivate_device_error_mapper,
)
from ..errors.profile_to_set_fallback_attribute_error import (
    ProfileToSetFallbackAttributeErrorBody,
    profile_to_set_fallback_attribute_error_mapper,
)
from ..models.activate_device_profile_request import ActivateDeviceProfileRequest, ActivateDeviceProfileRequestDict
from ..models.deactivate_device_profile_request import (
    DeactivateDeviceProfileRequest,
    DeactivateDeviceProfileRequestDict,
)
from ..models.profile_request import ProfileRequest, ProfileRequestDict
from ..models.request_response import RequestResponse
from ..models.set_fallback_attribute_request import SetFallbackAttributeRequest, SetFallbackAttributeRequestDict
from ..server.server import Server


class DeviceProfileManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceProfileManagementWithRawResponse(client, server, auth)

    def activate_device_through_profile(
        self,
        body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Uses the profile to bring the device under management.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.activate_device_through_profile(body, request_options=request_options).unwrap()

    def profile_to_activate_device(
        self, body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RequestResponse:
        """Uses the profile to activate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.profile_to_activate_device(body, request_options=request_options).unwrap()

    def profile_to_deactivate_device(
        self,
        body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Uses the profile to deactivate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.profile_to_deactivate_device(body, request_options=request_options).unwrap()

    def profile_to_set_fallback_attribute(
        self,
        body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Allows the profile to set the fallback attribute to the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.profile_to_set_fallback_attribute(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceProfileManagementWithRawResponse:
        return self._with_raw_response


class AsyncDeviceProfileManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceProfileManagementWithRawResponse(client, server, auth)

    async def activate_device_through_profile(
        self,
        body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Uses the profile to bring the device under management.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return (
            await self._with_raw_response.activate_device_through_profile(body, request_options=request_options)
        ).unwrap()

    async def profile_to_activate_device(
        self, body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RequestResponse:
        """Uses the profile to activate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return (
            await self._with_raw_response.profile_to_activate_device(body, request_options=request_options)
        ).unwrap()

    async def profile_to_deactivate_device(
        self,
        body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Uses the profile to deactivate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return (
            await self._with_raw_response.profile_to_deactivate_device(body, request_options=request_options)
        ).unwrap()

    async def profile_to_set_fallback_attribute(
        self,
        body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Allows the profile to set the fallback attribute to the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request ``error`` is ``RestErrorResponse | RawError``."""
        return (
            await self._with_raw_response.profile_to_set_fallback_attribute(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceProfileManagementWithRawResponse:
        return self._with_raw_response


class DeviceProfileManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_device_through_profile(
        self,
        body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, ActivateDeviceThroughProfileErrorBody]:
        """Uses the profile to bring the device under management.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate_enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=activate_device_through_profile_error_mapper,
            request_options=request_options,
        )

    def profile_to_activate_device(
        self, body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RequestResponse, ProfileToActivateDeviceErrorBody]:
        """Uses the profile to activate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileRequest | ProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=profile_to_activate_device_error_mapper,
            request_options=request_options,
        )

    def profile_to_deactivate_device(
        self,
        body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, ProfileToDeactivateDeviceErrorBody]:
        """Uses the profile to deactivate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=profile_to_deactivate_device_error_mapper,
            request_options=request_options,
        )

    def profile_to_set_fallback_attribute(
        self,
        body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, ProfileToSetFallbackAttributeErrorBody]:
        """Allows the profile to set the fallback attribute to the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/setfallbackattribute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetFallbackAttributeRequest | SetFallbackAttributeRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=profile_to_set_fallback_attribute_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceProfileManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_device_through_profile(
        self,
        body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, ActivateDeviceThroughProfileErrorBody]:
        """Uses the profile to bring the device under management.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate_enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=activate_device_through_profile_error_mapper,
            request_options=request_options,
        )

    async def profile_to_activate_device(
        self, body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RequestResponse, ProfileToActivateDeviceErrorBody]:
        """Uses the profile to activate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileRequest | ProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=profile_to_activate_device_error_mapper,
            request_options=request_options,
        )

    async def profile_to_deactivate_device(
        self,
        body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, ProfileToDeactivateDeviceErrorBody]:
        """Uses the profile to deactivate the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=profile_to_deactivate_device_error_mapper,
            request_options=request_options,
        )

    async def profile_to_set_fallback_attribute(
        self,
        body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, ProfileToSetFallbackAttributeErrorBody]:
        """Allows the profile to set the fallback attribute to the device.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/setfallbackattribute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetFallbackAttributeRequest | SetFallbackAttributeRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=profile_to_set_fallback_attribute_error_mapper,
            request_options=request_options,
        )
