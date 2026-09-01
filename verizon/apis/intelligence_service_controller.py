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
from ..errors.set_connection_planner_error import SetConnectionPlannerErrorBody, set_connection_planner_error_mapper
from ..errors.status_connection_planner_error import (
    StatusConnectionPlannerErrorBody,
    status_connection_planner_error_mapper,
)
from ..models.asynchronous_request_resultforplanner import AsynchronousRequestResultforplanner
from ..models.get_device_statuses_requestforplanner import (
    GetDeviceStatusesRequestforplanner,
    GetDeviceStatusesRequestforplannerDict,
)
from ..models.get_device_statuses_responseforplanner import GetDeviceStatusesResponseforplanner
from ..models.get_devices_windows_requestforplanner import (
    GetDevicesWindowsRequestforplanner,
    GetDevicesWindowsRequestforplannerDict,
)
from ..server.server import Server


class IntelligenceServiceController:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = IntelligenceServiceControllerWithRawResponse(client, server, auth)

    def set_connection_planner(
        self,
        *,
        body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsynchronousRequestResultforplanner:
        """Retrieves available device windows for Connection Planner.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The asynchronous request status.

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``RestErrorResponseforplanner | AuthRestErrorResponseforplanner |
                RawError``."""
        return self._with_raw_response.set_connection_planner(body=body, request_options=request_options).unwrap()

    def status_connection_planner(
        self,
        *,
        body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetDeviceStatusesResponseforplanner:
        """Retrieves the device status for the Connection Planner service.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``RestErrorResponseforplanner | AuthRestErrorResponseforplanner |
                RawError``."""
        return self._with_raw_response.status_connection_planner(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> IntelligenceServiceControllerWithRawResponse:
        return self._with_raw_response


class AsyncIntelligenceServiceController:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncIntelligenceServiceControllerWithRawResponse(client, server, auth)

    async def set_connection_planner(
        self,
        *,
        body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsynchronousRequestResultforplanner:
        """Retrieves available device windows for Connection Planner.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The asynchronous request status.

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``RestErrorResponseforplanner | AuthRestErrorResponseforplanner |
                RawError``."""
        return (
            await self._with_raw_response.set_connection_planner(body=body, request_options=request_options)
        ).unwrap()

    async def status_connection_planner(
        self,
        *,
        body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetDeviceStatusesResponseforplanner:
        """Retrieves the device status for the Connection Planner service.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``RestErrorResponseforplanner | AuthRestErrorResponseforplanner |
                RawError``."""
        return (
            await self._with_raw_response.status_connection_planner(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncIntelligenceServiceControllerWithRawResponse:
        return self._with_raw_response


class IntelligenceServiceControllerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def set_connection_planner(
        self,
        *,
        body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsynchronousRequestResultforplanner, SetConnectionPlannerErrorBody]:
        """Retrieves available device windows for Connection Planner.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/intelligence/device/connection-planner"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AsynchronousRequestResultforplanner],
            error_mapper=set_connection_planner_error_mapper,
            request_options=request_options,
        )

    def status_connection_planner(
        self,
        *,
        body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetDeviceStatusesResponseforplanner, StatusConnectionPlannerErrorBody]:
        """Retrieves the device status for the Connection Planner service.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/intelligence/device/connection-planner/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetDeviceStatusesResponseforplanner],
            error_mapper=status_connection_planner_error_mapper,
            request_options=request_options,
        )


class AsyncIntelligenceServiceControllerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def set_connection_planner(
        self,
        *,
        body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsynchronousRequestResultforplanner, SetConnectionPlannerErrorBody]:
        """Retrieves available device windows for Connection Planner.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/intelligence/device/connection-planner"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AsynchronousRequestResultforplanner],
            error_mapper=set_connection_planner_error_mapper,
            request_options=request_options,
        )

    async def status_connection_planner(
        self,
        *,
        body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetDeviceStatusesResponseforplanner, StatusConnectionPlannerErrorBody]:
        """Retrieves the device status for the Connection Planner service.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/intelligence/device/connection-planner/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetDeviceStatusesResponseforplanner],
            error_mapper=status_connection_planner_error_mapper,
            request_options=request_options,
        )
