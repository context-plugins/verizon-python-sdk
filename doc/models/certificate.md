
# Certificate

Structure for the credentials required to connect to the ETX MQTT Message Exchange.

## Structure

`Certificate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cert_pem` | `str` | Required | The string containing the certificate<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `4096`, *Pattern*: ``^[a-zA-Z0-9~\+\-!@#$%^&*()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `key_pem` | `str` | Required | The string containing the private key<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `4096`, *Pattern*: ``^[a-zA-Z0-9~\+\-!@#$%^&*()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `ca_pem` | `str` | Required | The string containing the CA certificate<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `4096`, *Pattern*: ``^[a-zA-Z0-9~\+\-!@#$%^&*()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `expiration_time` | `datetime` | Required | The string describing the expiration timestamp of the certificate |

## Example

```python
import dateutil.parser

from verizon.models.certificate import Certificate

certificate = Certificate(
    cert_pem='"-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgICEAEwDQYJKoZIhvcNAQELBQAwUjELMAkGA1UEBhMCQVUx\n...\nuuA1Zog3aBOeeEzp9SEJBMTJRYPXbK4e8Xer+7m98OL/3g==\n-----END CERTIFICATE-----"\n',
    key_pem='"-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDa1lF7DWudshQ5\n...\nJbjD2hacWGzpKzTfn5Mt1frE\n-----END PRIVATE KEY-----"\n',
    ca_pem='"-----BEGIN CERTIFICATE-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDa1lF7DWudshQ5\n...\nJbjD2hacWGzpKzTfn5Mt1frE\n-----END CERTIFICATE-----"\n',
    expiration_time=dateutil.parser.parse('2017-07-21T17:32:28Z')
)
```

