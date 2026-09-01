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
from ..errors.sensor_insights_create_user_request_error import (
    SensorInsightsCreateUserRequestErrorBody,
    sensor_insights_create_user_request_error_mapper,
)
from ..errors.sensor_insights_delete_user_error import (
    SensorInsightsDeleteUserErrorBody,
    sensor_insights_delete_user_error_mapper,
)
from ..errors.sensor_insights_list_user_request_error import (
    SensorInsightsListUserRequestErrorBody,
    sensor_insights_list_user_request_error_mapper,
)
from ..errors.sensor_insights_update_user_request_error import (
    SensorInsightsUpdateUserRequestErrorBody,
    sensor_insights_update_user_request_error_mapper,
)
from ..models.dto_create_user_request import DtoCreateUserRequest, DtoCreateUserRequestDict
from ..models.dto_delete_user_request import DtoDeleteUserRequest, DtoDeleteUserRequestDict
from ..models.dto_list_user_request import DtoListUserRequest, DtoListUserRequestDict
from ..models.dto_update_user_request import DtoUpdateUserRequest, DtoUpdateUserRequestDict
from ..models.resource_user import ResourceUser
from ..server.server import Server


class SensorInsightsUsers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsUsersWithRawResponse(client, server, auth)

    def sensor_insights_create_user_request(
        self,
        body: DtoCreateUserRequest | DtoCreateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceUser:
        """Send a ``POST`` request.

        Args:
            body: Create a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_create_user_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_delete_user(
        self,
        deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            deleterequestpayload: Payload for the delete user request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError |
                ManagementError403 | ManagementError404 | RawError``."""
        return self._with_raw_response.sensor_insights_delete_user(
            deleterequestpayload, request_options=request_options
        ).unwrap()

    def sensor_insights_list_user_request(
        self, body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ResourceUser]:
        """Send a ``POST`` request.

        Args:
            body: A summary of user profile records on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_user_request(body, request_options=request_options).unwrap()

    def sensor_insights_update_user_request(
        self,
        body: DtoUpdateUserRequest | DtoUpdateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceUser:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_update_user_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsUsersWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsUsers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsUsersWithRawResponse(client, server, auth)

    async def sensor_insights_create_user_request(
        self,
        body: DtoCreateUserRequest | DtoCreateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceUser:
        """Send a ``POST`` request.

        Args:
            body: Create a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_create_user_request(body, request_options=request_options)
        ).unwrap()

    async def sensor_insights_delete_user(
        self,
        deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            deleterequestpayload: Payload for the delete user request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError |
                ManagementError403 | ManagementError404 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_delete_user(
                deleterequestpayload, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_list_user_request(
        self, body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ResourceUser]:
        """Send a ``POST`` request.

        Args:
            body: A summary of user profile records on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_user_request(body, request_options=request_options)
        ).unwrap()

    async def sensor_insights_update_user_request(
        self,
        body: DtoUpdateUserRequest | DtoUpdateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceUser:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_update_user_request(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsUsersWithRawResponse:
        return self._with_raw_response


class SensorInsightsUsersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_create_user_request(
        self,
        body: DtoCreateUserRequest | DtoCreateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceUser, SensorInsightsCreateUserRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Create a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoCreateUserRequest | DtoCreateUserRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceUser],
            error_mapper=sensor_insights_create_user_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_delete_user(
        self,
        deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsDeleteUserErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            deleterequestpayload: Payload for the delete user request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users"),
            query_params=[
                param[DtoDeleteUserRequest | DtoDeleteUserRequestDict]("deleterequestpayload", deleterequestpayload)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_delete_user_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_list_user_request(
        self, body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ResourceUser], SensorInsightsListUserRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: A summary of user profile records on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListUserRequest | DtoListUserRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceUser]],
            error_mapper=sensor_insights_list_user_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_update_user_request(
        self,
        body: DtoUpdateUserRequest | DtoUpdateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceUser, SensorInsightsUpdateUserRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoUpdateUserRequest | DtoUpdateUserRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceUser],
            error_mapper=sensor_insights_update_user_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsUsersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_create_user_request(
        self,
        body: DtoCreateUserRequest | DtoCreateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceUser, SensorInsightsCreateUserRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Create a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoCreateUserRequest | DtoCreateUserRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceUser],
            error_mapper=sensor_insights_create_user_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_delete_user(
        self,
        deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsDeleteUserErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            deleterequestpayload: Payload for the delete user request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users"),
            query_params=[
                param[DtoDeleteUserRequest | DtoDeleteUserRequestDict]("deleterequestpayload", deleterequestpayload)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_delete_user_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_list_user_request(
        self, body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ResourceUser], SensorInsightsListUserRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: A summary of user profile records on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListUserRequest | DtoListUserRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceUser]],
            error_mapper=sensor_insights_list_user_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_update_user_request(
        self,
        body: DtoUpdateUserRequest | DtoUpdateUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceUser, SensorInsightsUpdateUserRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a user profile
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoUpdateUserRequest | DtoUpdateUserRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceUser],
            error_mapper=sensor_insights_update_user_request_error_mapper,
            request_options=request_options,
        )
