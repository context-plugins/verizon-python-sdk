
# Fota V3 Result Exception

Error response.

## Structure

`FotaV3ResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | Error code string. |
| `error_message` | `str` | Required | Error message string. |

## Example

```python
try:
    # make the API call
except FotaV3ResultException as e:
    print(e)
except APIException as e:
    print(e)
```

