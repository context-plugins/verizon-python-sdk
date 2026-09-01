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
from ..errors.sensor_insights_device_action_set_request_error import (
    SensorInsightsDeviceActionSetRequestErrorBody,
    sensor_insights_device_action_set_request_error_mapper,
)
from ..errors.sensor_insights_last_reported_time_request_error import (
    SensorInsightsLastReportedTimeRequestErrorBody,
    sensor_insights_last_reported_time_request_error_mapper,
)
from ..errors.sensor_insights_list_device_experience_history_request_error import (
    SensorInsightsListDeviceExperienceHistoryRequestErrorBody,
    sensor_insights_list_device_experience_history_request_error_mapper,
)
from ..errors.sensor_insights_list_devices_request_error import (
    SensorInsightsListDevicesRequestErrorBody,
    sensor_insights_list_devices_request_error_mapper,
)
from ..errors.sensor_insights_list_network_experience_history_request_error import (
    SensorInsightsListNetworkExperienceHistoryRequestErrorBody,
    sensor_insights_list_network_experience_history_request_error_mapper,
)
from ..errors.sensor_insights_patch_device_request_error import (
    SensorInsightsPatchDeviceRequestErrorBody,
    sensor_insights_patch_device_request_error_mapper,
)
from ..models.dto_device_action_set_response import DtoDeviceActionSetResponse
from ..models.dto_expanded_device_response import DtoExpandedDeviceResponse
from ..models.dto_last_reported_time_request import DtoLastReportedTimeRequest, DtoLastReportedTimeRequestDict
from ..models.dto_last_reported_time_response import DtoLastReportedTimeResponse
from ..models.dto_list_device_experience_history_request import (
    DtoListDeviceExperienceHistoryRequest,
    DtoListDeviceExperienceHistoryRequestDict,
)
from ..models.dto_list_devices_request import DtoListDevicesRequest, DtoListDevicesRequestDict
from ..models.dto_list_network_experience_history_request import (
    DtoListNetworkExperienceHistoryRequest,
    DtoListNetworkExperienceHistoryRequestDict,
)
from ..models.dto_patch_device_request import DtoPatchDeviceRequest, DtoPatchDeviceRequestDict
from ..models.resource_device import ResourceDevice
from ..models.unions.dm_v1_devices_actions_set_request import (
    DmV1DevicesActionsSetRequest,
    DmV1DevicesActionsSetRequestDict,
)
from ..models.user_device_experience_history import UserDeviceExperienceHistory
from ..models.user_network_experience_history import UserNetworkExperienceHistory
from ..server.server import Server


