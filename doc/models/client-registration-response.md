
# Client Registration Response

Response for /clients/registration. It provides a generated device ID and the certificates needed to connect the ETX Message Exchange.

## Structure

`ClientRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `uuid\|str` | Required | The generated ID (UUID v4) for the device. It can be used as:<br><br>- the MQTT Client ID when connecting to the Message Exchange system<br>- a parameter when asking for the connection endpoint<br>- a parameter when finishing the device registration<br>- a parameter when unregistering the device |
| `certificate` | [`Certificate`](../../doc/models/certificate.md) | Required | Structure for the credentials required to connect to the ETX MQTT Message Exchange. |

## Example

```python
import dateutil.parser

from verizon.models.certificate import Certificate
from verizon.models.client_registration_response import ClientRegistrationResponse

client_registration_response = ClientRegistrationResponse(
    device_id='a4fcd16a-343d-4527-8203-2f46e3e4ff4b',
    certificate=Certificate(
        cert_pem='"-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgICEAEwDQYJKoZIhvcNAQELBQAwUjELMAkGA1UEBhMCQVUx\n...\nuuA1Zog3aBOeeEzp9SEJBMTJRYPXbK4e8Xer+7m98OL/3g==\n-----END CERTIFICATE-----"\n',
        key_pem='"-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDa1lF7DWudshQ5\n...\nJbjD2hacWGzpKzTfn5Mt1frE\n-----END PRIVATE KEY-----"\n',
        ca_pem='"-----BEGIN CERTIFICATE-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDa1lF7DWudshQ5\n...\nJbjD2hacWGzpKzTfn5Mt1frE\n-----END CERTIFICATE-----"\n',
        expiration_time=dateutil.parser.parse('2017-07-21T17:32:28Z')
    )
)
```

