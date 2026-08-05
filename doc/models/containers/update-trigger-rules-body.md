
# Update Trigger Rules Body

## Data Type

`AccountLevelUpdateTriggerRequest | DeviceLevelUpdateTriggerRequest | AccountGroupShareUpdateTriggerRequest | AccountShareUpdateTriggerRequest | PayAsYouGoUpdateTriggerRequest | Updatetriggerchunk`

## Cases

| Type |
|  --- |
| [`AccountLevelUpdateTriggerRequest`](../../../doc/models/account-level-update-trigger-request.md) |
| [`DeviceLevelUpdateTriggerRequest`](../../../doc/models/device-level-update-trigger-request.md) |
| [`AccountGroupShareUpdateTriggerRequest`](../../../doc/models/account-group-share-update-trigger-request.md) |
| [`AccountShareUpdateTriggerRequest`](../../../doc/models/account-share-update-trigger-request.md) |
| [`PayAsYouGoUpdateTriggerRequest`](../../../doc/models/pay-as-you-go-update-trigger-request.md) |
| [`Updatetriggerchunk`](../../../doc/models/updatetriggerchunk.md) |

## AccountLevelUpdateTriggerRequest

### Initialization Code

#### Example

```python
value = AccountLevelUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    notification_type='PerEvent',
    callback=True,
    email_notification=False,
    notification_group_name='Notification Group Name (User defined)',
    notification_frequency_factor=3,
    notification_frequency_interval='Daily',
    external_email_recipients='Email addresses',
    sms_notification=True,
    reminder=True,
    severity='Notify',
    active=ActiveEnum.TRUE
)
```

## DeviceLevelUpdateTriggerRequest

### Initialization Code

#### Example

```python
value = DeviceLevelUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

## AccountGroupShareUpdateTriggerRequest

### Initialization Code

#### Example

```python
value = AccountGroupShareUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    account_name='0000123456-00001',
    active=ActiveEnum.TRUE
)
```

## AccountShareUpdateTriggerRequest

### Initialization Code

#### Example

```python
value = AccountShareUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

## PayAsYouGoUpdateTriggerRequest

### Initialization Code

#### Example

```python
value = PayAsYouGoUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

## Updatetriggerchunk

### Initialization Code

#### Example

```python
value = Updatetriggerchunk(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

