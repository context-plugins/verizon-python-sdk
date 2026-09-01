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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.change_configuration_request import ChangeConfigurationRequest, ChangeConfigurationRequestDict
from ..models.change_configuration_response import ChangeConfigurationResponse
from ..models.find_device_by_property_response_list import FindDeviceByPropertyResponseList
from ..models.query_subscription_request import QuerySubscriptionRequest, QuerySubscriptionRequestDict
from ..models.remove_device_request import RemoveDeviceRequest, RemoveDeviceRequestDict
from ..models.search_device_by_property_response_list import SearchDeviceByPropertyResponseList
from ..models.search_device_event_history_request import (
    SearchDeviceEventHistoryRequest,
    SearchDeviceEventHistoryRequestDict,
)
from ..models.search_device_event_history_response_list import SearchDeviceEventHistoryResponseList
from ..models.search_sensor_history_request import SearchSensorHistoryRequest, SearchSensorHistoryRequestDict
from ..models.search_sensor_history_response_list import SearchSensorHistoryResponseList
from ..server.server import Server


class CloudConnectorDevices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CloudConnectorDevicesWithRawResponse(client, server, auth)

    def delete_device_from_account(
        self,
        body: RemoveDeviceRequest | RemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a device from a ThingSpace account.

        Args:
            body: The request body identifies the device to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_device_from_account(body, request_options=request_options).unwrap()

    def find_device_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FindDeviceByPropertyResponseList:
        """Find devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices. Each device includes the full device resource
            definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.find_device_by_property_values(body, request_options=request_options).unwrap()

    def search_device_event_history(
        self,
        body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchDeviceEventHistoryResponseList:
        """Search device event history to find events that match criteria.Sensor readings, configuration changes, and
        other device data are all stored as events.

        Args:
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_device_event_history(body, request_options=request_options).unwrap()

    def search_devices_resources_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchDeviceByPropertyResponseList:
        """Search for devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_devices_resources_by_property_values(
            body, request_options=request_options
        ).unwrap()

    def search_sensor_readings(
        self,
        fieldname: str,
        body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchSensorHistoryResponseList:
        """Returns the readings of a specified sensor, with the most recent reading first. Sensor readings are stored as
        events; this request an array of events.

        Args:
            fieldname: The name of the sensor.
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_sensor_readings(fieldname, body, request_options=request_options).unwrap()

    def update_devices_configuration_value(
        self,
        body: ChangeConfigurationRequest | ChangeConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangeConfigurationResponse:
        """Change configuration values on a device, such as setting how often a device records and reports sensor
        readings.

        Args:
            body: The request body changes configuration values on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response contains the ts.event.configuration event that was created to record the change.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_devices_configuration_value(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CloudConnectorDevicesWithRawResponse:
        return self._with_raw_response


class AsyncCloudConnectorDevices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCloudConnectorDevicesWithRawResponse(client, server, auth)

    async def delete_device_from_account(
        self,
        body: RemoveDeviceRequest | RemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a device from a ThingSpace account.

        Args:
            body: The request body identifies the device to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_device_from_account(body, request_options=request_options)
        ).unwrap()

    async def find_device_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FindDeviceByPropertyResponseList:
        """Find devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices. Each device includes the full device resource
            definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.find_device_by_property_values(body, request_options=request_options)
        ).unwrap()

    async def search_device_event_history(
        self,
        body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchDeviceEventHistoryResponseList:
        """Search device event history to find events that match criteria.Sensor readings, configuration changes, and
        other device data are all stored as events.

        Args:
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_device_event_history(body, request_options=request_options)
        ).unwrap()

    async def search_devices_resources_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchDeviceByPropertyResponseList:
        """Search for devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_devices_resources_by_property_values(
                body, request_options=request_options
            )
        ).unwrap()

    async def search_sensor_readings(
        self,
        fieldname: str,
        body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchSensorHistoryResponseList:
        """Returns the readings of a specified sensor, with the most recent reading first. Sensor readings are stored as
        events; this request an array of events.

        Args:
            fieldname: The name of the sensor.
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_sensor_readings(fieldname, body, request_options=request_options)
        ).unwrap()

    async def update_devices_configuration_value(
        self,
        body: ChangeConfigurationRequest | ChangeConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangeConfigurationResponse:
        """Change configuration values on a device, such as setting how often a device records and reports sensor
        readings.

        Args:
            body: The request body changes configuration values on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response contains the ts.event.configuration event that was created to record the change.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_devices_configuration_value(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCloudConnectorDevicesWithRawResponse:
        return self._with_raw_response


class CloudConnectorDevicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_device_from_account(
        self,
        body: RemoveDeviceRequest | RemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a device from a ThingSpace account.

        Args:
            body: The request body identifies the device to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveDeviceRequest | RemoveDeviceRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def find_device_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FindDeviceByPropertyResponseList, RawError]:
        """Find devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QuerySubscriptionRequest | QuerySubscriptionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FindDeviceByPropertyResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_device_event_history(
        self,
        body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchDeviceEventHistoryResponseList, RawError]:
        """Search device event history to find events that match criteria.Sensor readings, configuration changes, and
        other device data are all stored as events.

        Args:
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/fields/actions/history/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SearchDeviceEventHistoryResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_devices_resources_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchDeviceByPropertyResponseList, RawError]:
        """Search for devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/actions/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QuerySubscriptionRequest | QuerySubscriptionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SearchDeviceByPropertyResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_sensor_readings(
        self,
        fieldname: str,
        body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchSensorHistoryResponseList, RawError]:
        """Returns the readings of a specified sensor, with the most recent reading first. Sensor readings are stored as
        events; this request an array of events.

        Args:
            fieldname: The name of the sensor.
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/fields/{fieldname}/actions/history"),
            path_params=[param[str]("fieldname", fieldname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchSensorHistoryRequest | SearchSensorHistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SearchSensorHistoryResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_devices_configuration_value(
        self,
        body: ChangeConfigurationRequest | ChangeConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangeConfigurationResponse, RawError]:
        """Change configuration values on a device, such as setting how often a device records and reports sensor
        readings.

        Args:
            body: The request body changes configuration values on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/configuration/actions/set"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangeConfigurationRequest | ChangeConfigurationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangeConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCloudConnectorDevicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_device_from_account(
        self,
        body: RemoveDeviceRequest | RemoveDeviceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a device from a ThingSpace account.

        Args:
            body: The request body identifies the device to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveDeviceRequest | RemoveDeviceRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def find_device_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FindDeviceByPropertyResponseList, RawError]:
        """Find devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QuerySubscriptionRequest | QuerySubscriptionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FindDeviceByPropertyResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_device_event_history(
        self,
        body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchDeviceEventHistoryResponseList, RawError]:
        """Search device event history to find events that match criteria.Sensor readings, configuration changes, and
        other device data are all stored as events.

        Args:
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/fields/actions/history/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SearchDeviceEventHistoryResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_devices_resources_by_property_values(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchDeviceByPropertyResponseList, RawError]:
        """Search for devices by property values. Returns an array of all matching device resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/actions/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QuerySubscriptionRequest | QuerySubscriptionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SearchDeviceByPropertyResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_sensor_readings(
        self,
        fieldname: str,
        body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchSensorHistoryResponseList, RawError]:
        """Returns the readings of a specified sensor, with the most recent reading first. Sensor readings are stored as
        events; this request an array of events.

        Args:
            fieldname: The name of the sensor.
            body: The device identifier and fields to match in the search.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/fields/{fieldname}/actions/history"),
            path_params=[param[str]("fieldname", fieldname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchSensorHistoryRequest | SearchSensorHistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SearchSensorHistoryResponseList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_devices_configuration_value(
        self,
        body: ChangeConfigurationRequest | ChangeConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangeConfigurationResponse, RawError]:
        """Change configuration values on a device, such as setting how often a device records and reports sensor
        readings.

        Args:
            body: The request body changes configuration values on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/devices/configuration/actions/set"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangeConfigurationRequest | ChangeConfigurationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangeConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
