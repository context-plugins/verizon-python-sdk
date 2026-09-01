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
from ..models.change_pwndevice_ipaddress_request import (
    ChangePwndeviceIpaddressRequest,
    ChangePwndeviceIpaddressRequestDict,
)
from ..models.change_pwndevice_ipaddress_response import ChangePwndeviceIpaddressResponse
from ..models.change_pwndevice_profile_request import ChangePwndeviceProfileRequest, ChangePwndeviceProfileRequestDict
from ..models.change_pwndevice_profile_response import ChangePwndeviceProfileResponse
from ..models.change_pwndevice_state_activate_request import (
    ChangePwndeviceStateActivateRequest,
    ChangePwndeviceStateActivateRequestDict,
)
from ..models.change_pwndevice_state_deactivate_request import (
    ChangePwndeviceStateDeactivateRequest,
    ChangePwndeviceStateDeactivateRequestDict,
)
from ..models.change_pwndevice_state_response import ChangePwndeviceStateResponse
from ..models.get_pwnperformance_consent_response import GetPwnperformanceConsentResponse
from ..models.kpiinfo_list import KpiinfoList
from ..models.pwnprofile_list import PwnprofileList
from ..server.server import Server


class Pwn:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PwnWithRawResponse(client, server, auth)

    def change_pwn_device_i_paddress(
        self,
        body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceIpaddressResponse:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.change_pwn_device_i_paddress(body, request_options=request_options).unwrap()

    def change_pwn_device_profile(
        self,
        body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceProfileResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.change_pwn_device_profile(body, request_options=request_options).unwrap()

    def change_pwn_device_state_activate(
        self,
        body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceStateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.change_pwn_device_state_activate(body, request_options=request_options).unwrap()

    def change_pwn_device_state_deactivate(
        self,
        body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceStateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.change_pwn_device_state_deactivate(
            body, request_options=request_options
        ).unwrap()

    def get_pwn_performance_consent(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPwnperformanceConsentResponse:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            consent received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_pwn_performance_consent(aname, request_options=request_options).unwrap()

    def get_profile_list(self, aname: str, *, request_options: RequestOptionsOrDict | None = None) -> PwnprofileList:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            PWN profiles list received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_profile_list(aname, request_options=request_options).unwrap()

    def kpi_list(self, aname: str, *, request_options: RequestOptionsOrDict | None = None) -> KpiinfoList:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Kpi list received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.kpi_list(aname, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PwnWithRawResponse:
        return self._with_raw_response


class AsyncPwn:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPwnWithRawResponse(client, server, auth)

    async def change_pwn_device_i_paddress(
        self,
        body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceIpaddressResponse:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.change_pwn_device_i_paddress(body, request_options=request_options)
        ).unwrap()

    async def change_pwn_device_profile(
        self,
        body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceProfileResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.change_pwn_device_profile(body, request_options=request_options)).unwrap()

    async def change_pwn_device_state_activate(
        self,
        body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceStateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.change_pwn_device_state_activate(body, request_options=request_options)
        ).unwrap()

    async def change_pwn_device_state_deactivate(
        self,
        body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangePwndeviceStateResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.change_pwn_device_state_deactivate(body, request_options=request_options)
        ).unwrap()

    async def get_pwn_performance_consent(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPwnperformanceConsentResponse:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            consent received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_pwn_performance_consent(aname, request_options=request_options)
        ).unwrap()

    async def get_profile_list(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PwnprofileList:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            PWN profiles list received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_profile_list(aname, request_options=request_options)).unwrap()

    async def kpi_list(self, aname: str, *, request_options: RequestOptionsOrDict | None = None) -> KpiinfoList:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Kpi list received on a successful response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.kpi_list(aname, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncPwnWithRawResponse:
        return self._with_raw_response


class PwnWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def change_pwn_device_i_paddress(
        self,
        body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceIpaddressResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/ipaddress"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceIpaddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def change_pwn_device_profile(
        self,
        body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceProfileResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/profile"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def change_pwn_device_state_activate(
        self,
        body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceStateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/state/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceStateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def change_pwn_device_state_deactivate(
        self,
        body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceStateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/state/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceStateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_pwn_performance_consent(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPwnperformanceConsentResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/performance/consent/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetPwnperformanceConsentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_profile_list(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PwnprofileList, RawError]:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/profiles/list/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[PwnprofileList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def kpi_list(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[KpiinfoList, RawError]:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/kpi/list/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[KpiinfoList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPwnWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def change_pwn_device_i_paddress(
        self,
        body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceIpaddressResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/ipaddress"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceIpaddressResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def change_pwn_device_profile(
        self,
        body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceProfileResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/profile"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def change_pwn_device_state_activate(
        self,
        body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceStateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/state/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceStateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def change_pwn_device_state_deactivate(
        self,
        body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangePwndeviceStateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/actions/state/deactivate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ChangePwndeviceStateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_pwn_performance_consent(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPwnperformanceConsentResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/performance/consent/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetPwnperformanceConsentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_profile_list(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PwnprofileList, RawError]:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/profiles/list/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[PwnprofileList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def kpi_list(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[KpiinfoList, RawError]:
        """Send a ``GET`` request.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/pwn/kpi/list/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[KpiinfoList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
