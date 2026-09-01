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
    json_decoder,
    multipart_body,
    param,
)
from ..errors.get_list_of_files_error import GetListOfFilesErrorBody, get_list_of_files_error_mapper
from ..errors.upload_config_file_error import UploadConfigFileErrorBody, upload_config_file_error_mapper
from ..models.retrieves_available_files_response_list import RetrievesAvailableFilesResponseList
from ..models.upload_configuration_files_response import UploadConfigurationFilesResponse
from ..server.server import Server


class ConfigurationFiles:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ConfigurationFilesWithRawResponse(client, server, auth)

    def get_list_of_files(
        self, acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrievesAvailableFilesResponseList:
        """You can retrieve a list of configuration or supplementary of files for an account.

        Args:
            acc: Account identifier.
            distribution_type: Filter the distributionType to only retrieve files for a specific distribution type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_list_of_files(
            acc, distribution_type, request_options=request_options
        ).unwrap()

    def upload_config_file(
        self,
        acc: str,
        *,
        file_version: str | None = None,
        make: str | None = None,
        model: str | None = None,
        local_target_path: str | None = None,
        fileupload: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadConfigurationFilesResponse:
        """Uploads a configuration/supplementary file for an account. ThingSpace generates a fileName after the upload
        and is returned in the response.

        Args:
            acc: Account identifier.
            file_version: Version of the file.
            make: The software-applicable device make.
            model: The software-applicable device model.
            local_target_path: Local target path on the device.
            fileupload: The file to upload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.upload_config_file(
            acc,
            file_version=file_version,
            make=make,
            model=model,
            local_target_path=local_target_path,
            fileupload=fileupload,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ConfigurationFilesWithRawResponse:
        return self._with_raw_response


class AsyncConfigurationFiles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncConfigurationFilesWithRawResponse(client, server, auth)

    async def get_list_of_files(
        self, acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrievesAvailableFilesResponseList:
        """You can retrieve a list of configuration or supplementary of files for an account.

        Args:
            acc: Account identifier.
            distribution_type: Filter the distributionType to only retrieve files for a specific distribution type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_list_of_files(acc, distribution_type, request_options=request_options)
        ).unwrap()

    async def upload_config_file(
        self,
        acc: str,
        *,
        file_version: str | None = None,
        make: str | None = None,
        model: str | None = None,
        local_target_path: str | None = None,
        fileupload: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadConfigurationFilesResponse:
        """Uploads a configuration/supplementary file for an account. ThingSpace generates a fileName after the upload
        and is returned in the response.

        Args:
            acc: Account identifier.
            file_version: Version of the file.
            make: The software-applicable device make.
            model: The software-applicable device model.
            local_target_path: Local target path on the device.
            fileupload: The file to upload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful responses.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.upload_config_file(
                acc,
                file_version=file_version,
                make=make,
                model=model,
                local_target_path=local_target_path,
                fileupload=fileupload,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncConfigurationFilesWithRawResponse:
        return self._with_raw_response


class ConfigurationFilesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_list_of_files(
        self, acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrievesAvailableFilesResponseList, GetListOfFilesErrorBody]:
        """You can retrieve a list of configuration or supplementary of files for an account.

        Args:
            acc: Account identifier.
            distribution_type: Filter the distributionType to only retrieve files for a specific distribution type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/files/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[param[str]("distributionType", distribution_type)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RetrievesAvailableFilesResponseList],
            error_mapper=get_list_of_files_error_mapper,
            request_options=request_options,
        )

    def upload_config_file(
        self,
        acc: str,
        *,
        file_version: str | None = None,
        make: str | None = None,
        model: str | None = None,
        local_target_path: str | None = None,
        fileupload: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadConfigurationFilesResponse, UploadConfigFileErrorBody]:
        """Uploads a configuration/supplementary file for an account. ThingSpace generates a fileName after the upload
        and is returned in the response.

        Args:
            acc: Account identifier.
            file_version: Version of the file.
            make: The software-applicable device make.
            model: The software-applicable device model.
            local_target_path: Local target path on the device.
            fileupload: The file to upload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/files/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [
                    param[str | None]("fileVersion", file_version),
                    param[str | None]("make", make),
                    param[str | None]("model", model),
                    param[str | None]("localTargetPath", local_target_path),
                ],
                {"fileupload": fileupload},
            ),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UploadConfigurationFilesResponse],
            error_mapper=upload_config_file_error_mapper,
            request_options=request_options,
        )


class AsyncConfigurationFilesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_list_of_files(
        self, acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrievesAvailableFilesResponseList, GetListOfFilesErrorBody]:
        """You can retrieve a list of configuration or supplementary of files for an account.

        Args:
            acc: Account identifier.
            distribution_type: Filter the distributionType to only retrieve files for a specific distribution type.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/files/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[param[str]("distributionType", distribution_type)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RetrievesAvailableFilesResponseList],
            error_mapper=get_list_of_files_error_mapper,
            request_options=request_options,
        )

    async def upload_config_file(
        self,
        acc: str,
        *,
        file_version: str | None = None,
        make: str | None = None,
        model: str | None = None,
        local_target_path: str | None = None,
        fileupload: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadConfigurationFilesResponse, UploadConfigFileErrorBody]:
        """Uploads a configuration/supplementary file for an account. ThingSpace generates a fileName after the upload
        and is returned in the response.

        Args:
            acc: Account identifier.
            file_version: Version of the file.
            make: The software-applicable device make.
            model: The software-applicable device model.
            local_target_path: Local target path on the device.
            fileupload: The file to upload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/files/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [
                    param[str | None]("fileVersion", file_version),
                    param[str | None]("make", make),
                    param[str | None]("model", model),
                    param[str | None]("localTargetPath", local_target_path),
                ],
                {"fileupload": fileupload},
            ),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UploadConfigurationFilesResponse],
            error_mapper=upload_config_file_error_mapper,
            request_options=request_options,
        )
