
# Rest Error Responseforplanner Exception

## Structure

`RestErrorResponseforplannerException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |
| `error_url` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except RestErrorResponseforplannerException as e:
    print(e)
except APIException as e:
    print(e)
```

