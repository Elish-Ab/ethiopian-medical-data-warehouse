SELECT *
FROM {{ ref('telegram_messages') }}
WHERE LENGTH(message) IS NULL