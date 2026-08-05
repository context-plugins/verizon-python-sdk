
# Fota V2 Result Exception

Response for error cases.

## Structure

`FotaV2ResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | Code of the error. |
| `error_message` | `str` | Required | Details of the error. |

## Example

```python
try:
    # make the API call
except FotaV2ResultException as e:
    print(e)
except APIException as e:
    print(e)
```

