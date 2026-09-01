from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateIoTapplicationRequest(SdkBaseModel):
    """The request body must include the UUID of the subscription that you want to update plus any properties that you
    want to change."""

    app_name: Optional[str] = Field(default=UNSET, alias="appName")
    """A user defined name for the application being deployed in Azure IoT Central."""

    billing_account_id: Optional[str] = Field(default=UNSET, alias="billingAccountID")
    """The ThingSpace ID of the authenticating billing account"""

    client_id: Optional[str] = Field(default=UNSET, alias="clientID")
    """The Azure ClientID of the associated Azure target account"""

    client_secret: Optional[str] = Field(default=UNSET, alias="clientSecret")
    """The Azure Client Secret of the associated Azure target account"""

    email_ids: Optional[str] = Field(default=UNSET, alias="emailIDs")
    """The “email IDs” to be added to/sent to with this API."""

    resourcegroup: Optional[str] = UNSET
    """The Azure Resource group of the associated Azure target account"""

    sample_io_tc_app: Optional[str] = Field(default=UNSET, alias="sampleIOTcApp")
    """This is the reference Azure IoT Central application developed by Verizon."""

    subscription_id: Optional[str] = Field(default=UNSET, alias="subscriptionID")
    """The Azure Subscription ID of the associated Azure target account"""

    tenant_id: Optional[str] = Field(default=UNSET, alias="tenantID")
    """The Azure Tenant ID of the associated Azure target account"""


class CreateIoTapplicationRequestDict(TypedDict):
    app_name: NotRequired[str]
    billing_account_id: NotRequired[str]
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    email_ids: NotRequired[str]
    resourcegroup: NotRequired[str]
    sample_io_tc_app: NotRequired[str]
    subscription_id: NotRequired[str]
    tenant_id: NotRequired[str]
