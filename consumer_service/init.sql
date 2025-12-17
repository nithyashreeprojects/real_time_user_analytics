CREATE TABLE IF NOT EXISTS user_events (
    user_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_time TIMESTAMPTZ NOT NULL
);

SELECT create_hypertable(
    'user_events',
    'event_time',
    if_not_exists => TRUE
);
