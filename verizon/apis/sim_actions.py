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
from ..errors.newactivatecode_error import NewactivatecodeErrorBody, newactivatecode_error_mapper
from ..errors.setactivate_using_post_error import SetactivateUsingPostErrorBody, setactivate_using_post_error_mapper
from ..errors.setdeactivate_using_post_error import (
    SetdeactivateUsingPostErrorBody,
    setdeactivate_using_post_error_mapper,
)
from ..models.e_simprofile_request import ESimprofileRequest, ESimprofileRequestDict
from ..models.e_simprofile_request2 import ESimprofileRequest2, ESimprofileRequest2Dict
from ..models.e_simrequest_response import ESimrequestResponse
from ..models.profile_request2 import ProfileRequest2, ProfileRequest2Dict
from ..server.server import Server


class SimActions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SimActionsWithRawResponse(client, server, auth)

    def newactivatecode(
        self,
        body: ESimprofileRequest2 | ESimprofileRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ESimrequestResponse:
        """System assign a new activation code to reactivate a deactivated device. **Note:** the previously assigned
        ICCID must be used to request a new activation code.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return self._with_raw_response.newactivatecode(body, request_options=request_options).unwrap()

    def setactivate_using_post(
        self, body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ESimrequestResponse:
        """Uses the profile to activate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return self._with_raw_response.setactivate_using_post(body, request_options=request_options).unwrap()

    def setdeactivate_using_post(
        self, body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ESimrequestResponse:
        """Uses the profile to deactivate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return self._with_raw_response.setdeactivate_using_post(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SimActionsWithRawResponse:
        return self._with_raw_response


class AsyncSimActions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSimActionsWithRawResponse(client, server, auth)

    async def newactivatecode(
        self,
        body: ESimprofileRequest2 | ESimprofileRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ESimrequestResponse:
        """System assign a new activation code to reactivate a deactivated device. **Note:** the previously assigned
        ICCID must be used to request a new activation code.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return (await self._with_raw_response.newactivatecode(body, request_options=request_options)).unwrap()

    async def setactivate_using_post(
        self, body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ESimrequestResponse:
        """Uses the profile to activate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return (await self._with_raw_response.setactivate_using_post(body, request_options=request_options)).unwrap()

    async def setdeactivate_using_post(
        self, body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ESimrequestResponse:
        """Uses the profile to deactivate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return (await self._with_raw_response.setdeactivate_using_post(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSimActionsWithRawResponse:
        return self._with_raw_response


class SimActionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def newactivatecode(
        self,
        body: ESimprofileRequest2 | ESimprofileRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ESimrequestResponse, NewactivatecodeErrorBody]:
        """System assign a new activation code to reactivate a deactivated device. **Note:** the previously assigned
        ICCID must be used to request a new activation code.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/devices/profile/actions/renew_activation_code"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ESimprofileRequest2 | ESimprofileRequest2Dict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=newactivatecode_error_mapper,
            request_options=request_options,
        )

    def setactivate_using_post(
        self, body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ESimrequestResponse, SetactivateUsingPostErrorBody]:
        """Uses the profile to activate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ESimprofileRequest | ESimprofileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=setactivate_using_post_error_mapper,
            request_options=request_options,
        )

    def setdeactivate_using_post(
        self, body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ESimrequestResponse, SetdeactivateUsingPostErrorBody]:
        """Uses the profile to deactivate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileRequest2 | ProfileRequest2Dict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=setdeactivate_using_post_error_mapper,
            request_options=request_options,
        )


class AsyncSimActionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def newactivatecode(
        self,
        body: ESimprofileRequest2 | ESimprofileRequest2Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ESimrequestResponse, NewactivatecodeErrorBody]:
        """System assign a new activation code to reactivate a deactivated device. **Note:** the previously assigned
        ICCID must be used to request a new activation code.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/devices/profile/actions/renew_activation_code"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ESimprofileRequest2 | ESimprofileRequest2Dict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=newactivatecode_error_mapper,
            request_options=request_options,
        )

    async def setactivate_using_post(
        self, body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ESimrequestResponse, SetactivateUsingPostErrorBody]:
        """Uses the profile to activate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ESimprofileRequest | ESimprofileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=setactivate_using_post_error_mapper,
            request_options=request_options,
        )

    async def setdeactivate_using_post(
        self, body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ESimrequestResponse, SetdeactivateUsingPostErrorBody]:
        """Uses the profile to deactivate the SIM.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/profile/actions/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileRequest2 | ProfileRequest2Dict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=setdeactivate_using_post_error_mapper,
            request_options=request_options,
        )
