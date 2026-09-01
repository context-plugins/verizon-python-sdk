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
from ..errors.create_anomaly_detection_trigger_error import (
    CreateAnomalyDetectionTriggerErrorBody,
    create_anomaly_detection_trigger_error_mapper,
)
from ..errors.list_anomaly_detection_trigger_settings_error import (
    ListAnomalyDetectionTriggerSettingsErrorBody,
    list_anomaly_detection_trigger_settings_error_mapper,
)
from ..errors.list_anomaly_detection_triggers_error import (
    ListAnomalyDetectionTriggersErrorBody,
    list_anomaly_detection_triggers_error_mapper,
)
from ..errors.update_anomaly_detection_trigger_error import (
    UpdateAnomalyDetectionTriggerErrorBody,
    update_anomaly_detection_trigger_error_mapper,
)
from ..models.anomaly_detection_trigger import AnomalyDetectionTrigger
from ..models.create_trigger_request import CreateTriggerRequest, CreateTriggerRequestDict
from ..models.get_trigger_response_list import GetTriggerResponseList
from ..models.update_trigger_request import UpdateTriggerRequest, UpdateTriggerRequestDict
from ..server.server import Server


class AnomalyTriggers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AnomalyTriggersWithRawResponse(client, server, auth)

    def create_anomaly_detection_trigger(
        self,
        body: CreateTriggerRequest | CreateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnomalyDetectionTrigger:
        """This corresponds to the M2M-MC SOAP interface, ````CreateTrigger````.

        Args:
            body: Create Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trigger ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return self._with_raw_response.create_anomaly_detection_trigger(body, request_options=request_options).unwrap()

    def delete_anomaly_detection_trigger(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnomalyDetectionTrigger:
        """Deletes a specific trigger ID

        Args:
            trigger_id: The trigger ID to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The ID of the deleted trigger is returned

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_anomaly_detection_trigger(
            trigger_id, request_options=request_options
        ).unwrap()

    def list_anomaly_detection_trigger_settings(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GetTriggerResponseList]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            trigger_id: trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trigger information associated to a Trigger Id

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return self._with_raw_response.list_anomaly_detection_trigger_settings(
            trigger_id, request_options=request_options
        ).unwrap()

    def list_anomaly_detection_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GetTriggerResponseList]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of triggers associated to a Contact

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return self._with_raw_response.list_anomaly_detection_triggers(request_options=request_options).unwrap()

    def update_anomaly_detection_trigger(
        self,
        body: UpdateTriggerRequest | UpdateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnomalyDetectionTrigger:
        """This corresponds to the M2M-MC SOAP interface, ````UpdateTriggerRequest````.

        Args:
            body: Update Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trigger ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return self._with_raw_response.update_anomaly_detection_trigger(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AnomalyTriggersWithRawResponse:
        return self._with_raw_response


class AsyncAnomalyTriggers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAnomalyTriggersWithRawResponse(client, server, auth)

    async def create_anomaly_detection_trigger(
        self,
        body: CreateTriggerRequest | CreateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnomalyDetectionTrigger:
        """This corresponds to the M2M-MC SOAP interface, ````CreateTrigger````.

        Args:
            body: Create Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trigger ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return (
            await self._with_raw_response.create_anomaly_detection_trigger(body, request_options=request_options)
        ).unwrap()

    async def delete_anomaly_detection_trigger(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnomalyDetectionTrigger:
        """Deletes a specific trigger ID

        Args:
            trigger_id: The trigger ID to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The ID of the deleted trigger is returned

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_anomaly_detection_trigger(trigger_id, request_options=request_options)
        ).unwrap()

    async def list_anomaly_detection_trigger_settings(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GetTriggerResponseList]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            trigger_id: trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trigger information associated to a Trigger Id

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return (
            await self._with_raw_response.list_anomaly_detection_trigger_settings(
                trigger_id, request_options=request_options
            )
        ).unwrap()

    async def list_anomaly_detection_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GetTriggerResponseList]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of triggers associated to a Contact

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return (await self._with_raw_response.list_anomaly_detection_triggers(request_options=request_options)).unwrap()

    async def update_anomaly_detection_trigger(
        self,
        body: UpdateTriggerRequest | UpdateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnomalyDetectionTrigger:
        """This corresponds to the M2M-MC SOAP interface, ````UpdateTriggerRequest````.

        Args:
            body: Update Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Trigger ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``IntelligenceResult | RawError``."""
        return (
            await self._with_raw_response.update_anomaly_detection_trigger(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAnomalyTriggersWithRawResponse:
        return self._with_raw_response


class AnomalyTriggersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_anomaly_detection_trigger(
        self,
        body: CreateTriggerRequest | CreateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnomalyDetectionTrigger, CreateAnomalyDetectionTriggerErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````CreateTrigger````.

        Args:
            body: Create Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTriggerRequest | CreateTriggerRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=create_anomaly_detection_trigger_error_mapper,
            request_options=request_options,
        )

    def delete_anomaly_detection_trigger(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnomalyDetectionTrigger, RawError]:
        """Deletes a specific trigger ID

        Args:
            trigger_id: The trigger ID to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_anomaly_detection_trigger_settings(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggerSettingsErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            trigger_id: trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[GetTriggerResponseList]],
            error_mapper=list_anomaly_detection_trigger_settings_error_mapper,
            request_options=request_options,
        )

    def list_anomaly_detection_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggersErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers"),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[GetTriggerResponseList]],
            error_mapper=list_anomaly_detection_triggers_error_mapper,
            request_options=request_options,
        )

    def update_anomaly_detection_trigger(
        self,
        body: UpdateTriggerRequest | UpdateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnomalyDetectionTrigger, UpdateAnomalyDetectionTriggerErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````UpdateTriggerRequest````.

        Args:
            body: Update Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateTriggerRequest | UpdateTriggerRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=update_anomaly_detection_trigger_error_mapper,
            request_options=request_options,
        )


class AsyncAnomalyTriggersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_anomaly_detection_trigger(
        self,
        body: CreateTriggerRequest | CreateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnomalyDetectionTrigger, CreateAnomalyDetectionTriggerErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````CreateTrigger````.

        Args:
            body: Create Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTriggerRequest | CreateTriggerRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=create_anomaly_detection_trigger_error_mapper,
            request_options=request_options,
        )

    async def delete_anomaly_detection_trigger(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnomalyDetectionTrigger, RawError]:
        """Deletes a specific trigger ID

        Args:
            trigger_id: The trigger ID to be deleted
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_anomaly_detection_trigger_settings(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggerSettingsErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            trigger_id: trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[GetTriggerResponseList]],
            error_mapper=list_anomaly_detection_trigger_settings_error_mapper,
            request_options=request_options,
        )

    async def list_anomaly_detection_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggersErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````GetTriggers````.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers"),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[GetTriggerResponseList]],
            error_mapper=list_anomaly_detection_triggers_error_mapper,
            request_options=request_options,
        )

    async def update_anomaly_detection_trigger(
        self,
        body: UpdateTriggerRequest | UpdateTriggerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnomalyDetectionTrigger, UpdateAnomalyDetectionTriggerErrorBody]:
        """This corresponds to the M2M-MC SOAP interface, ````UpdateTriggerRequest````.

        Args:
            body: Update Trigger Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateTriggerRequest | UpdateTriggerRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionTrigger],
            error_mapper=update_anomaly_detection_trigger_error_mapper,
            request_options=request_options,
        )
