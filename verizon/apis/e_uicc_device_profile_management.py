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
from ..errors.delete_local_profile_error import DeleteLocalProfileErrorBody, delete_local_profile_error_mapper
from ..errors.disable_local_profile_error import DisableLocalProfileErrorBody, disable_local_profile_error_mapper
from ..errors.download_local_profile_to_disable_error import (
    DownloadLocalProfileToDisableErrorBody,
    download_local_profile_to_disable_error_mapper,
)
from ..errors.download_local_profile_to_enable_error import (
    DownloadLocalProfileToEnableErrorBody,
    download_local_profile_to_enable_error_mapper,
)
from ..errors.enable_local_profile_error import EnableLocalProfileErrorBody, enable_local_profile_error_mapper
from ..models.device_management_result import DeviceManagementResult
from ..models.profile_change_state_request import ProfileChangeStateRequest, ProfileChangeStateRequestDict
from ..models.request_response import RequestResponse
from ..server.server import Server


class EUiccDeviceProfileManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EUiccDeviceProfileManagementWithRawResponse(client, server, auth)

    def delete_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Delete a local profile from eUICC devices. If the local profile is enabled, it will first be disabled and the
        boot or default profile will be enabled.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.delete_local_profile(body, request_options=request_options).unwrap()

    def disable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Disable a local profile on eUICC devices. The default or boot profile will become the enabled profile.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.disable_local_profile(body, request_options=request_options).unwrap()

    def download_local_profile_to_disable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Downloads an eUICC local profile to devices and leaves the profile disabled.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.download_local_profile_to_disable(body, request_options=request_options).unwrap()

    def download_local_profile_to_enable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Downloads an eUICC local profile to devices and enables the profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.download_local_profile_to_enable(body, request_options=request_options).unwrap()

    def enable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Enable a local profile that has been downloaded to eUICC devices.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.enable_local_profile(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> EUiccDeviceProfileManagementWithRawResponse:
        return self._with_raw_response


class AsyncEUiccDeviceProfileManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEUiccDeviceProfileManagementWithRawResponse(client, server, auth)

    async def delete_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Delete a local profile from eUICC devices. If the local profile is enabled, it will first be disabled and the
        boot or default profile will be enabled.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return (await self._with_raw_response.delete_local_profile(body, request_options=request_options)).unwrap()

    async def disable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Disable a local profile on eUICC devices. The default or boot profile will become the enabled profile.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return (await self._with_raw_response.disable_local_profile(body, request_options=request_options)).unwrap()

    async def download_local_profile_to_disable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Downloads an eUICC local profile to devices and leaves the profile disabled.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.download_local_profile_to_disable(body, request_options=request_options)
        ).unwrap()

    async def download_local_profile_to_enable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Downloads an eUICC local profile to devices and enables the profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.download_local_profile_to_enable(body, request_options=request_options)
        ).unwrap()

    async def enable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Enable a local profile that has been downloaded to eUICC devices.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return (await self._with_raw_response.enable_local_profile(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncEUiccDeviceProfileManagementWithRawResponse:
        return self._with_raw_response


class EUiccDeviceProfileManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DeleteLocalProfileErrorBody]:
        """Delete a local profile from eUICC devices. If the local profile is enabled, it will first be disabled and the
        boot or default profile will be enabled.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=delete_local_profile_error_mapper,
            request_options=request_options,
        )

    def disable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DisableLocalProfileErrorBody]:
        """Disable a local profile on eUICC devices. The default or boot profile will become the enabled profile.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/disable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=disable_local_profile_error_mapper,
            request_options=request_options,
        )

    def download_local_profile_to_disable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DownloadLocalProfileToDisableErrorBody]:
        """Downloads an eUICC local profile to devices and leaves the profile disabled.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download_disable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=download_local_profile_to_disable_error_mapper,
            request_options=request_options,
        )

    def download_local_profile_to_enable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DownloadLocalProfileToEnableErrorBody]:
        """Downloads an eUICC local profile to devices and enables the profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download_enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=download_local_profile_to_enable_error_mapper,
            request_options=request_options,
        )

    def enable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, EnableLocalProfileErrorBody]:
        """Enable a local profile that has been downloaded to eUICC devices.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=enable_local_profile_error_mapper,
            request_options=request_options,
        )


class AsyncEUiccDeviceProfileManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DeleteLocalProfileErrorBody]:
        """Delete a local profile from eUICC devices. If the local profile is enabled, it will first be disabled and the
        boot or default profile will be enabled.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=delete_local_profile_error_mapper,
            request_options=request_options,
        )

    async def disable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DisableLocalProfileErrorBody]:
        """Disable a local profile on eUICC devices. The default or boot profile will become the enabled profile.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/disable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=disable_local_profile_error_mapper,
            request_options=request_options,
        )

    async def download_local_profile_to_disable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DownloadLocalProfileToDisableErrorBody]:
        """Downloads an eUICC local profile to devices and leaves the profile disabled.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download_disable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=download_local_profile_to_disable_error_mapper,
            request_options=request_options,
        )

    async def download_local_profile_to_enable(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DownloadLocalProfileToEnableErrorBody]:
        """Downloads an eUICC local profile to devices and enables the profile.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/download_enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=download_local_profile_to_enable_error_mapper,
            request_options=request_options,
        )

    async def enable_local_profile(
        self,
        body: ProfileChangeStateRequest | ProfileChangeStateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, EnableLocalProfileErrorBody]:
        """Enable a local profile that has been downloaded to eUICC devices.

        Args:
            body: Update state
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/enable"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileChangeStateRequest | ProfileChangeStateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=enable_local_profile_error_mapper,
            request_options=request_options,
        )
