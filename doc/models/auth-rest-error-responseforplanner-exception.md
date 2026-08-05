
# Auth Rest Error Responseforplanner Exception

## Structure

`AuthRestErrorResponseforplannerException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fault` | [`AuthSubRestErrorResponseforplanner`](../../doc/models/auth-sub-rest-error-responseforplanner.md) | Optional | - |

## Example

```python
try:
    # make the API call
except AuthRestErrorResponseforplannerException as e:
    print(e)
except APIException as e:
    print(e)
```

