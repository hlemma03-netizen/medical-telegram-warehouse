SELECT
    message_id,
    channel_name,
    message_date,
    message_text,
    views,
    forwards,
    has_media,
    image_path,
    LENGTH(message_text) AS message_length,
    has_media AS has_image
FROM raw.telegram_messages
WHERE message_text IS NOT NULL;