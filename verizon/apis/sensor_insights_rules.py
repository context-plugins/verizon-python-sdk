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
from ..errors.sensor_insights_list_rules_request_error import (
    SensorInsightsListRulesRequestErrorBody,
    sensor_insights_list_rules_request_error_mapper,
)
from ..errors.sensor_insights_overwrite_rule_request_error import (
    SensorInsightsOverwriteRuleRequestErrorBody,
    sensor_insights_overwrite_rule_request_error_mapper,
)
from ..models.dto_list_rules_request import DtoListRulesRequest, DtoListRulesRequestDict
from ..models.dto_overwrite_rule_request import DtoOverwriteRuleRequest, DtoOverwriteRuleRequestDict
from ..models.resource_rule import ResourceRule
from ..server.server import Server


class SensorInsightsRules:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsRulesWithRawResponse(client, server, auth)

    def sensor_insights_list_rules_request(
        self,
        body: DtoListRulesRequest | DtoListRulesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ResourceRule]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_list_rules_request(
            body, request_options=request_options
        ).unwrap()

    def sensor_insights_overwrite_rule_request(
        self,
        body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceRule:
        """Send a ``POST`` request.

        Args:
            body: Overwrite a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_overwrite_rule_request(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsRulesWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsRules:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsRulesWithRawResponse(client, server, auth)

    async def sensor_insights_list_rules_request(
        self,
        body: DtoListRulesRequest | DtoListRulesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ResourceRule]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_list_rules_request(body, request_options=request_options)
        ).unwrap()

    async def sensor_insights_overwrite_rule_request(
        self,
        body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResourceRule:
        """Send a ``POST`` request.

        Args:
            body: Overwrite a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Found Not Acceptable Unsupported media type Too many
                requests Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403
                | ManagementError404 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_overwrite_rule_request(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsRulesWithRawResponse:
        return self._with_raw_response


class SensorInsightsRulesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_list_rules_request(
        self,
        body: DtoListRulesRequest | DtoListRulesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ResourceRule], SensorInsightsListRulesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/rules/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListRulesRequest | DtoListRulesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceRule]],
            error_mapper=sensor_insights_list_rules_request_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_overwrite_rule_request(
        self,
        body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceRule, SensorInsightsOverwriteRuleRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Overwrite a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/rules"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceRule],
            error_mapper=sensor_insights_overwrite_rule_request_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsRulesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_list_rules_request(
        self,
        body: DtoListRulesRequest | DtoListRulesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ResourceRule], SensorInsightsListRulesRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Retrieve a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/rules/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoListRulesRequest | DtoListRulesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ResourceRule]],
            error_mapper=sensor_insights_list_rules_request_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_overwrite_rule_request(
        self,
        body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResourceRule, SensorInsightsOverwriteRuleRequestErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Overwrite a rule
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/rules"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResourceRule],
            error_mapper=sensor_insights_overwrite_rule_request_error_mapper,
            request_options=request_options,
        )
