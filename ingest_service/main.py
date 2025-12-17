from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json
import os
import time

app = FastAPI()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

producer = None

@app.on_event("startup")
def startup_event():
    global producer
    retries = 10
    while retries > 0:
        try:
            producer = KafkaProducer(
                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            print("Kafka producer connected")
            return
        except Exception as e:
            print(f"Kafka not ready, retrying... ({retries})", e)
            retries -= 1
            time.sleep(3)

    print("Kafka connection failed after retries")


class UserEvent(BaseModel):
    user_id: str
    event_type: str
    page: str
    device: str
    timestamp: str

@app.post("/ingest")
def ingest_event(event: UserEvent):
    if producer:
        producer.send("user-events", event.dict())
        return {"status": "event sent to kafka"}
    else:
        return {"status": "kafka unavailable"}
