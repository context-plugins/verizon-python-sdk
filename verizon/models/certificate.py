from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class Certificate(SdkBaseModel):
    """Structure for the credentials required to connect to the ETX MQTT Message Exchange."""

    cert_pem: str = Field(alias="cert.pem")
    """The string containing the certificate"""

    key_pem: str = Field(alias="key.pem")
    """The string containing the private key"""

    ca_pem: str = Field(alias="ca.pem")
    """The string containing the CA certificate"""

    expiration_time: RFC3339DateTime = Field(alias="ExpirationTime")
    """The string describing the expiration timestamp of the certificate"""


class CertificateDict(TypedDict):
    cert_pem: str
    key_pem: str
    ca_pem: str
    expiration_time: RFC3339DateTime
