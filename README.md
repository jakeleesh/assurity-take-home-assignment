# Service Reliability Monitor

A lightweight FastAPI service that periodically monitors multiple services, checks their availability and version, and stores results in SQLite. Provides a minimal API for querying services and their health.

---

## Features

- Add services to monitor (name, URL, expected version)
- Periodically check service status, latency, and version
- Store results persistently in SQLite
- Expose a minimal API for service management
- Dockerized for easy deployment

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd svc-reliability
```

### 2. Build and Run with Docker Compose
```bash
docker-compose build
docker-compse up
```

This will:
- Install dependencies inside the container
- Start the FastAPI server
- Create SQLite database file in ./data/data.db
- Start background tasks that check all services periodically

---

### 3. Add Services to Monitor

Use the POST /services endpoint to create services.

```bash
curl -X POST http://localhost:8000/services \
-H "Content-Type: application/json" \
-d '{"name": "Example Service", "url": "https://example.com/health", "expected_version": "1.0"}'
```

---

### 4. List Services

Check all registered services:

```bash
curl http://localhost:8000/services
```