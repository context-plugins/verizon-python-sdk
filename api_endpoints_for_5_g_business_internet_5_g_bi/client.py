from __future__ import annotations

from functools import cached_property
from types import TracebackType
from uuid import UUID, uuid4

from typing_extensions import Self

from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseApiEndpointsFor5GBusinessInternet5GBiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AnySchemes,
    ApiKeyHeaderScheme,
    ApiResult,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    HttpxClient,
    OAuth2Scheme,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    TokenSource,
    client_secret_basic,
    json_body,
    json_decoder,
    no_auth,
    param,
    raw_error_response,
)
from .models.gbi_request_response5 import GbiRequestResponse5
from .models.gbiactivate_request5 import GbiactivateRequest5, GbiactivateRequest5Dict
from .models.gbichange_request5 import GbichangeRequest5, GbichangeRequest5Dict
from .models.gbidevice_detailsresponse5 import GbideviceDetailsresponse5
from .models.gbidevice_id5 import GbideviceId5, GbideviceId5Dict
from .server.environment import Environment
from .server.server import Server
from .server.server_config import ServerConfigOrDict


class ApiEndpointsFor5GBusinessInternet5GBiClient(BaseApiEndpointsFor5GBusinessInternet5GBiClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        thingspace_oauth: ClientCredentialsOrDict | None = None,
        thingspace_oauth_token_source: TokenSource[ClientCredentials] | None = None,
        vz_m2m_session_token: str | None = None,
    ) -> None:
        super().__init__(environment=environment, timeout=timeout, server_config=server_config)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "ApiEndpointsFor5GBusinessInternet5GBiClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            thingspace_oauth=(
                OAuth2Scheme(
                    credentials=ClientCredentials.coerce(thingspace_oauth),
                    source=(
                        thingspace_oauth_token_source
                        if thingspace_oauth_token_source is not None
                        else ClientCredentialsTokenSource(
                            client=self._raw_client,
                            token_url=self._server.o_auth_server("/oauth2/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if thingspace_oauth is not None
                else no_auth
            ),
            vz_m2m_session_token=(
                ApiKeyHeaderScheme("VZ-M2M-Token", vz_m2m_session_token)
                if vz_m2m_session_token is not None
                else no_auth
            ),
        )

    @cached_property
    def with_raw_response(self) -> ApiWithRawResponse:
        return ApiWithRawResponse(self._raw_client, self._server, self._auth)

    def business_internet_serviceplanchange(
        self, body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GbiRequestResponse5:
        """Change a device's service plan to use 5G BI.

        Args:
            body: This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service
                plan can change for an active device up to four times per month but will require address validation for
                each change. The service plan cannot be changed for a device while its service is suspended.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A request ID is returned as a successful response. Use a callback to see the details associated with the
            request ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.business_internet_serviceplanchange(
            body, request_options=request_options
        ).unwrap()

    def business_internetactivate_using_post(
        self,
        body: GbiactivateRequest5 | GbiactivateRequest5Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GbiRequestResponse5:
        """Uses the device's ICCID and IMEI to activate service.

        Args:
            body: Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is
                required for activating as Public Static. Leave <code>publicIpRestriction</code> undefined to activate
                as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile
                Private Network (MPN).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A request ID is returned as a successful response. Use a callback to see the details associated with the
            request ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.business_internetactivate_using_post(
            body, request_options=request_options
        ).unwrap()

    def business_internetlist_device_information(
        self, body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GbideviceDetailsresponse5:
        """Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's
        properties.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The device's details will be returned from a successful request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.business_internetlist_device_information(
            body, request_options=request_options
        ).unwrap()

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class ApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def business_internet_serviceplanchange(
        self, body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GbiRequestResponse5, RawError]:
        """Change a device's service plan to use 5G BI.

        Args:
            body: This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service
                plan can change for an active device up to four times per month but will require address validation for
                each change. The service plan cannot be changed for a device while its service is suspended.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.o_auth_server("/actions/plan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbichangeRequest5 | GbichangeRequest5Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2m_session_token),
            decoder=json_decoder[GbiRequestResponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def business_internetactivate_using_post(
        self,
        body: GbiactivateRequest5 | GbiactivateRequest5Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GbiRequestResponse5, RawError]:
        """Uses the device's ICCID and IMEI to activate service.

        Args:
            body: Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is
                required for activating as Public Static. Leave <code>publicIpRestriction</code> undefined to activate
                as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile
                Private Network (MPN).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.o_auth_server("/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbiactivateRequest5 | GbiactivateRequest5Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2m_session_token),
            decoder=json_decoder[GbiRequestResponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def business_internetlist_device_information(
        self, body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GbideviceDetailsresponse5, RawError]:
        """Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's
        properties.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.o_auth_server("/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbideviceId5 | GbideviceId5Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2m_session_token),
            decoder=json_decoder[GbideviceDetailsresponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


Client = ApiEndpointsFor5GBusinessInternet5GBiClient
