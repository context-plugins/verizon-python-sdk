
# Rule Rest Error Response Exception

## Structure

`RuleRestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except RuleRestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

