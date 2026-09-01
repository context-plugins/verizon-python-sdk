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
from ..errors.exclude_devices_error import ExcludeDevicesErrorBody, exclude_devices_error_mapper
from ..errors.list_excluded_devices_error import ListExcludedDevicesErrorBody, list_excluded_devices_error_mapper
from ..errors.remove_devices_from_exclusion_list_error import (
    RemoveDevicesFromExclusionListErrorBody,
    remove_devices_from_exclusion_list_error_mapper,
)
from ..models.account_consent_create import AccountConsentCreate, AccountConsentCreateDict
from ..models.account_consent_update import AccountConsentUpdate, AccountConsentUpdateDict
from ..models.consent_transaction_id import ConsentTransactionId
from ..models.device_location_success_result import DeviceLocationSuccessResult
from ..models.devices_consent_result import DevicesConsentResult
from ..models.get_account_device_consent import GetAccountDeviceConsent
from ..server.server import Server


class Exclusions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ExclusionsWithRawResponse(client, server, auth)

    def devices_location_get_consent_async(
        self, account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetAccountDeviceConsent:
        """Get the consent settings for the entire account or device list in an account.

        Args:
            account_name: The numeric name of the account.
            device_id: The IMEI of the device being queried
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.devices_location_get_consent_async(
            account_name, device_id=device_id, request_options=request_options
        ).unwrap()

    def devices_location_give_consent_async(
        self,
        *,
        body: AccountConsentCreate | AccountConsentCreateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConsentTransactionId:
        """Create a consent record to use location services as an asynchronous request.

        Args:
            body: Account details to create a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.devices_location_give_consent_async(
            body=body, request_options=request_options
        ).unwrap()

    def devices_location_update_consent(
        self,
        *,
        body: AccountConsentUpdate | AccountConsentUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConsentTransactionId:
        """Update the location services consent record for an entire account.

        Args:
            body: Account details to update a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.devices_location_update_consent(
            body=body, request_options=request_options
        ).unwrap()

    def exclude_devices(self, *, request_options: RequestOptionsOrDict | None = None) -> DeviceLocationSuccessResult:
        """This consents endpoint sets a new exclusion list.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.exclude_devices(request_options=request_options).unwrap()

    def list_excluded_devices(
        self, account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DevicesConsentResult:
        """This consents endpoint retrieves a list of excluded devices in an account.

        Args:
            account_name: Account identifier in "##########-#####".
            start_index: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Excluded devices result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.list_excluded_devices(
            account_name, start_index, request_options=request_options
        ).unwrap()

    def remove_devices_from_exclusion_list(
        self, account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSuccessResult:
        """Removes devices from the exclusion list so that they can be located with Device Location Services requests.

        Args:
            account_name: The numeric name of the account.
            device_list: A list of the device IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Devices successfully removed from list.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.remove_devices_from_exclusion_list(
            account_name, device_list, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ExclusionsWithRawResponse:
        return self._with_raw_response


class AsyncExclusions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncExclusionsWithRawResponse(client, server, auth)

    async def devices_location_get_consent_async(
        self, account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetAccountDeviceConsent:
        """Get the consent settings for the entire account or device list in an account.

        Args:
            account_name: The numeric name of the account.
            device_id: The IMEI of the device being queried
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.devices_location_get_consent_async(
                account_name, device_id=device_id, request_options=request_options
            )
        ).unwrap()

    async def devices_location_give_consent_async(
        self,
        *,
        body: AccountConsentCreate | AccountConsentCreateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConsentTransactionId:
        """Create a consent record to use location services as an asynchronous request.

        Args:
            body: Account details to create a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.devices_location_give_consent_async(
                body=body, request_options=request_options
            )
        ).unwrap()

    async def devices_location_update_consent(
        self,
        *,
        body: AccountConsentUpdate | AccountConsentUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConsentTransactionId:
        """Update the location services consent record for an entire account.

        Args:
            body: Account details to update a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of JSON objects, each containing the position data or an error for a device in the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.devices_location_update_consent(body=body, request_options=request_options)
        ).unwrap()

    async def exclude_devices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSuccessResult:
        """This consents endpoint sets a new exclusion list.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return (await self._with_raw_response.exclude_devices(request_options=request_options)).unwrap()

    async def list_excluded_devices(
        self, account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DevicesConsentResult:
        """This consents endpoint retrieves a list of excluded devices in an account.

        Args:
            account_name: Account identifier in "##########-#####".
            start_index: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Excluded devices result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.list_excluded_devices(
                account_name, start_index, request_options=request_options
            )
        ).unwrap()

    async def remove_devices_from_exclusion_list(
        self, account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSuccessResult:
        """Removes devices from the exclusion list so that they can be located with Device Location Services requests.

        Args:
            account_name: The numeric name of the account.
            device_list: A list of the device IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Devices successfully removed from list.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.remove_devices_from_exclusion_list(
                account_name, device_list, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncExclusionsWithRawResponse:
        return self._with_raw_response


class ExclusionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def devices_location_get_consent_async(
        self, account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAccountDeviceConsent, RawError]:
        """Get the consent settings for the entire account or device list in an account.

        Args:
            account_name: The numeric name of the account.
            device_id: The IMEI of the device being queried
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/devicelocations/action/consents"),
            query_params=[param[str]("accountName", account_name), param[str | None]("deviceId", device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetAccountDeviceConsent],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def devices_location_give_consent_async(
        self,
        *,
        body: AccountConsentCreate | AccountConsentCreateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConsentTransactionId, RawError]:
        """Create a consent record to use location services as an asynchronous request.

        Args:
            body: Account details to create a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/devicelocations/action/consents"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountConsentCreate | AccountConsentCreateDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConsentTransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def devices_location_update_consent(
        self,
        *,
        body: AccountConsentUpdate | AccountConsentUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConsentTransactionId, RawError]:
        """Update the location services consent record for an entire account.

        Args:
            body: Account details to update a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.device_location("/devicelocations/action/consents"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountConsentUpdate | AccountConsentUpdateDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConsentTransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def exclude_devices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSuccessResult, ExcludeDevicesErrorBody]:
        """This consents endpoint sets a new exclusion list.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/consents"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=exclude_devices_error_mapper,
            request_options=request_options,
        )

    def list_excluded_devices(
        self, account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DevicesConsentResult, ListExcludedDevicesErrorBody]:
        """This consents endpoint retrieves a list of excluded devices in an account.

        Args:
            account_name: Account identifier in "##########-#####".
            start_index: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/consents/{accountName}/index/{startIndex}"),
            path_params=[param[str]("accountName", account_name), param[str]("startIndex", start_index)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DevicesConsentResult],
            error_mapper=list_excluded_devices_error_mapper,
            request_options=request_options,
        )

    def remove_devices_from_exclusion_list(
        self, account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSuccessResult, RemoveDevicesFromExclusionListErrorBody]:
        """Removes devices from the exclusion list so that they can be located with Device Location Services requests.

        Args:
            account_name: The numeric name of the account.
            device_list: A list of the device IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/consents"),
            query_params=[param[str]("accountName", account_name), param[str]("deviceList", device_list)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=remove_devices_from_exclusion_list_error_mapper,
            request_options=request_options,
        )


class AsyncExclusionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def devices_location_get_consent_async(
        self, account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAccountDeviceConsent, RawError]:
        """Get the consent settings for the entire account or device list in an account.

        Args:
            account_name: The numeric name of the account.
            device_id: The IMEI of the device being queried
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/devicelocations/action/consents"),
            query_params=[param[str]("accountName", account_name), param[str | None]("deviceId", device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetAccountDeviceConsent],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def devices_location_give_consent_async(
        self,
        *,
        body: AccountConsentCreate | AccountConsentCreateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConsentTransactionId, RawError]:
        """Create a consent record to use location services as an asynchronous request.

        Args:
            body: Account details to create a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/devicelocations/action/consents"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountConsentCreate | AccountConsentCreateDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConsentTransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def devices_location_update_consent(
        self,
        *,
        body: AccountConsentUpdate | AccountConsentUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConsentTransactionId, RawError]:
        """Update the location services consent record for an entire account.

        Args:
            body: Account details to update a consent record.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.device_location("/devicelocations/action/consents"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountConsentUpdate | AccountConsentUpdateDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConsentTransactionId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def exclude_devices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSuccessResult, ExcludeDevicesErrorBody]:
        """This consents endpoint sets a new exclusion list.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/consents"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=exclude_devices_error_mapper,
            request_options=request_options,
        )

    async def list_excluded_devices(
        self, account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DevicesConsentResult, ListExcludedDevicesErrorBody]:
        """This consents endpoint retrieves a list of excluded devices in an account.

        Args:
            account_name: Account identifier in "##########-#####".
            start_index: Zero-based number of the first record to return.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/consents/{accountName}/index/{startIndex}"),
            path_params=[param[str]("accountName", account_name), param[str]("startIndex", start_index)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DevicesConsentResult],
            error_mapper=list_excluded_devices_error_mapper,
            request_options=request_options,
        )

    async def remove_devices_from_exclusion_list(
        self, account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSuccessResult, RemoveDevicesFromExclusionListErrorBody]:
        """Removes devices from the exclusion list so that they can be located with Device Location Services requests.

        Args:
            account_name: The numeric name of the account.
            device_list: A list of the device IDs to remove from the exclusion list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.device_location("/consents"),
            query_params=[param[str]("accountName", account_name), param[str]("deviceList", device_list)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=remove_devices_from_exclusion_list_error_mapper,
            request_options=request_options,
        )
