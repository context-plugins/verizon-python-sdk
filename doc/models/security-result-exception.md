
# Security Result Exception

Error response.

## Structure

`SecurityResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3`, *Pattern*: `^[0-9]{3,3}$` |
| `error_message` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `error_url` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^https://[A-Za-z0-9].[A-Za-z]{3,64}$` |

## Example

```python
try:
    # make the API call
except SecurityResultException as e:
    print(e)
except APIException as e:
    print(e)
```

