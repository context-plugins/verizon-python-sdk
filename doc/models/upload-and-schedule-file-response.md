
# Upload and Schedule File Response

## Structure

`UploadAndScheduleFileResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Updgrade identifier. |
| `account_name` | `str` | Optional | Account identifer. |
| `campaign_name` | `str` | Optional | The campaign name. |
| `software_name` | `str` | Optional | Software name. |
| `software_from` | `str` | Optional | Old software name. |
| `software_to` | `str` | Optional | New software name. |
| `file_name` | `str` | Optional | The name of the file you are upgrading to. |
| `file_version` | `str` | Optional | The version of the file you are upgrading to. |
| `distribution_type` | `str` | Optional | Valid values |
| `make` | `str` | Optional | Applicable make. |
| `model` | `str` | Optional | Applicable model. |
| `start_date` | `str` | Optional | Campaign start date. |
| `end_date` | `str` | Optional | Campaign end date. |
| `download_after_date` | `str` | Optional | Specifies the starting date the client should download the package. If null, client downloads as soon as possible. |
| `download_time_window_list` | [`List[DownloadTimeWindow]`](../../doc/models/download-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `str` | Optional | The date after which you install the package. If null, install as soon as possible. |
| `install_time_window_list` | [`List[DownloadTimeWindow]`](../../doc/models/download-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List[str]` | Optional | Device IMEI list. |
| `status` | `str` | Optional | Software update status. |

## Example

```python
from verizon.models.upload_and_schedule_file_response import UploadAndScheduleFileResponse

upload_and_schedule_file_response = UploadAndScheduleFileResponse(
    id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
    account_name='0242078689-00001',
    campaign_name='FOTA_Verizon_Upgrade',
    software_name='FOTA_Verizon_Model-A_02To03_HF',
    software_from='FOTA_Verizon_Model-A_00To01_HF',
    software_to='FOTA_Verizon_Model-A_02To03_HF',
    file_name='configfile-Verizon_VZW1_hello-world.txt',
    file_version='1.0',
    distribution_type='HTTP',
    make='Verizon',
    model='Model-A',
    start_date='2021-02-08',
    end_date='2021-02-08',
    download_after_date='2021-02-08',
    status='pending'
)
```

