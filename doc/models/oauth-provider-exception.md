
# Oauth Provider Exception

OAuth 2 Authorization endpoint exception.

## Structure

`OauthProviderException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | [`OauthProviderErrorEnum`](../../doc/models/oauth-provider-error-enum.md) | Required | Gets or sets error code. |
| `error_description` | `str` | Optional | Gets or sets human-readable text providing additional information on error.<br>Used to assist the client developer in understanding the error that occurred. |
| `error_uri` | `str` | Optional | Gets or sets a URI identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error. |

## Example

```python
try:
    # make the API call
except OauthProviderException as e:
    print(e)
except APIException as e:
    print(e)
```

