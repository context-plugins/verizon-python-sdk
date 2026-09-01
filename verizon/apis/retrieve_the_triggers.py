from __future__ import annotations

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
from ..models.trigger_value_response import TriggerValueResponse
from ..models.trigger_value_response2 import TriggerValueResponse2
from ..server.server import Server


class RetrieveTheTriggers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RetrieveTheTriggersWithRawResponse(client, server, auth)

    def get_all_available_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse:
        """Retrieves all of the available triggers for pseudo-MDN.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status of Request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_all_available_triggers(request_options=request_options).unwrap()

    def get_all_triggers_by_account_name(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse:
        """Retrieve the triggers associated with an account name.

        Args:
            account_name: The account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status of Request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_all_triggers_by_account_name(
            account_name, request_options=request_options
        ).unwrap()

    def get_all_triggers_by_trigger_category(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse2:
        """Retrieves all of the triggers for the specified account associated with the PromoAlert category

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_all_triggers_by_trigger_category(request_options=request_options).unwrap()

    def get_triggers_by_id(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse2:
        """Retrives a specific trigger by its ID.

        Args:
            trigger_id: The ID of a specific trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_triggers_by_id(trigger_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> RetrieveTheTriggersWithRawResponse:
        return self._with_raw_response


class AsyncRetrieveTheTriggers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRetrieveTheTriggersWithRawResponse(client, server, auth)

    async def get_all_available_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse:
        """Retrieves all of the available triggers for pseudo-MDN.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status of Request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_all_available_triggers(request_options=request_options)).unwrap()

    async def get_all_triggers_by_account_name(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse:
        """Retrieve the triggers associated with an account name.

        Args:
            account_name: The account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Status of Request

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_all_triggers_by_account_name(
                account_name, request_options=request_options
            )
        ).unwrap()

    async def get_all_triggers_by_trigger_category(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse2:
        """Retrieves all of the triggers for the specified account associated with the PromoAlert category

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_all_triggers_by_trigger_category(request_options=request_options)
        ).unwrap()

    async def get_triggers_by_id(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TriggerValueResponse2:
        """Retrives a specific trigger by its ID.

        Args:
            trigger_id: The ID of a specific trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_triggers_by_id(trigger_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncRetrieveTheTriggersWithRawResponse:
        return self._with_raw_response


class RetrieveTheTriggersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_all_available_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse, RawError]:
        """Retrieves all of the available triggers for pseudo-MDN.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_all_triggers_by_account_name(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse, RawError]:
        """Retrieve the triggers associated with an account name.

        Args:
            account_name: The account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/accounts/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_all_triggers_by_trigger_category(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse2, RawError]:
        """Retrieves all of the triggers for the specified account associated with the PromoAlert category

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/categories/PromoAlerts"),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_triggers_by_id(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse2, RawError]:
        """Retrives a specific trigger by its ID.

        Args:
            trigger_id: The ID of a specific trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRetrieveTheTriggersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_all_available_triggers(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse, RawError]:
        """Retrieves all of the available triggers for pseudo-MDN.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers"),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_all_triggers_by_account_name(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse, RawError]:
        """Retrieve the triggers associated with an account name.

        Args:
            account_name: The account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/accounts/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_all_triggers_by_trigger_category(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse2, RawError]:
        """Retrieves all of the triggers for the specified account associated with the PromoAlert category

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/categories/PromoAlerts"),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_triggers_by_id(
        self, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TriggerValueResponse2, RawError]:
        """Retrives a specific trigger by its ID.

        Args:
            trigger_id: The ID of a specific trigger
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[TriggerValueResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
