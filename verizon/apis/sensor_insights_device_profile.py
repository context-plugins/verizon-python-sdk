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
from ..errors.create_aprofile_error import CreateAprofileErrorBody, create_aprofile_error_mapper
from ..errors.delete_aprofile_error import DeleteAprofileErrorBody, delete_aprofile_error_mapper
from ..errors.query_aprofile_error import QueryAprofileErrorBody, query_aprofile_error_mapper
from ..errors.update_aprofile_error import UpdateAprofileErrorBody, update_aprofile_error_mapper
from ..models.dto_configuration_profile import DtoConfigurationProfile, DtoConfigurationProfileDict
from ..models.dto_configuration_profile_delete import DtoConfigurationProfileDelete, DtoConfigurationProfileDeleteDict
from ..models.dto_configuration_profile_path import DtoConfigurationProfilePath, DtoConfigurationProfilePathDict
from ..models.dto_profile_response import DtoProfileResponse
from ..models.resource_resource_query import ResourceResourceQuery, ResourceResourceQueryDict
from ..server.server import Server


class SensorInsightsDeviceProfile:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsDeviceProfileWithRawResponse(client, server, auth)

    def create_a_profile(
        self,
        body: DtoConfigurationProfile | DtoConfigurationProfileDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Create a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return self._with_raw_response.create_a_profile(body, request_options=request_options).unwrap()

    def delete_a_profile(
        self,
        deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Delete a device profile

        Args:
            deleterequest: payload for the delete request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return self._with_raw_response.delete_a_profile(deleterequest, request_options=request_options).unwrap()

    def query_a_profile(
        self,
        body: ResourceResourceQuery | ResourceResourceQueryDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Query a device profile for an individual device

        Args:
            body: body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return self._with_raw_response.query_a_profile(body, request_options=request_options).unwrap()

    def update_a_profile(
        self,
        body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Partially update a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return self._with_raw_response.update_a_profile(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsDeviceProfileWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsDeviceProfile:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsDeviceProfileWithRawResponse(client, server, auth)

    async def create_a_profile(
        self,
        body: DtoConfigurationProfile | DtoConfigurationProfileDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Create a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return (await self._with_raw_response.create_a_profile(body, request_options=request_options)).unwrap()

    async def delete_a_profile(
        self,
        deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Delete a device profile

        Args:
            deleterequest: payload for the delete request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return (await self._with_raw_response.delete_a_profile(deleterequest, request_options=request_options)).unwrap()

    async def query_a_profile(
        self,
        body: ResourceResourceQuery | ResourceResourceQueryDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Query a device profile for an individual device

        Args:
            body: body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return (await self._with_raw_response.query_a_profile(body, request_options=request_options)).unwrap()

    async def update_a_profile(
        self,
        body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoProfileResponse]:
        """Partially update a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return (await self._with_raw_response.update_a_profile(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsDeviceProfileWithRawResponse:
        return self._with_raw_response


class SensorInsightsDeviceProfileWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_a_profile(
        self,
        body: DtoConfigurationProfile | DtoConfigurationProfileDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], CreateAprofileErrorBody]:
        """Create a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoConfigurationProfile | DtoConfigurationProfileDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=create_aprofile_error_mapper,
            request_options=request_options,
        )

    def delete_a_profile(
        self,
        deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], DeleteAprofileErrorBody]:
        """Delete a device profile

        Args:
            deleterequest: payload for the delete request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles"),
            headers=[
                param[DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict](
                    "deleterequest", deleterequest
                ),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=delete_aprofile_error_mapper,
            request_options=request_options,
        )

    def query_a_profile(
        self,
        body: ResourceResourceQuery | ResourceResourceQueryDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], QueryAprofileErrorBody]:
        """Query a device profile for an individual device

        Args:
            body: body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ResourceResourceQuery | ResourceResourceQueryDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=query_aprofile_error_mapper,
            request_options=request_options,
        )

    def update_a_profile(
        self,
        body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], UpdateAprofileErrorBody]:
        """Partially update a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoConfigurationProfilePath | DtoConfigurationProfilePathDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=update_aprofile_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsDeviceProfileWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_a_profile(
        self,
        body: DtoConfigurationProfile | DtoConfigurationProfileDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], CreateAprofileErrorBody]:
        """Create a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoConfigurationProfile | DtoConfigurationProfileDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=create_aprofile_error_mapper,
            request_options=request_options,
        )

    async def delete_a_profile(
        self,
        deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], DeleteAprofileErrorBody]:
        """Delete a device profile

        Args:
            deleterequest: payload for the delete request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles"),
            headers=[
                param[DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict](
                    "deleterequest", deleterequest
                ),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=delete_aprofile_error_mapper,
            request_options=request_options,
        )

    async def query_a_profile(
        self,
        body: ResourceResourceQuery | ResourceResourceQueryDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], QueryAprofileErrorBody]:
        """Query a device profile for an individual device

        Args:
            body: body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ResourceResourceQuery | ResourceResourceQueryDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=query_aprofile_error_mapper,
            request_options=request_options,
        )

    async def update_a_profile(
        self,
        body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoProfileResponse], UpdateAprofileErrorBody]:
        """Partially update a device profile

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/deviceConfigurationProfiles"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoConfigurationProfilePath | DtoConfigurationProfilePathDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoProfileResponse]],
            error_mapper=update_aprofile_error_mapper,
            request_options=request_options,
        )
