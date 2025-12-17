import json
import time
import os
import psycopg2
from kafka import KafkaConsumer
 
# -----------------------------
# Kafka config
# -----------------------------
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "user-events")
GROUP_ID = os.getenv("KAFKA_GROUP_ID", "analytics-consumer")

# -----------------------------
# TimescaleDB / Postgres config
# -----------------------------
DB_HOST = os.getenv("DB_HOST", "timescaledb")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "analytics")
DB_USER = os.getenv("DB_USER", "analytics_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "analytics_pass")

# -----------------------------
# Wait for Postgres
# -----------------------------
print("Waiting for TimescaleDB...")
while True:
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        conn.close()
        print("Connected to TimescaleDB")
        break
    except Exception as e:
        print("Postgres not ready, retrying...", e)
        time.sleep(5)

# -----------------------------
# Connect to Kafka
# -----------------------------
print("Connecting to Kafka...")
while True:
    try:
        consumer = KafkaConsumer(
            TOPIC,
            bootstrap_servers=KAFKA_BROKER,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=GROUP_ID,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )
        print("Connected to Kafka")
        break
    except Exception as e:
        print("Kafka not ready, retrying...", e)
        time.sleep(5)

# -----------------------------
# Insert query
# -----------------------------
INSERT_QUERY = """
INSERT INTO user_events (user_id, event_type, event_time)
VALUES (%s, %s, %s)
"""

# -----------------------------
# Consume messages
# -----------------------------
print("Waiting for messages...")
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
)
cur = conn.cursor()

for message in consumer:
    data = message.value
    print("Received:", data)

    cur.execute(
        INSERT_QUERY,
        (
            data["user_id"],
            data["event_type"],
            data["timestamp"],
        ),
    )
    conn.commit()