class SensorInsightsDevices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsDevicesWithRawResponse(client, server, auth)

    def sensor_insights_device_action_set_request(
        self,
        body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoDeviceActionSetResponse:
        """Send a ``POST`` request.

        Args:
            body: Set device configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError403 |
                ManagementError404 | RawError``."""
        return self._with_raw_response.sensor_insights_device_action_set_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_last_reported_time_request(
        self,
        body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoLastReportedTimeResponse:
        """Send a ``POST`` request.

        Args:
            body: Get the last reported information for a device
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError403 |
                ManagementError404 | RawError``."""
        return self._with_raw_response.sensor_insights_last_reported_time_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_list_device_experience_history_request(
        self,
        body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UserDeviceExperienceHistory]:
        """Send a ``POST`` request.

        Args:
            body: List the device experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_device_experience_history_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_list_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoExpandedDeviceResponse]:
        """Send a ``POST`` request.

        Args:
            body: List all device details on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError | RawError``."""
        return self._with_raw_response.sensor_insights_list_devices_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_list_network_experience_history_request(
        self,
        body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UserNetworkExperienceHistory]:
        """Send a ``POST`` request.

        Args:
            body: List the network experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_network_experience_history_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_patch_device_request(
        self,
        body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceDevice:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a device's details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_patch_device_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsDevicesWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsDevices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsDevicesWithRawResponse(client, server, auth)

    async def sensor_insights_device_action_set_request(
        self,
        body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoDeviceActionSetResponse:
        """Send a ``POST`` request.

        Args:
            body: Set device configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError403 |
                ManagementError404 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_device_action_set_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_last_reported_time_request(
        self,
        body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DtoLastReportedTimeResponse:
        """Send a ``POST`` request.

        Args:
            body: Get the last reported information for a device
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request Forbidden Not Found ``error`` is ``ManagementError400 | ManagementError403 |
                ManagementError404 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_last_reported_time_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_list_device_experience_history_request(
        self,
        body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UserDeviceExperienceHistory]:
        """Send a ``POST`` request.

        Args:
            body: List the device experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_device_experience_history_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_list_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DtoExpandedDeviceResponse]:
        """Send a ``POST`` request.

        Args:
            body: List all device details on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_devices_request(body, request_options=request_options)
        ).unwrap()

    async def sensor_insights_list_network_experience_history_request(
        self,
        body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UserNetworkExperienceHistory]:
        """Send a ``POST`` request.

        Args:
            body: List the network experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_network_experience_history_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_patch_device_request(
        self,
        body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceDevice:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a device's details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_patch_device_request(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsDevicesWithRawResponse:
        return self._with_raw_response


class SensorInsightsDevicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_device_action_set_request(
        self,
        body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoDeviceActionSetResponse, SensorInsightsDeviceActionSetRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Set device configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/actions/set"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoDeviceActionSetResponse],
            error_mapper=sensor_insights_device_action_set_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_last_reported_time_request(
        self,
        body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoLastReportedTimeResponse, SensorInsightsLastReportedTimeRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get the last reported information for a device
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/lastreported"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoLastReportedTimeResponse],
            error_mapper=sensor_insights_last_reported_time_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_list_device_experience_history_request(
        self,
        body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UserDeviceExperienceHistory], SensorInsightsListDeviceExperienceHistoryRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List the device experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/experience/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[UserDeviceExperienceHistory]],
            error_mapper=sensor_insights_list_device_experience_history_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_list_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoExpandedDeviceResponse], SensorInsightsListDevicesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List all device details on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListDevicesRequest | DtoListDevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoExpandedDeviceResponse]],
            error_mapper=sensor_insights_list_devices_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_list_network_experience_history_request(
        self,
        body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UserNetworkExperienceHistory], SensorInsightsListNetworkExperienceHistoryRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List the network experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/networkexperience/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[UserNetworkExperienceHistory]],
            error_mapper=sensor_insights_list_network_experience_history_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_patch_device_request(
        self,
        body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceDevice, SensorInsightsPatchDeviceRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a device's details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoPatchDeviceRequest | DtoPatchDeviceRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceDevice],
            error_mapper=sensor_insights_patch_device_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsDevicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_device_action_set_request(
        self,
        body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoDeviceActionSetResponse, SensorInsightsDeviceActionSetRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Set device configuration
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/actions/set"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoDeviceActionSetResponse],
            error_mapper=sensor_insights_device_action_set_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_last_reported_time_request(
        self,
        body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DtoLastReportedTimeResponse, SensorInsightsLastReportedTimeRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Get the last reported information for a device
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/lastreported"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoLastReportedTimeResponse],
            error_mapper=sensor_insights_last_reported_time_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_list_device_experience_history_request(
        self,
        body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UserDeviceExperienceHistory], SensorInsightsListDeviceExperienceHistoryRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List the device experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/experience/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[UserDeviceExperienceHistory]],
            error_mapper=sensor_insights_list_device_experience_history_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_list_devices_request(
        self,
        body: DtoListDevicesRequest | DtoListDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DtoExpandedDeviceResponse], SensorInsightsListDevicesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List all device details on an account
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListDevicesRequest | DtoListDevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DtoExpandedDeviceResponse]],
            error_mapper=sensor_insights_list_devices_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_list_network_experience_history_request(
        self,
        body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UserNetworkExperienceHistory], SensorInsightsListNetworkExperienceHistoryRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: List the network experience
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices/networkexperience/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[UserNetworkExperienceHistory]],
            error_mapper=sensor_insights_list_network_experience_history_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_patch_device_request(
        self,
        body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceDevice, SensorInsightsPatchDeviceRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a device's details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/devices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoPatchDeviceRequest | DtoPatchDeviceRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceDevice],
            error_mapper=sensor_insights_patch_device_request_error_mapper,
            request_options=request_options,
        )
