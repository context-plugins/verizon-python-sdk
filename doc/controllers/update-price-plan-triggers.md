# Update Price Plan Triggers

```python
update_price_plan_triggers_controller = client.update_price_plan_triggers
```

## Class Name

`UpdatePricePlanTriggersController`


# Update Trigger Rules

Updates a usage trigger at the account level, device level or a price plan trigger for all devices on the account

```python
def update_trigger_rules(self,
                        body)
```

## Authentication

This endpoint requires [thingspace_oauth1](../../doc/auth/oauth-2-client-credentials-grant-1.md) **OR** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [accountLevelUpdateTriggerRequest](../../doc/models/account-level-update-trigger-request.md) \| [deviceLevelUpdateTriggerRequest](../../doc/models/device-level-update-trigger-request.md) \| [accountGroupShareUpdateTriggerRequest](../../doc/models/account-group-share-update-trigger-request.md) \| [accountShareUpdateTriggerRequest](../../doc/models/account-share-update-trigger-request.md) \| [payAsYouGoUpdateTriggerRequest](../../doc/models/pay-as-you-go-update-trigger-request.md) \| [updatetriggerchunk](../../doc/models/updatetriggerchunk.md) | Body, Required | This is a container for any-of cases. |

## Response Type

**200**: Successful request

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TriggerResponse`](../../doc/models/trigger-response.md).

## Example Usage

```python
body = AccountLevelUpdateTriggerRequest(
    trigger_id='b9cc1da6-ffff-eeee-gggg-7eba8859ab5e',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.ACCOUNTUSAGE,
    data_trigger=DataTrigger1(
        condition_type=ConditionTypeEnum.AGING
    ),
    notification=Notificationarray(
        notification_type='PerEvent',
        callback=True,
        email_notification=False,
        notification_group_name='NotificationGroupName',
        notification_frequency_factor=3,
        notification_frequency_interval='Daily',
        external_email_recipients='ExternalEmailRecipients',
        sms_notification=True,
        sms_numbers=[
            Cellphonenumber(
                number='10-digit mobile number',
                carrier='mobile service provider'
            ),
            Cellphonenumber(
                number='10-digit mobile number',
                carrier='mobile service provider'
            )
        ],
        reminder=True,
        severity='Notice'
    ),
    active=ActiveEnum.TRUE
)

result = update_price_plan_triggers_controller.update_trigger_rules(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "be1b5958-ffff-eeee-gggg-b1b7618c0035"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RuleRestErrorResponseException`](../../doc/models/rule-rest-error-response-exception.md) |

