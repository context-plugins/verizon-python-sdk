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
from ..models.request_trigger import RequestTrigger, RequestTriggerDict
from ..models.success_model import SuccessModel
from ..server.server import Server


class UpdateTriggers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UpdateTriggersWithRawResponse(client, server, auth)

    def update_all_available_triggers(
        self,
        *,
        body: RequestTrigger | RequestTriggerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SuccessModel:
        """Updates the promotional triggers for pseudo-MDN.

        Args:
            body: Update the triggers
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status of Request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_all_available_triggers(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UpdateTriggersWithRawResponse:
        return self._with_raw_response


class AsyncUpdateTriggers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUpdateTriggersWithRawResponse(client, server, auth)

    async def update_all_available_triggers(
        self,
        *,
        body: RequestTrigger | RequestTriggerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SuccessModel:
        """Updates the promotional triggers for pseudo-MDN.

        Args:
            body: Update the triggers
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status of Request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_all_available_triggers(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUpdateTriggersWithRawResponse:
        return self._with_raw_response


class UpdateTriggersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_all_available_triggers(
        self,
        *,
        body: RequestTrigger | RequestTriggerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SuccessModel, RawError]:
        """Updates the promotional triggers for pseudo-MDN.

        Args:
            body: Update the triggers
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RequestTrigger | RequestTriggerDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SuccessModel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUpdateTriggersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def update_all_available_triggers(
        self,
        *,
        body: RequestTrigger | RequestTriggerDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SuccessModel, RawError]:
        """Updates the promotional triggers for pseudo-MDN.

        Args:
            body: Update the triggers
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RequestTrigger | RequestTriggerDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SuccessModel],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
