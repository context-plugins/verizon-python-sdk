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
from ..errors.sensor_insights_list_gateway_devices_request_error import (
    SensorInsightsListGatewayDevicesRequestErrorBody,
    sensor_insights_list_gateway_devices_request_error_mapper,
)
from ..models.dto_list_devices_request import DtoListDevicesRequest, DtoListDevicesRequestDict
from ..models.resource_device import ResourceDevice
from ..server.server import Server


class SensorInsightsGateways:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsGatewaysWithRawResponse(client, server, auth)

    def sensor_insights_list_gateway_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ResourceDevice]:
        """Send a ``POST`` request.

        Args:
            body: Get gateway information
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_gateway_devices_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsGatewaysWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsGateways:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsGatewaysWithRawResponse(client, server, auth)

    async def sensor_insights_list_gateway_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ResourceDevice]:
        """Send a ``POST`` request.

        Args:
            body: Get gateway information
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_gateway_devices_request(
                body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsGatewaysWithRawResponse:
        return self._with_raw_response


class SensorInsightsGatewaysWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_list_gateway_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ResourceDevice], SensorInsightsListGatewayDevicesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get gateway information
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/gateways/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListDevicesRequest | DtoListDevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceDevice]],
            error_mapper=sensor_insights_list_gateway_devices_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsGatewaysWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_list_gateway_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ResourceDevice], SensorInsightsListGatewayDevicesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get gateway information
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/gateways/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListDevicesRequest | DtoListDevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceDevice]],
            error_mapper=sensor_insights_list_gateway_devices_request_error_mapper,
            request_options=request_options,
        )
