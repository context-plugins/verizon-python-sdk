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
from ..errors.sensor_insights_list_sensor_devices_request_error import (
    SensorInsightsListSensorDevicesRequestErrorBody,
    sensor_insights_list_sensor_devices_request_error_mapper,
)
from ..errors.sensor_insights_off_board_sensor_request_error import (
    SensorInsightsOffBoardSensorRequestErrorBody,
    sensor_insights_off_board_sensor_request_error_mapper,
)
from ..errors.sensor_insights_on_board_sensor_request_error import (
    SensorInsightsOnBoardSensorRequestErrorBody,
    sensor_insights_on_board_sensor_request_error_mapper,
)
from ..errors.sensor_insights_sensor_off_boarding_status_request_error import (
    SensorInsightsSensorOffBoardingStatusRequestErrorBody,
    sensor_insights_sensor_off_boarding_status_request_error_mapper,
)
from ..errors.sensor_insights_sensor_on_board_status_request_error import (
    SensorInsightsSensorOnBoardStatusRequestErrorBody,
    sensor_insights_sensor_on_board_status_request_error_mapper,
)
from ..models.dto_list_sensor_devices_request import DtoListSensorDevicesRequest, DtoListSensorDevicesRequestDict
from ..models.dto_off_board_sensor_request import DtoOffBoardSensorRequest, DtoOffBoardSensorRequestDict
from ..models.dto_on_board_sensor_request import DtoOnBoardSensorRequest, DtoOnBoardSensorRequestDict
from ..models.dto_sensor_off_board_status_request import (
    DtoSensorOffBoardStatusRequest,
    DtoSensorOffBoardStatusRequestDict,
)
from ..models.dto_sensor_off_boarding_status_response import DtoSensorOffBoardingStatusResponse
from ..models.dto_sensor_on_board_status_request import DtoSensorOnBoardStatusRequest, DtoSensorOnBoardStatusRequestDict
from ..models.dto_sensor_on_boarding_status_response import DtoSensorOnBoardingStatusResponse
from ..models.resource_device import ResourceDevice
from ..server.server import Server


class SensorInsightsSensors:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsSensorsWithRawResponse(client, server, auth)

    def sensor_insights_list_sensor_devices_request(
        self,
        body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ResourceDevice]:
        """Send a ``POST`` request.

        Args:
            body: List details of the sensors
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_sensor_devices_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_off_board_sensor_request(
        self,
        body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Offboard a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden ``error`` is ``ManagementError400 | ManagementError |
                ManagementError403 | RawError``."""
        return self._with_raw_response.sensor_insights_off_board_sensor_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_on_board_sensor_request(
        self,
        body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Onboarding a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_on_board_sensor_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_sensor_off_boarding_status_request(
        self,
        body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoSensorOffBoardingStatusResponse:
        """Send a ``POST`` request.

        Args:
            body: Get a sensor's offboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_sensor_off_boarding_status_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_sensor_on_board_status_request(
        self,
        body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoSensorOnBoardingStatusResponse:
        """Send a ``POST`` request.

        Args:
            body: Get the sensor's onboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_sensor_on_board_status_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsSensorsWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsSensors:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsSensorsWithRawResponse(client, server, auth)

    async def sensor_insights_list_sensor_devices_request(
        self,
        body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ResourceDevice]:
        """Send a ``POST`` request.

        Args:
            body: List details of the sensors
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_sensor_devices_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_off_board_sensor_request(
        self,
        body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Offboard a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden ``error`` is ``ManagementError400 | ManagementError |
                ManagementError403 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_off_board_sensor_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_on_board_sensor_request(
        self,
        body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            body: Onboarding a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_on_board_sensor_request(body, request_options=request_options)
        ).unwrap()

    async def sensor_insights_sensor_off_boarding_status_request(
        self,
        body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoSensorOffBoardingStatusResponse:
        """Send a ``POST`` request.

        Args:
            body: Get a sensor's offboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_sensor_off_boarding_status_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_sensor_on_board_status_request(
        self,
        body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoSensorOnBoardingStatusResponse:
        """Send a ``POST`` request.

        Args:
            body: Get the sensor's onboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_sensor_on_board_status_request(
                body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsSensorsWithRawResponse:
        return self._with_raw_response


class SensorInsightsSensorsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_list_sensor_devices_request(
        self,
        body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ResourceDevice], SensorInsightsListSensorDevicesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List details of the sensors
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceDevice]],
            error_mapper=sensor_insights_list_sensor_devices_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_off_board_sensor_request(
        self,
        body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsOffBoardSensorRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Offboard a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/offboard"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_off_board_sensor_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_on_board_sensor_request(
        self,
        body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsOnBoardSensorRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Onboarding a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/onboard"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_on_board_sensor_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_sensor_off_boarding_status_request(
        self,
        body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoSensorOffBoardingStatusResponse, SensorInsightsSensorOffBoardingStatusRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get a sensor's offboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/offboard/status/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoSensorOffBoardingStatusResponse],
            error_mapper=sensor_insights_sensor_off_boarding_status_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_sensor_on_board_status_request(
        self,
        body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoSensorOnBoardingStatusResponse, SensorInsightsSensorOnBoardStatusRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get the sensor's onboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/onboard/status/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoSensorOnBoardingStatusResponse],
            error_mapper=sensor_insights_sensor_on_board_status_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsSensorsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_list_sensor_devices_request(
        self,
        body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ResourceDevice], SensorInsightsListSensorDevicesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List details of the sensors
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceDevice]],
            error_mapper=sensor_insights_list_sensor_devices_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_off_board_sensor_request(
        self,
        body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsOffBoardSensorRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Offboard a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/offboard"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_off_board_sensor_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_on_board_sensor_request(
        self,
        body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SensorInsightsOnBoardSensorRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Onboarding a sensor
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/onboard"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=sensor_insights_on_board_sensor_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_sensor_off_boarding_status_request(
        self,
        body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoSensorOffBoardingStatusResponse, SensorInsightsSensorOffBoardingStatusRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get a sensor's offboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/offboard/status/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoSensorOffBoardingStatusResponse],
            error_mapper=sensor_insights_sensor_off_boarding_status_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_sensor_on_board_status_request(
        self,
        body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoSensorOnBoardingStatusResponse, SensorInsightsSensorOnBoardStatusRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get the sensor's onboarding status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/sensors/onboard/status/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoSensorOnBoardingStatusResponse],
            error_mapper=sensor_insights_sensor_on_board_status_request_error_mapper,
            request_options=request_options,
        )
