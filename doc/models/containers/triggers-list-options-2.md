
# Triggers List Options 2

## Data Type

`AnomalyTriggerValue | TriggerType2`

## Cases

| Type |
|  --- |
| [`AnomalyTriggerValue`](../../../doc/models/anomaly-trigger-value.md) |
| [`TriggerType2`](../../../doc/models/trigger-type-2.md) |

## AnomalyTriggerValue

### Initialization Code

#### Example

```python
value = AnomalyTriggerValue(
    trigger_id='BE1B5958-3E11-41DB-9ABD-B1B7618C0035',
    trigger_name='Anomaly Daily Usage REST Test-1',
    organization_name='AnamolyDetectionRTRTest',
    trigger_category='UsageAnomaly',
    trigger_attributes=[
        NotificationGroupNameTriggerAttribute(
            key='DataPercentage50'
        )
    ],
    created_at='2021-10-21T23:57:03.397.0000Z',
    modified_at='2021-10-21T23:57:03.397.0000Z'
)
```

## TriggerType2

### Initialization Code

#### Example

```python
value = TriggerType2(
    anomalyattributes=UsageAnomalyAttributes(
        account_names='0000123456-00001',
        device_group='User Group 1',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    ),
    notification=TriggerNotification(
        notification_type='DailySummary',
        callback=True,
        email_notification=True,
        notification_group_name='Anomaly Test API',
        notification_frequency_factor=-2147483648,
        external_email_recipients='placeholder@verizon.com',
        sms_notification=True,
        sms_numbers=[
            SMSNumber(
                carrier='US Cellular',
                number='9299280711'
            )
        ],
        reminder=False,
        severity='Critical'
    )
)
```

