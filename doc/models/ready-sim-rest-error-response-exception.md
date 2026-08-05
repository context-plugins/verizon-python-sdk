
# Ready Sim Rest Error Response Exception

## Structure

`ReadySimRestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except ReadySimRestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

