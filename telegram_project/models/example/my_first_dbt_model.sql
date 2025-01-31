SELECT 
    message_id, 
    message, 
    LENGTH(message) AS message_length 
FROM {{ source('raw_telegram', 'telegram_messages') }}
