
# Upgrade Status Enum

The status of the upgrades that you want to retrieve.

## Enumeration

`UpgradeStatusEnum`

## Fields

| Name |
|  --- |
| `REQUESTPENDING` |
| `QUEUED` |
| `REQUESTFAILED` |
| `INPROGRESS` |
| `FINISHED` |
| `UPGRADEFAILED` |

## Example

```python
from verizon.models.upgrade_status_enum import UpgradeStatusEnum

upgrade_status = UpgradeStatusEnum.REQUESTPENDING
```

