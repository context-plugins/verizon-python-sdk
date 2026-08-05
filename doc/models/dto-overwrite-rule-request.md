
# Dto Overwrite Rule Request

## Structure

`DtoOverwriteRuleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `resourceidentifier` | [`DtoResourceidentifier`](../../doc/models/dto-resourceidentifier.md) | Optional | - |
| `rule` | [`ResourceRule`](../../doc/models/resource-rule.md) | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from verizon.models.dto_overwrite_rule_request import DtoOverwriteRuleRequest
from verizon.models.dto_resourceidentifier import DtoResourceidentifier
from verizon.models.resource_rule import ResourceRule

dto_overwrite_rule_request = DtoOverwriteRuleRequest(
    accountname='0000123456-00001',
    resourceidentifier=DtoResourceidentifier(
        id='id4'
    ),
    rule=ResourceRule(
        createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        foreignid='foreignid8',
        lastupdated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        rulechain=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        versionid='versionid2',
        accountclientid='accountclientid4',
        billingaccountid='billingaccountid6',
        description='description0',
        deviceid='deviceid0',
        disabled=False
    )
)
```

