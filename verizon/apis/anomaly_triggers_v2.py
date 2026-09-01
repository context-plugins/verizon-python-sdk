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
from ..models.anomaly_detection_trigger import AnomalyDetectionTrigger
from ..models.anomaly_trigger_result import AnomalyTriggerResult
from ..models.intelligence_success_result import IntelligenceSuccessResult
from ..models.unions.create_trigger_request_options import CreateTriggerRequestOptions, CreateTriggerRequestOptionsDict
from ..models.unions.update_trigger_request_options import UpdateTriggerRequestOptions, UpdateTriggerRequestOptionsDict
from ..server.server import Server


class AnomalyTriggersV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AnomalyTriggersV2WithRawResponse(client, server, auth)

    def create_anomaly_detection_trigger_v2(
        self,
        body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnomalyDetectionTrigger:
        """Creates the trigger to identify an anomaly.

        Args:
            body: Request to create an anomaly trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of request to create a trigger for anomaly detection.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_anomaly_detection_trigger_v2(
            body, request_options=request_options
        ).unwrap()

    def list_anomaly_detection_trigger_settings_v2(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnomalyTriggerResult:
        """Retrieves the values for a specific trigger ID.

        Args:
            trigger_id: The trigger ID of a specific trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Anomaly detection trigger details.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_anomaly_detection_trigger_settings_v2(
            trigger_id, request_options=request_options
        ).unwrap()

    def update_anomaly_detection_trigger_v2(
        self,
        body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IntelligenceSuccessResult:
        """Updates an existing trigger using the account name.

        Args:
            body: Request to update existing trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_anomaly_detection_trigger_v2(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AnomalyTriggersV2WithRawResponse:
        return self._with_raw_response


class AsyncAnomalyTriggersV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAnomalyTriggersV2WithRawResponse(client, server, auth)

    async def create_anomaly_detection_trigger_v2(
        self,
        body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnomalyDetectionTrigger:
        """Creates the trigger to identify an anomaly.

        Args:
            body: Request to create an anomaly trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of request to create a trigger for anomaly detection.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_anomaly_detection_trigger_v2(body, request_options=request_options)
        ).unwrap()

    async def list_anomaly_detection_trigger_settings_v2(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnomalyTriggerResult:
        """Retrieves the values for a specific trigger ID.

        Args:
            trigger_id: The trigger ID of a specific trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Anomaly detection trigger details.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_anomaly_detection_trigger_settings_v2(
                trigger_id, request_options=request_options
            )
        ).unwrap()

    async def update_anomaly_detection_trigger_v2(
        self,
        body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IntelligenceSuccessResult:
        """Updates an existing trigger using the account name.

        Args:
            body: Request to update existing trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_anomaly_detection_trigger_v2(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAnomalyTriggersV2WithRawResponse:
        return self._with_raw_response


class AnomalyTriggersV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_anomaly_detection_trigger_v2(
        self,
        body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnomalyDetectionTrigger, RawError]:
        """Creates the trigger to identify an anomaly.

        Args:
            body: Request to create an anomaly trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict]](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_anomaly_detection_trigger_settings_v2(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnomalyTriggerResult, RawError]:
        """Retrieves the values for a specific trigger ID.

        Args:
            trigger_id: The trigger ID of a specific trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyTriggerResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_anomaly_detection_trigger_v2(
        self,
        body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IntelligenceSuccessResult, RawError]:
        """Updates an existing trigger using the account name.

        Args:
            body: Request to update existing trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict]](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[IntelligenceSuccessResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAnomalyTriggersV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_anomaly_detection_trigger_v2(
        self,
        body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnomalyDetectionTrigger, RawError]:
        """Creates the trigger to identify an anomaly.

        Args:
            body: Request to create an anomaly trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict]](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_anomaly_detection_trigger_settings_v2(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnomalyTriggerResult, RawError]:
        """Retrieves the values for a specific trigger ID.

        Args:
            trigger_id: The trigger ID of a specific trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyTriggerResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_anomaly_detection_trigger_v2(
        self,
        body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IntelligenceSuccessResult, RawError]:
        """Updates an existing trigger using the account name.

        Args:
            body: Request to update existing trigger.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict]](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[IntelligenceSuccessResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
