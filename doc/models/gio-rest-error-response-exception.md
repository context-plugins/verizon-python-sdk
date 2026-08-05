
# GIO Rest Error Response Exception

## Structure

`GIORestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3`, *Pattern*: `^[0-9]{3,3}$` |
| `error_message` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `1000`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |

## Example

```python
try:
    # make the API call
except GIORestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

