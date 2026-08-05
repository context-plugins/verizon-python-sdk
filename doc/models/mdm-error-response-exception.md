
# Mdm Error Response Exception

error response structure

## Structure

`MdmErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | The short summary of the error<br><br>**Constraints**: *Maximum Length*: `1024`, *Pattern*: `^[a-zA-Z0-9_-]+$` |
| `description` | `str` | Required | The detailed description of the error<br><br>**Constraints**: *Maximum Length*: `4096`, *Pattern*: `^[a-zA-Z0-9_-]+$` |
| `uuid` | `uuid\|str` | Required | The unique identifier of the request for tracing |
| `timestamp` | `datetime` | Required | The timestamp of when the error occurred |

## Example

```python
try:
    # make the API call
except MdmErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

