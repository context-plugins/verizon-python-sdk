
# Dto Configuration Profile Delete

## Structure

`DtoConfigurationProfileDelete`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric account name, which must include leading zeros |
| `resourceidentifier` | [`DtoResourceidentifier`](../../doc/models/dto-resourceidentifier.md) | Optional | - |

## Example

```python
from verizon.models.dto_configuration_profile_delete import DtoConfigurationProfileDelete
from verizon.models.dto_resourceidentifier import DtoResourceidentifier

dto_configuration_profile_delete = DtoConfigurationProfileDelete(
    account_name='0000123456-00001',
    resourceidentifier=DtoResourceidentifier(
        id='id4'
    )
)
```

