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
from ..errors.drop_credentials_error import DropCredentialsErrorBody, drop_credentials_error_mapper
from ..errors.generate_credentials_error import GenerateCredentialsErrorBody, generate_credentials_error_mapper
from ..errors.reset_credentials_error import ResetCredentialsErrorBody, reset_credentials_error_mapper
from ..errors.retrieve_credentials_error import RetrieveCredentialsErrorBody, retrieve_credentials_error_mapper
from ..models.credentials_request import CredentialsRequest, CredentialsRequestDict
from ..models.drop_response import DropResponse
from ..models.generate_response import GenerateResponse
from ..models.retrieve_response import RetrieveResponse
from ..server.server import Server


class DeviceCredentialManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceCredentialManagementWithRawResponse(client, server, auth)

    def drop_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DropResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Credentials dropped successfully

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.drop_credentials(body, request_options=request_options).unwrap()

    def generate_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Credentials generated successfully

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.generate_credentials(body, request_options=request_options).unwrap()

    def reset_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Credentials reset successfully

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.reset_credentials(body, request_options=request_options).unwrap()

    def retrieve_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Bad Request / Verification Failure Unauthorized ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.retrieve_credentials(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceCredentialManagementWithRawResponse:
        return self._with_raw_response


class AsyncDeviceCredentialManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceCredentialManagementWithRawResponse(client, server, auth)

    async def drop_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DropResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Credentials dropped successfully

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.drop_credentials(body, request_options=request_options)).unwrap()

    async def generate_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Credentials generated successfully

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.generate_credentials(body, request_options=request_options)).unwrap()

    async def reset_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Credentials reset successfully

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.reset_credentials(body, request_options=request_options)).unwrap()

    async def retrieve_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Bad Request / Verification Failure Unauthorized ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.retrieve_credentials(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceCredentialManagementWithRawResponse:
        return self._with_raw_response


class DeviceCredentialManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def drop_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DropResponse, DropCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/drop"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DropResponse],
            error_mapper=drop_credentials_error_mapper,
            request_options=request_options,
        )

    def generate_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateResponse, GenerateCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/generate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GenerateResponse],
            error_mapper=generate_credentials_error_mapper,
            request_options=request_options,
        )

    def reset_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateResponse, ResetCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/reset"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GenerateResponse],
            error_mapper=reset_credentials_error_mapper,
            request_options=request_options,
        )

    def retrieve_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveResponse, RetrieveCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RetrieveResponse],
            error_mapper=retrieve_credentials_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceCredentialManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def drop_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DropResponse, DropCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/drop"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DropResponse],
            error_mapper=drop_credentials_error_mapper,
            request_options=request_options,
        )

    async def generate_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateResponse, GenerateCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/generate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GenerateResponse],
            error_mapper=generate_credentials_error_mapper,
            request_options=request_options,
        )

    async def reset_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateResponse, ResetCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/reset"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GenerateResponse],
            error_mapper=reset_credentials_error_mapper,
            request_options=request_options,
        )

    async def retrieve_credentials(
        self, body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveResponse, RetrieveCredentialsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/credentials/retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CredentialsRequest | CredentialsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RetrieveResponse],
            error_mapper=retrieve_credentials_error_mapper,
            request_options=request_options,
        )
