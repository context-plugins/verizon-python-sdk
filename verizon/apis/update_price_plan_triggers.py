from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
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
from ..models.trigger_response import TriggerResponse
from ..models.unions.v2_triggers_request1 import V2TriggersRequest1, V2TriggersRequest1Dict
from ..server.server import Server


class UpdatePricePlanTriggers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UpdatePricePlanTriggersWithRawResponse(client, server, auth)

    def update_trigger_rules(
        self, body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerResponse:
        """Updates a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Update a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_trigger_rules(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UpdatePricePlanTriggersWithRawResponse:
        return self._with_raw_response


class AsyncUpdatePricePlanTriggers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUpdatePricePlanTriggersWithRawResponse(client, server, auth)

    async def update_trigger_rules(
        self, body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerResponse:
        """Updates a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Update a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_trigger_rules(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncUpdatePricePlanTriggersWithRawResponse:
        return self._with_raw_response


class UpdatePricePlanTriggersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def update_trigger_rules(
        self, body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerResponse, RawError]:
        """Updates a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Update a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2TriggersRequest1 | V2TriggersRequest1Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth1, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUpdatePricePlanTriggersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def update_trigger_rules(
        self, body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerResponse, RawError]:
        """Updates a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Update a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2TriggersRequest1 | V2TriggersRequest1Dict](body),
            auth_scheme=AsyncAnySchemes(self._auth.thingspace_oauth1, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
