# Real-Time User Analytics Platform

A real-time user analytics system built using **FastAPI, Apache Kafka, TimescaleDB, Docker, and Grafana**.
This project simulates user activity events, processes them through a streaming pipeline, stores them efficiently, and visualizes metrics in real time.

---

## Project Overview

This system captures user interaction events (clicks, page views, etc.) and processes them in real time using an event-driven architecture.

### Key capabilities:
- Real-time event ingestion
- Kafka-based streaming pipeline
- Time-series optimized storage
- Live dashboards & alerts
- Fully containerized microservices

---

## Architecture
Event Generator -> Ingest Service (FastAPI) -> Kafka Topic -> Consumer Service -> TimescaleDB -> Grafana Dashboard

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/0f130540-ee87-4ca4-b0db-7a65bee70985" />

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| API | FastAPI |
| Messaging | Apache Kafka |
| Database | TimescaleDB (PostgreSQL) |
| Visualization | Grafana |
| Containerization | Docker & Docker Compose |
| Language | Python |

---

## 📁 Repository Structure

```
real_time_user_analytics/
├── ingest_service/ # FastAPI event ingestion service
├── consumer_service/ # Kafka consumer → TimescaleDB
├── event_generator/ # Simulated user activity producer
├── dashboard/ # Grafana dashboards & configs
├── docker-compose.yml # Multi-container orchestration
├── README.md
└── .gitignore
```

## 📊 Features Implemented

- Real-time event ingestion via REST API
- Kafka-based event streaming
- Time-bucketed analytics with TimescaleDB
- Live Grafana dashboards:
- Event rate over time
- Event type comparison
- Hourly traffic analysis
- Fully automated event generation
- Dockerized end-to-end system

## 🎯 Skills Demonstrated

- Data Engineering & Streaming Systems
- Microservices Architecture
- Kafka Producers & Consumers
- Time-series data modeling
- Observability & dashboards
- Docker & deployment workflows

## 👩‍💻 Author

Nithyashree
Software Engineering
