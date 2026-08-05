
# Schedules Software Upgrade Request

## Structure

`SchedulesSoftwareUpgradeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `str` | Optional | The campaign name. |
| `software_name` | `str` | Optional | Software name. |
| `software_from` | `str` | Optional | Old software name. |
| `software_to` | `str` | Optional | New software name. |
| `distribution_type` | `str` | Optional | Valid values |
| `start_date` | `str` | Optional | Campaign start date. |
| `end_date` | `str` | Optional | Campaign end date. |
| `download_after_date` | `str` | Optional | Specifies the starting date the client should download the package. If null, client downloads as soon as possible. |
| `download_time_window_list` | [`List[DownloadTimeWindow]`](../../doc/models/download-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `str` | Optional | The date after which you install the package. If null, install as soon as possible. |
| `install_time_window_list` | [`List[DownloadTimeWindow]`](../../doc/models/download-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List[str]` | Optional | Device IMEI list. |

## Example

```python
from verizon.models.schedules_software_upgrade_request import SchedulesSoftwareUpgradeRequest

schedules_software_upgrade_request = SchedulesSoftwareUpgradeRequest(
    campaign_name='FOTA_Verizon_Upgrade',
    software_name='FOTA_Verizon_Model-A_02To03_HF',
    software_from='FOTA_Verizon_Model-A_00To01_HF',
    software_to='FOTA_Verizon_Model-A_02To03_HF',
    distribution_type='HTTP',
    start_date='2021-02-08',
    end_date='2021-02-08',
    download_after_date='2021-02-08'
)
```

