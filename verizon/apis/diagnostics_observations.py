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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.diagnostics_observation_result import DiagnosticsObservationResult
from ..server.server import Server


class DiagnosticsObservations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DiagnosticsObservationsWithRawResponse(client, server, auth)

    def start_diagnostics_observation(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsObservationResult:
        """This endpoint allows the user to start or change observe diagnostics.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics observation result.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.start_diagnostics_observation(request_options=request_options).unwrap()

    def stop_diagnostics_observation(
        self, transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsObservationResult:
        """This endpoint allows the user to stop or reset observe diagnostics.

        Args:
            transaction_id: The ID value associated with the transaction.
            account_name: The numeric account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics observation result.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stop_diagnostics_observation(
            transaction_id, account_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DiagnosticsObservationsWithRawResponse:
        return self._with_raw_response


class AsyncDiagnosticsObservations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDiagnosticsObservationsWithRawResponse(client, server, auth)

    async def start_diagnostics_observation(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsObservationResult:
        """This endpoint allows the user to start or change observe diagnostics.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics observation result.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.start_diagnostics_observation(request_options=request_options)).unwrap()

    async def stop_diagnostics_observation(
        self, transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DiagnosticsObservationResult:
        """This endpoint allows the user to stop or reset observe diagnostics.

        Args:
            transaction_id: The ID value associated with the transaction.
            account_name: The numeric account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Diagnostics observation result.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stop_diagnostics_observation(
                transaction_id, account_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiagnosticsObservationsWithRawResponse:
        return self._with_raw_response


class DiagnosticsObservationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def start_diagnostics_observation(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsObservationResult, RawError]:
        """This endpoint allows the user to start or change observe diagnostics.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/devices/attributes/actions/observe"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsObservationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stop_diagnostics_observation(
        self, transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsObservationResult, RawError]:
        """This endpoint allows the user to stop or reset observe diagnostics.

        Args:
            transaction_id: The ID value associated with the transaction.
            account_name: The numeric account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_diagnostics("/devices/attributes/actions/observe"),
            query_params=[param[str]("transactionId", transaction_id), param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsObservationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDiagnosticsObservationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def start_diagnostics_observation(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsObservationResult, RawError]:
        """This endpoint allows the user to start or change observe diagnostics.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_diagnostics("/devices/attributes/actions/observe"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsObservationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stop_diagnostics_observation(
        self, transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DiagnosticsObservationResult, RawError]:
        """This endpoint allows the user to stop or reset observe diagnostics.

        Args:
            transaction_id: The ID value associated with the transaction.
            account_name: The numeric account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_diagnostics("/devices/attributes/actions/observe"),
            query_params=[param[str]("transactionId", transaction_id), param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DiagnosticsObservationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
