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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.device_profile_request import DeviceProfileRequest, DeviceProfileRequestDict
from ..models.fall_back import FallBack, FallBackDict
from ..models.giodeactivate_device_profile_request import (
    GiodeactivateDeviceProfileRequest,
    GiodeactivateDeviceProfileRequestDict,
)
from ..models.gioprofile_request import GioprofileRequest, GioprofileRequestDict
from ..models.giorequest_response import GiorequestResponse
from ..server.server import Server


class ManagingESimProfiles:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManagingESimProfilesWithRawResponse(client, server, auth)

    def activate_a_device_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Activate a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.activate_a_device_profile(body, request_options=request_options).unwrap()

    def deactivate_a_device_profile(
        self,
        body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Deactivate the lead or local profile. **Note:** to reactivate the profile, use the **Activate** endpoint
        above.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deactivate_a_device_profile(body, request_options=request_options).unwrap()

    def delete_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Delete a device profile for Global IoT Orchestration. **Note:** the profile must be deactivated first!

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_a_device_profile(body, request_options=request_options).unwrap()

    def device_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Suspend all service to an eUICC device, including the lead and local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.device_suspend(body, request_options=request_options).unwrap()

    def download_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Download a Global IoT Orchestration device profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.download_a_device_profile(body, request_options=request_options).unwrap()

    def enable_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Enable a device lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.enable_a_device_profile(body, request_options=request_options).unwrap()

    def enable_a_device_profile_for_download(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Enable the Global IoT Orchestration device profile for download.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.enable_a_device_profile_for_download(
            body, request_options=request_options
        ).unwrap()

    def profile_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Suspend a device's Global profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.profile_suspend(body, request_options=request_options).unwrap()

    def resume_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Resume service to a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.resume_profile(body, request_options=request_options).unwrap()

    def set_fallback(
        self, body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Enable a fallback profile to be set.

        Args:
            body: Set the fallback attributes to allow a fallback profile to be activated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.set_fallback(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManagingESimProfilesWithRawResponse:
        return self._with_raw_response


class AsyncManagingESimProfiles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManagingESimProfilesWithRawResponse(client, server, auth)

    async def activate_a_device_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Activate a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.activate_a_device_profile(body, request_options=request_options)).unwrap()

    async def deactivate_a_device_profile(
        self,
        body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Deactivate the lead or local profile. **Note:** to reactivate the profile, use the **Activate** endpoint
        above.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deactivate_a_device_profile(body, request_options=request_options)
        ).unwrap()

    async def delete_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Delete a device profile for Global IoT Orchestration. **Note:** the profile must be deactivated first!

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_a_device_profile(body, request_options=request_options)).unwrap()

    async def device_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Suspend all service to an eUICC device, including the lead and local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.device_suspend(body, request_options=request_options)).unwrap()

    async def download_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Download a Global IoT Orchestration device profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.download_a_device_profile(body, request_options=request_options)).unwrap()

    async def enable_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Enable a device lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.enable_a_device_profile(body, request_options=request_options)).unwrap()

    async def enable_a_device_profile_for_download(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Enable the Global IoT Orchestration device profile for download.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.enable_a_device_profile_for_download(body, request_options=request_options)
        ).unwrap()

    async def profile_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Suspend a device's Global profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.profile_suspend(body, request_options=request_options)).unwrap()

    async def resume_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Resume service to a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.resume_profile(body, request_options=request_options)).unwrap()

    async def set_fallback(
        self, body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Enable a fallback profile to be set.

        Args:
            body: Set the fallback attributes to allow a fallback profile to be activated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.set_fallback(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManagingESimProfilesWithRawResponse:
        return self._with_raw_response


class ManagingESimProfilesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_a_device_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Activate a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deactivate_a_device_profile(
        self,
        body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Deactivate the lead or local profile. **Note:** to reactivate the profile, use the **Activate** endpoint
        above.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Delete a device profile for Global IoT Orchestration. **Note:** the profile must be deactivated first!

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def device_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Suspend all service to an eUICC device, including the lead and local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/device_suspend"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def download_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Download a Global IoT Orchestration device profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def enable_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Enable a device lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def enable_a_device_profile_for_download(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Enable the Global IoT Orchestration device profile for download.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download_enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def profile_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Suspend a device's Global profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/profile_suspend"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def resume_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Resume service to a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/profile_resume"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def set_fallback(
        self, body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Enable a fallback profile to be set.

        Args:
            body: Set the fallback attributes to allow a fallback profile to be activated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/devices/profile/actions/setfallbackattribute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FallBack | FallBackDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncManagingESimProfilesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_a_device_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Activate a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deactivate_a_device_profile(
        self,
        body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Deactivate the lead or local profile. **Note:** to reactivate the profile, use the **Activate** endpoint
        above.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Delete a device profile for Global IoT Orchestration. **Note:** the profile must be deactivated first!

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def device_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Suspend all service to an eUICC device, including the lead and local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/device_suspend"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def download_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Download a Global IoT Orchestration device profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def enable_a_device_profile(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Enable a device lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def enable_a_device_profile_for_download(
        self,
        body: DeviceProfileRequest | DeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Enable the Global IoT Orchestration device profile for download.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download_enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceProfileRequest | DeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def profile_suspend(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Suspend a device's Global profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/profile_suspend"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def resume_profile(
        self, body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Resume service to a device with either a lead or local profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/profile_resume"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GioprofileRequest | GioprofileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def set_fallback(
        self, body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Enable a fallback profile to be set.

        Args:
            body: Set the fallback attributes to allow a fallback profile to be activated.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/devices/profile/actions/setfallbackattribute"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FallBack | FallBackDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
