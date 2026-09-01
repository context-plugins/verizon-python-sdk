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
from ..models.unions.v2_triggers_request import V2TriggersRequest, V2TriggersRequestDict
from ..server.server import Server


class CreatePricePlanTriggers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CreatePricePlanTriggersWithRawResponse(client, server, auth)

    def create_trigger_rules(
        self, body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerResponse:
        """Create a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Create a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_trigger_rules(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CreatePricePlanTriggersWithRawResponse:
        return self._with_raw_response


class AsyncCreatePricePlanTriggers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCreatePricePlanTriggersWithRawResponse(client, server, auth)

    async def create_trigger_rules(
        self, body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerResponse:
        """Create a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Create a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_trigger_rules(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCreatePricePlanTriggersWithRawResponse:
        return self._with_raw_response


class CreatePricePlanTriggersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_trigger_rules(
        self, body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerResponse, RawError]:
        """Create a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Create a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2TriggersRequest | V2TriggersRequestDict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth1, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCreatePricePlanTriggersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_trigger_rules(
        self, body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerResponse, RawError]:
        """Create a usage trigger at the account level, device level or a price plan trigger for all devices on the
        account

        Args:
            body: Create a trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v2/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V2TriggersRequest | V2TriggersRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.thingspace_oauth1, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
