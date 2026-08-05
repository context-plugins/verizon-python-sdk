
# Custom Header Signature



Documentation for accessing and setting credentials for sessionToken.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| SessionToken | `str` | This is the Session/M2M token needed to authenticate the user. It should be acquired by using the ThingSpace APIs. For detail on how to obtain a Session/M2M token please refer to the<br><br>- [ThingSpace Quick Start Guide - Obtaining a VZ-M2M Session Token Programmatically](https://thingspace.verizon.com/documentation/api-documentation.html#/http/quick-start/credentials-and-tokens/obtaining-a-vz-m2m-sessiontoken-programmatically)<br>- or the [ThingSpace API Video Guide 1](https://www.youtube.com/watch?v=QPJQFT3637w) and [ThingSpace API Video Guide 2](https://www.youtube.com/watch?v=hc9udGp4P_s) | `session_token` |



**Note:** Auth credentials can be set using `SessionTokenCredentials` object, passed in as named parameter `session_token_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from verizon.http.auth.session_token import SessionTokenCredentials
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    session_token_credentials=SessionTokenCredentials(
        session_token='SessionToken'
    )
)
```


