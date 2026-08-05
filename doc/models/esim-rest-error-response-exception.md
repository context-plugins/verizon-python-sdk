
# ESIM Rest Error Response Exception

## Structure

`ESIMRestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except ESIMRestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

