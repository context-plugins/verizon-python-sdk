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
from ..errors.sensor_insights_add_users_to_notification_group_request_error import (
    SensorInsightsAddUsersToNotificationGroupRequestErrorBody,
    sensor_insights_add_users_to_notification_group_request_error_mapper,
)
from ..errors.sensor_insights_create_notification_group_request_error import (
    SensorInsightsCreateNotificationGroupRequestErrorBody,
    sensor_insights_create_notification_group_request_error_mapper,
)
from ..errors.sensor_insights_delete_notification_group_error import (
    SensorInsightsDeleteNotificationGroupErrorBody,
    sensor_insights_delete_notification_group_error_mapper,
)
from ..errors.sensor_insights_list_notification_group_request_error import (
    SensorInsightsListNotificationGroupRequestErrorBody,
    sensor_insights_list_notification_group_request_error_mapper,
)
from ..errors.sensor_insights_remove_users_from_notification_group_request_error import (
    SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody,
    sensor_insights_remove_users_from_notification_group_request_error_mapper,
)
from ..errors.sensor_insights_update_notification_group_request_error import (
    SensorInsightsUpdateNotificationGroupRequestErrorBody,
    sensor_insights_update_notification_group_request_error_mapper,
)
from ..models.dto_add_users_to_notification_group_request import (
    DtoAddUsersToNotificationGroupRequest,
    DtoAddUsersToNotificationGroupRequestDict,
)
from ..models.dto_create_notification_group_request import (
    DtoCreateNotificationGroupRequest,
    DtoCreateNotificationGroupRequestDict,
)
from ..models.dto_delete_notification_group_request import (
    DtoDeleteNotificationGroupRequest,
    DtoDeleteNotificationGroupRequestDict,
)
from ..models.dto_list_notification_group_request import (
    DtoListNotificationGroupRequest,
    DtoListNotificationGroupRequestDict,
)
from ..models.dto_notification_group_response_entity import DtoNotificationGroupResponseEntity
from ..models.dto_remove_users_from_notification_group_request import (
    DtoRemoveUsersFromNotificationGroupRequest,
    DtoRemoveUsersFromNotificationGroupRequestDict,
)
from ..models.dto_update_notification_group_request import (
    DtoUpdateNotificationGroupRequest,
    DtoUpdateNotificationGroupRequestDict,
)
from ..server.server import Server


class SensorInsightsNotificationGroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsNotificationGroupsWithRawResponse(client, server, auth)

    def sensor_insights_add_users_to_notification_group_request(
        self,
        body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Add users to a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_add_users_to_notification_group_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_create_notification_group_request(
        self,
        body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoNotificationGroupResponseEntity:
        """Send a ``POST`` request.

        Args:
            body: Create a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_create_notification_group_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_delete_notification_group(
        self,
        payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            payload: Payload for the delete request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError |
                ManagementError403 | ManagementError404 | RawError``."""
        return self._with_raw_response.sensor_insights_delete_notification_group(
            payload, request_options=request_options
        ).unwrap()

    def sensor_insights_list_notification_group_request(
        self,
        body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoNotificationGroupResponseEntity]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_notification_group_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_remove_users_from_notification_group_request(
        self,
        body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Remove users from a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_remove_users_from_notification_group_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_update_notification_group_request(
        self,
        body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoNotificationGroupResponseEntity:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_update_notification_group_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsNotificationGroupsWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsNotificationGroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsNotificationGroupsWithRawResponse(client, server, auth)

    async def sensor_insights_add_users_to_notification_group_request(
        self,
        body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Add users to a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_add_users_to_notification_group_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_create_notification_group_request(
        self,
        body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoNotificationGroupResponseEntity:
        """Send a ``POST`` request.

        Args:
            body: Create a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_create_notification_group_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_delete_notification_group(
        self,
        payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            payload: Payload for the delete request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError |
                ManagementError403 | ManagementError404 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_delete_notification_group(
                payload, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_list_notification_group_request(
        self,
        body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoNotificationGroupResponseEntity]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_notification_group_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_remove_users_from_notification_group_request(
        self,
        body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Remove users from a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_remove_users_from_notification_group_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_update_notification_group_request(
        self,
        body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoNotificationGroupResponseEntity:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_update_notification_group_request(
                body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsNotificationGroupsWithRawResponse:
        return self._with_raw_response


class SensorInsightsNotificationGroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_add_users_to_notification_group_request(
        self,
        body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsAddUsersToNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Add users to a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups/actions/add-users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_add_users_to_notification_group_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_create_notification_group_request(
        self,
        body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsCreateNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Create a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoNotificationGroupResponseEntity],
            error_mapper=sensor_insights_create_notification_group_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_delete_notification_group(
        self,
        payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsDeleteNotificationGroupErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            payload: Payload for the delete request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups"),
            query_params=[
                param[DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict]("payload", payload)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_delete_notification_group_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_list_notification_group_request(
        self,
        body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoNotificationGroupResponseEntity], SensorInsightsListNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoNotificationGroupResponseEntity]],
            error_mapper=sensor_insights_list_notification_group_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_remove_users_from_notification_group_request(
        self,
        body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Remove users from a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups/actions/remove-users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict](
                body
            ),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_remove_users_from_notification_group_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_update_notification_group_request(
        self,
        body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsUpdateNotificationGroupRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoNotificationGroupResponseEntity],
            error_mapper=sensor_insights_update_notification_group_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsNotificationGroupsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def sensor_insights_add_users_to_notification_group_request(
        self,
        body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsAddUsersToNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Add users to a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups/actions/add-users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_add_users_to_notification_group_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_create_notification_group_request(
        self,
        body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsCreateNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Create a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoNotificationGroupResponseEntity],
            error_mapper=sensor_insights_create_notification_group_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_delete_notification_group(
        self,
        payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsDeleteNotificationGroupErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            payload: Payload for the delete request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups"),
            query_params=[
                param[DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict]("payload", payload)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_delete_notification_group_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_list_notification_group_request(
        self,
        body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoNotificationGroupResponseEntity], SensorInsightsListNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoNotificationGroupResponseEntity]],
            error_mapper=sensor_insights_list_notification_group_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_remove_users_from_notification_group_request(
        self,
        body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Remove users from a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups/actions/remove-users"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict](
                body
            ),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_remove_users_from_notification_group_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_update_notification_group_request(
        self,
        body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsUpdateNotificationGroupRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a notification group
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/notificationGroups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoNotificationGroupResponseEntity],
            error_mapper=sensor_insights_update_notification_group_request_error_mapper,
            request_options=request_options,
        )
