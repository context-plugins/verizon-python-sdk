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
from ..models.asynchronous_location_request_result import AsynchronousLocationRequestResult
from ..models.location import Location
from ..models.location_report import LocationReport
from ..models.location_report_status import LocationReportStatus
from ..models.location_request import LocationRequest, LocationRequestDict
from ..models.synchronous_location_request_result import SynchronousLocationRequestResult
from ..models.transaction_id import TransactionId
from ..server.server import Server


class DevicesLocations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DevicesLocationsWithRawResponse(client, server, auth)

    def cancel_queued_location_report_generation(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionId:
        """Cancel a queued device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Report generation cancelled.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_queued_location_report_generation(
            account_name, txid, request_options=request_options
        ).unwrap()

    def create_location_report(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsynchronousLocationRequestResult:
        """Request an asynchronous device location report.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request accepted; location report in progress.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_location_report(request_options=request_options).unwrap()

    def get_location_report_status(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LocationReportStatus:
        """Returns the current status of a requested device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Location report status.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_location_report_status(
            account_name, txid, request_options=request_options
        ).unwrap()

    def list_devices_locations_asynchronous(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SynchronousLocationRequestResult:
        """Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This
        request returns a synchronous transaction ID, and the location information for each device is returned
        asynchronously as a DeviceLocation callback message.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request accepted; location report in progress

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_devices_locations_asynchronous(request_options=request_options).unwrap()

    def list_devices_locations_synchronous(
        self, body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Location]:
        """This locations endpoint retrieves the locations for a list of devices.

        Args:
            body: Request to obtain location of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_devices_locations_synchronous(
            body, request_options=request_options
        ).unwrap()

    def retrieve_location_report(
        self, account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> LocationReport:
        """Download a completed asynchronous device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID from POST /locationreports response.
            startindex: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Location information for up to 1,000 devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_location_report(
            account_name, txid, startindex, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DevicesLocationsWithRawResponse:
        return self._with_raw_response


class AsyncDevicesLocations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDevicesLocationsWithRawResponse(client, server, auth)

    async def cancel_queued_location_report_generation(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionId:
        """Cancel a queued device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Report generation cancelled.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_queued_location_report_generation(
                account_name, txid, request_options=request_options
            )
        ).unwrap()

    async def create_location_report(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsynchronousLocationRequestResult:
        """Request an asynchronous device location report.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request accepted; location report in progress.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_location_report(request_options=request_options)).unwrap()

    async def get_location_report_status(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LocationReportStatus:
        """Returns the current status of a requested device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Location report status.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_location_report_status(
                account_name, txid, request_options=request_options
            )
        ).unwrap()

    async def list_devices_locations_asynchronous(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SynchronousLocationRequestResult:
        """Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This
        request returns a synchronous transaction ID, and the location information for each device is returned
        asynchronously as a DeviceLocation callback message.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request accepted; location report in progress

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_devices_locations_asynchronous(request_options=request_options)
        ).unwrap()

    async def list_devices_locations_synchronous(
        self, body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Location]:
        """This locations endpoint retrieves the locations for a list of devices.

        Args:
            body: Request to obtain location of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_devices_locations_synchronous(body, request_options=request_options)
        ).unwrap()

    async def retrieve_location_report(
        self, account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> LocationReport:
        """Download a completed asynchronous device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID from POST /locationreports response.
            startindex: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Location information for up to 1,000 devices.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_location_report(
                account_name, txid, startindex, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDevicesLocationsWithRawResponse:
        return self._with_raw_response


class DevicesLocationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_queued_location_report_generation(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionId, RawError]:
        """Cancel a queued device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/locationreports/{accountName}/report/{txid}"),
            path_params=[param[str]("accountName", account_name), param[str]("txid", txid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_location_report(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsynchronousLocationRequestResult, RawError]:
        """Request an asynchronous device location report.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/locationreports"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AsynchronousLocationRequestResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_location_report_status(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LocationReportStatus, RawError]:
        """Returns the current status of a requested device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/locationreports/{accountName}/report/{txid}/status"),
            path_params=[param[str]("accountName", account_name), param[str]("txid", txid)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[LocationReportStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_devices_locations_asynchronous(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SynchronousLocationRequestResult, RawError]:
        """Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This
        request returns a synchronous transaction ID, and the location information for each device is returned
        asynchronously as a DeviceLocation callback message.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/devicelocations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SynchronousLocationRequestResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_devices_locations_synchronous(
        self, body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Location], RawError]:
        """This locations endpoint retrieves the locations for a list of devices.

        Args:
            body: Request to obtain location of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/locations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LocationRequest | LocationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Location]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_location_report(
        self, account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LocationReport, RawError]:
        """Download a completed asynchronous device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID from POST /locationreports response.
            startindex: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_location(
                "/locationreports/{accountName}/report/{txid}/index/{startindex}"
            ),
            path_params=[
                param[str]("accountName", account_name), param[str]("txid", txid), param[int]("startindex", startindex)
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[LocationReport],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDevicesLocationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_queued_location_report_generation(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionId, RawError]:
        """Cancel a queued device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/locationreports/{accountName}/report/{txid}"),
            path_params=[param[str]("accountName", account_name), param[str]("txid", txid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_location_report(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsynchronousLocationRequestResult, RawError]:
        """Request an asynchronous device location report.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/locationreports"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AsynchronousLocationRequestResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_location_report_status(
        self, account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LocationReportStatus, RawError]:
        """Returns the current status of a requested device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID of the report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/locationreports/{accountName}/report/{txid}/status"),
            path_params=[param[str]("accountName", account_name), param[str]("txid", txid)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[LocationReportStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_devices_locations_asynchronous(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SynchronousLocationRequestResult, RawError]:
        """Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This
        request returns a synchronous transaction ID, and the location information for each device is returned
        asynchronously as a DeviceLocation callback message.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/devicelocations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SynchronousLocationRequestResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_devices_locations_synchronous(
        self, body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Location], RawError]:
        """This locations endpoint retrieves the locations for a list of devices.

        Args:
            body: Request to obtain location of devices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/locations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LocationRequest | LocationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Location]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_location_report(
        self, account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LocationReport, RawError]:
        """Download a completed asynchronous device location report.

        Args:
            account_name: Account identifier in "##########-#####".
            txid: Transaction ID from POST /locationreports response.
            startindex: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_location(
                "/locationreports/{accountName}/report/{txid}/index/{startindex}"
            ),
            path_params=[
                param[str]("accountName", account_name), param[str]("txid", txid), param[int]("startindex", startindex)
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[LocationReport],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
