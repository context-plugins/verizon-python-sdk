
# Rest Error Response Exception

## Structure

`RestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | **Constraints**: *Maximum Length*: `3`, *Pattern*: `^[0-9]{3}$` |
| `error_message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except RestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

