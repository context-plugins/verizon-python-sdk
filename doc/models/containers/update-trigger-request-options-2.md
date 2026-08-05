
# Update Trigger Request Options 2

## Data Type

`TriggerType3 | ActiveAnomalyIndicator`

## Cases

| Type |
|  --- |
| [`TriggerType3`](../../../doc/models/trigger-type-3.md) |
| [`ActiveAnomalyIndicator`](../../../doc/models/active-anomaly-indicator.md) |

## TriggerType3

### Initialization Code

#### Example

```python
value = TriggerType3(
    trigger_id='595f5c44-c31c-4552-8670-020a1545a84d',
    trigger_name='Anomaly Daily Usage REST Test-Patch Update 4',
    trigger_category='UsageAnomaly',
    account_name='0000123456-00001',
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=False,
        include_over_expected_usage=True
    ),
    notification=TriggerNotification(
        notification_type='DailySummary',
        callback=True,
        email_notification=False,
        notification_group_name='Anomaly Test API',
        notification_frequency_factor=3,
        notification_frequency_interval='Hourly',
        external_email_recipients='placeholder@verizon.com',
        sms_notification=True,
        sms_numbers=[
            SMSNumber(
                carrier='US Cellular',
                number='9299280711'
            )
        ],
        reminder=True,
        severity='Critical'
    )
)
```

## ActiveAnomalyIndicator

### Initialization Code

#### Example

```python
value = ActiveAnomalyIndicator(
    active=True
)
```

