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
from ..errors.sensor_insights_bulk_update_error import (
    SensorInsightsBulkUpdateErrorBody,
    sensor_insights_bulk_update_error_mapper,
)
from ..errors.sensor_insights_list_smart_alerts_request_error import (
    SensorInsightsListSmartAlertsRequestErrorBody,
    sensor_insights_list_smart_alerts_request_error_mapper,
)
from ..errors.sensor_insights_patch_smart_alert_request_error import (
    SensorInsightsPatchSmartAlertRequestErrorBody,
    sensor_insights_patch_smart_alert_request_error_mapper,
)
from ..models.dto_bulk_update import DtoBulkUpdate, DtoBulkUpdateDict
from ..models.dto_list_smart_alerts_request import DtoListSmartAlertsRequest, DtoListSmartAlertsRequestDict
from ..models.dto_patch_smart_alert_request import DtoPatchSmartAlertRequest, DtoPatchSmartAlertRequestDict
from ..models.user_smart_alert import UserSmartAlert
from ..server.server import Server


class SensorInsightsSmartAlerts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsSmartAlertsWithRawResponse(client, server, auth)

    def sensor_insights_bulk_update(
        self, body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserSmartAlert:
        """Send a ``POST`` request.

        Args:
            body: Bulk update smart alerts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_bulk_update(body, request_options=request_options).unwrap()

    def sensor_insights_list_smart_alerts_request(
        self,
        body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UserSmartAlert]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_smart_alerts_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_patch_smart_alert_request(
        self,
        body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserSmartAlert:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_patch_smart_alert_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsSmartAlertsWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsSmartAlerts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsSmartAlertsWithRawResponse(client, server, auth)

    async def sensor_insights_bulk_update(
        self, body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserSmartAlert:
        """Send a ``POST`` request.

        Args:
            body: Bulk update smart alerts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_bulk_update(body, request_options=request_options)
        ).unwrap()

    async def sensor_insights_list_smart_alerts_request(
        self,
        body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UserSmartAlert]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_smart_alerts_request(
                body, request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_patch_smart_alert_request(
        self,
        body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UserSmartAlert:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_patch_smart_alert_request(
                body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsSmartAlertsWithRawResponse:
        return self._with_raw_response


class SensorInsightsSmartAlertsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_bulk_update(
        self, body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserSmartAlert, SensorInsightsBulkUpdateErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Bulk update smart alerts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts/actions/bulkupdate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoBulkUpdate | DtoBulkUpdateDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UserSmartAlert],
            error_mapper=sensor_insights_bulk_update_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_list_smart_alerts_request(
        self,
        body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UserSmartAlert], SensorInsightsListSmartAlertsRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[UserSmartAlert]],
            error_mapper=sensor_insights_list_smart_alerts_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_patch_smart_alert_request(
        self,
        body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserSmartAlert, SensorInsightsPatchSmartAlertRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UserSmartAlert],
            error_mapper=sensor_insights_patch_smart_alert_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsSmartAlertsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_bulk_update(
        self, body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserSmartAlert, SensorInsightsBulkUpdateErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Bulk update smart alerts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts/actions/bulkupdate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoBulkUpdate | DtoBulkUpdateDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UserSmartAlert],
            error_mapper=sensor_insights_bulk_update_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_list_smart_alerts_request(
        self,
        body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UserSmartAlert], SensorInsightsListSmartAlertsRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[UserSmartAlert]],
            error_mapper=sensor_insights_list_smart_alerts_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_patch_smart_alert_request(
        self,
        body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UserSmartAlert, SensorInsightsPatchSmartAlertRequestErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            body: Partially update a smart alert
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UserSmartAlert],
            error_mapper=sensor_insights_patch_smart_alert_request_error_mapper,
            request_options=request_options,
        )
