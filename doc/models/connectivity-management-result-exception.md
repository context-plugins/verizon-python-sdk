
# Connectivity Management Result Exception

Response to errors.

## Structure

`ConnectivityManagementResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | Code of the error. |
| `error_message` | `str` | Optional | Details of the error. |

## Example

```python
try:
    # make the API call
except ConnectivityManagementResultException as e:
    print(e)
except APIException as e:
    print(e)
```

