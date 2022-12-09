SELECT *
FROM scheduled_posts
WHERE time <= strftime('%s', 'now');
