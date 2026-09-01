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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.create_io_tapplication_request import CreateIoTapplicationRequest, CreateIoTapplicationRequestDict
from ..models.create_io_tapplication_response import CreateIoTapplicationResponse
from ..models.create_target_request import CreateTargetRequest, CreateTargetRequestDict
from ..models.delete_target_request import DeleteTargetRequest, DeleteTargetRequestDict
from ..models.generate_external_idrequest import GenerateExternalIdrequest, GenerateExternalIdrequestDict
from ..models.generate_external_idresult import GenerateExternalIdresult
from ..models.query_target_request import QueryTargetRequest, QueryTargetRequestDict
from ..models.target import Target
from ..server.server import Server


class Targets:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TargetsWithRawResponse(client, server, auth)

    def create_azure_central_io_t_application(
        self,
        billingaccount_id: str,
        body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateIoTapplicationResponse:
        """Deploy a new Azure IoT Central application based on the Verizon ARM template within the specified Azure
        Active Directory account.

        Args:
            billingaccount_id: TThe ThingSpace ID of the authenticating billing account.
            body: The request body must include the UUID of the subscription that you want to update plus any properties
                that you want to change.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes the full subscription resource definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_azure_central_io_t_application(
            billingaccount_id, body, request_options=request_options
        ).unwrap()

    def create_target(
        self,
        body: CreateTargetRequest | CreateTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Target:
        """Define a target to receive data streams, alerts, or callbacks. After creating the target resource, use its ID
        in a subscription to set up a data stream.

        Args:
            body: The request body provides the details of the target that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes the full target resource definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_target(body, request_options=request_options).unwrap()

    def delete_target(
        self,
        body: DeleteTargetRequest | DeleteTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a target from a ThingSpace account.

        Args:
            body: The request body identifies the target to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_target(body, request_options=request_options).unwrap()

    def generate_target_external_id(
        self,
        body: GenerateExternalIdrequest | GenerateExternalIdrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateExternalIdresult:
        """Create a unique string that ThingSpace will pass to AWS for increased security.

        Args:
            body: The request body only contains the authenticating account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns a new external ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.generate_target_external_id(body, request_options=request_options).unwrap()

    def query_target(
        self, body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Target]:
        """Search for targets by property values. Returns an array of all matching target resources.

        Args:
            body: Search for targets by property values.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching targets. Each target includes the full target resource
            definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.query_target(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TargetsWithRawResponse:
        return self._with_raw_response


class AsyncTargets:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTargetsWithRawResponse(client, server, auth)

    async def create_azure_central_io_t_application(
        self,
        billingaccount_id: str,
        body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateIoTapplicationResponse:
        """Deploy a new Azure IoT Central application based on the Verizon ARM template within the specified Azure
        Active Directory account.

        Args:
            billingaccount_id: TThe ThingSpace ID of the authenticating billing account.
            body: The request body must include the UUID of the subscription that you want to update plus any properties
                that you want to change.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes the full subscription resource definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_azure_central_io_t_application(
                billingaccount_id, body, request_options=request_options
            )
        ).unwrap()

    async def create_target(
        self,
        body: CreateTargetRequest | CreateTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Target:
        """Define a target to receive data streams, alerts, or callbacks. After creating the target resource, use its ID
        in a subscription to set up a data stream.

        Args:
            body: The request body provides the details of the target that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes the full target resource definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_target(body, request_options=request_options)).unwrap()

    async def delete_target(
        self,
        body: DeleteTargetRequest | DeleteTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a target from a ThingSpace account.

        Args:
            body: The request body identifies the target to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Target deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_target(body, request_options=request_options)).unwrap()

    async def generate_target_external_id(
        self,
        body: GenerateExternalIdrequest | GenerateExternalIdrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateExternalIdresult:
        """Create a unique string that ThingSpace will pass to AWS for increased security.

        Args:
            body: The request body only contains the authenticating account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns a new external ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.generate_target_external_id(body, request_options=request_options)
        ).unwrap()

    async def query_target(
        self, body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Target]:
        """Search for targets by property values. Returns an array of all matching target resources.

        Args:
            body: Search for targets by property values.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A success response includes an array of all matching targets. Each target includes the full target resource
            definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.query_target(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTargetsWithRawResponse:
        return self._with_raw_response


class TargetsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_azure_central_io_t_application(
        self,
        billingaccount_id: str,
        body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateIoTapplicationResponse, RawError]:
        """Deploy a new Azure IoT Central application based on the Verizon ARM template within the specified Azure
        Active Directory account.

        Args:
            billingaccount_id: TThe ThingSpace ID of the authenticating billing account.
            body: The request body must include the UUID of the subscription that you want to update plus any properties
                that you want to change.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/newaic"),
            headers=[param[str]("BillingaccountID", billingaccount_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateIoTapplicationRequest | CreateIoTapplicationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CreateIoTapplicationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_target(
        self,
        body: CreateTargetRequest | CreateTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Target, RawError]:
        """Define a target to receive data streams, alerts, or callbacks. After creating the target resource, use its ID
        in a subscription to set up a data stream.

        Args:
            body: The request body provides the details of the target that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTargetRequest | CreateTargetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Target],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_target(
        self,
        body: DeleteTargetRequest | DeleteTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a target from a ThingSpace account.

        Args:
            body: The request body identifies the target to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteTargetRequest | DeleteTargetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_target_external_id(
        self,
        body: GenerateExternalIdrequest | GenerateExternalIdrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateExternalIdresult, RawError]:
        """Create a unique string that ThingSpace will pass to AWS for increased security.

        Args:
            body: The request body only contains the authenticating account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/newextid"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateExternalIdrequest | GenerateExternalIdrequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GenerateExternalIdresult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def query_target(
        self, body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Target], RawError]:
        """Search for targets by property values. Returns an array of all matching target resources.

        Args:
            body: Search for targets by property values.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QueryTargetRequest | QueryTargetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Target]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTargetsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_azure_central_io_t_application(
        self,
        billingaccount_id: str,
        body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateIoTapplicationResponse, RawError]:
        """Deploy a new Azure IoT Central application based on the Verizon ARM template within the specified Azure
        Active Directory account.

        Args:
            billingaccount_id: TThe ThingSpace ID of the authenticating billing account.
            body: The request body must include the UUID of the subscription that you want to update plus any properties
                that you want to change.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/newaic"),
            headers=[param[str]("BillingaccountID", billingaccount_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateIoTapplicationRequest | CreateIoTapplicationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[CreateIoTapplicationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_target(
        self,
        body: CreateTargetRequest | CreateTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Target, RawError]:
        """Define a target to receive data streams, alerts, or callbacks. After creating the target resource, use its ID
        in a subscription to set up a data stream.

        Args:
            body: The request body provides the details of the target that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTargetRequest | CreateTargetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Target],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_target(
        self,
        body: DeleteTargetRequest | DeleteTargetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a target from a ThingSpace account.

        Args:
            body: The request body identifies the target to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteTargetRequest | DeleteTargetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_target_external_id(
        self,
        body: GenerateExternalIdrequest | GenerateExternalIdrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateExternalIdresult, RawError]:
        """Create a unique string that ThingSpace will pass to AWS for increased security.

        Args:
            body: The request body only contains the authenticating account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/newextid"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateExternalIdrequest | GenerateExternalIdrequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GenerateExternalIdresult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def query_target(
        self, body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Target], RawError]:
        """Search for targets by property values. Returns an array of all matching target resources.

        Args:
            body: Search for targets by property values.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/targets/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QueryTargetRequest | QueryTargetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Target]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
