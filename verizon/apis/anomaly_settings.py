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
from ..models.anomaly_detection_request import AnomalyDetectionRequest, AnomalyDetectionRequestDict
from ..models.anomaly_detection_settings import AnomalyDetectionSettings
from ..models.intelligence_success_result import IntelligenceSuccessResult
from ..server.server import Server


class AnomalySettings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AnomalySettingsWithRawResponse(client, server, auth)

    def activate_anomaly_detection(
        self,
        body: AnomalyDetectionRequest | AnomalyDetectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IntelligenceSuccessResult:
        """Uses the subscribed account ID to activate anomaly detection and set threshold values.

        Args:
            body: Request to activate anomaly detection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.activate_anomaly_detection(body, request_options=request_options).unwrap()

    def list_anomaly_detection_settings(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnomalyDetectionSettings:
        """Retrieves the current anomaly detection settings for an account.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Retrieve the settings for anomaly detection.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_anomaly_detection_settings(
            account_name, request_options=request_options
        ).unwrap()

    def reset_anomaly_detection_parameters(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IntelligenceSuccessResult:
        """Resets the thresholds to zero.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.reset_anomaly_detection_parameters(
            account_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AnomalySettingsWithRawResponse:
        return self._with_raw_response


class AsyncAnomalySettings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAnomalySettingsWithRawResponse(client, server, auth)

    async def activate_anomaly_detection(
        self,
        body: AnomalyDetectionRequest | AnomalyDetectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IntelligenceSuccessResult:
        """Uses the subscribed account ID to activate anomaly detection and set threshold values.

        Args:
            body: Request to activate anomaly detection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.activate_anomaly_detection(body, request_options=request_options)
        ).unwrap()

    async def list_anomaly_detection_settings(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnomalyDetectionSettings:
        """Retrieves the current anomaly detection settings for an account.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Retrieve the settings for anomaly detection.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_anomaly_detection_settings(account_name, request_options=request_options)
        ).unwrap()

    async def reset_anomaly_detection_parameters(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IntelligenceSuccessResult:
        """Resets the thresholds to zero.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.reset_anomaly_detection_parameters(
                account_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAnomalySettingsWithRawResponse:
        return self._with_raw_response


class AnomalySettingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_anomaly_detection(
        self,
        body: AnomalyDetectionRequest | AnomalyDetectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IntelligenceSuccessResult, RawError]:
        """Uses the subscribed account ID to activate anomaly detection and set threshold values.

        Args:
            body: Request to activate anomaly detection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/anomaly/settings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AnomalyDetectionRequest | AnomalyDetectionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[IntelligenceSuccessResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_anomaly_detection_settings(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnomalyDetectionSettings, RawError]:
        """Retrieves the current anomaly detection settings for an account.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/{accountName}/anomaly/settings"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def reset_anomaly_detection_parameters(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IntelligenceSuccessResult, RawError]:
        """Resets the thresholds to zero.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/intelligence/{accountName}/anomaly/settings/reset"
            ),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[IntelligenceSuccessResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAnomalySettingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_anomaly_detection(
        self,
        body: AnomalyDetectionRequest | AnomalyDetectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IntelligenceSuccessResult, RawError]:
        """Uses the subscribed account ID to activate anomaly detection and set threshold values.

        Args:
            body: Request to activate anomaly detection.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/anomaly/settings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AnomalyDetectionRequest | AnomalyDetectionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[IntelligenceSuccessResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_anomaly_detection_settings(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnomalyDetectionSettings, RawError]:
        """Retrieves the current anomaly detection settings for an account.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/{accountName}/anomaly/settings"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AnomalyDetectionSettings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def reset_anomaly_detection_parameters(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IntelligenceSuccessResult, RawError]:
        """Resets the thresholds to zero.

        Args:
            account_name: The name of the subscribed account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/intelligence/{accountName}/anomaly/settings/reset"
            ),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[IntelligenceSuccessResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
