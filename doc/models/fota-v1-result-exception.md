
# Fota V1 Result Exception

Response in case of any errors.

## Structure

`FotaV1ResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | Error response code. |
| `error_message` | `str` | Required | Description of the error. |

## Example

```python
try:
    # make the API call
except FotaV1ResultException as e:
    print(e)
except APIException as e:
    print(e)
```

