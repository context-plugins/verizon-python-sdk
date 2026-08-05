
# ETX Responding Error Exception

error response structure

## Structure

`ETXRespondingErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | The short summary of the error<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `1024`, *Pattern*: ``^[\w~\+\-!@#$%^&*()\`\[\]{=};\"':,.\\\/<>?\|\s]*$`` |
| `description` | `str` | Required | The detailed description of the error<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `4096`, *Pattern*: ``^[\w~\+\-!@#$%^&*()\`\[\]{=};\"':,.\\\/<>?\|\s]*$`` |

## Example

```python
try:
    # make the API call
except ETXRespondingErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

