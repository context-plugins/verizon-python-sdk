
# Create Io T Application Request

The request body must include the UUID of the subscription that you want to update plus any properties that you want to change.

## Structure

`CreateIoTApplicationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_name` | `str` | Optional | A user defined name for the application being deployed in Azure IoT Central. |
| `billing_account_id` | `str` | Optional | The ThingSpace ID of the authenticating billing account |
| `client_id` | `str` | Optional | The Azure ClientID of the associated Azure target account |
| `client_secret` | `str` | Optional | The Azure Client Secret of the associated Azure target account |
| `email_i_ds` | `str` | Optional | The “email IDs” to be added to/sent to with this API. |
| `resourcegroup` | `str` | Optional | The Azure Resource group of the associated Azure target account |
| `sample_io_tc_app` | `str` | Optional | This is the reference Azure IoT Central application developed by Verizon. |
| `subscription_id` | `str` | Optional | The Azure Subscription ID of the associated Azure target account |
| `tenant_id` | `str` | Optional | The Azure Tenant ID of the associated Azure target account |

## Example

```python
from verizon.models.create_io_t_application_request import CreateIoTApplicationRequest

create_io_t_application_request = CreateIoTApplicationRequest(
    app_name='newarmapp1',
    billing_account_id='0000123456-00001',
    client_id='UUID',
    client_secret='client secret',
    email_i_ds='email@domain.com',
    resourcegroup='Myresourcegroup',
    sample_io_tc_app='app ID',
    subscription_id='subscription ID',
    tenant_id='tenant ID'
)
```

