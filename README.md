# 🚀 Telemetry & Observability Middleware  
**Real-time Data Ingestion & Streaming Platform**

## Overview

This project implements a production-grade telemetry and observability middleware designed to collect, process, and distribute real-time data from a Linux-based online service.

The platform:

- Ingests structured telemetry via secure REST endpoints  
- Processes and enriches data through a modular plugin pipeline  
- Broadcasts the processed payload in real time to connected clients via **WebSocket**  
- Exposes a secure whitelist and control API backed by a relational database to support dashboards, monitoring, auditing, and automation workflows

**Core design focus:**

- Modularity and extensibility  
- Fault tolerance and reliability  
- Security and access control  
- Real-time data streaming  
- Operational observability

## High-level Architecture
```sql
External Service
      |
      |  HTTPS REST (Bearer token)
      v
+-----------------------+
|   Telemetry Middleware|
|  Express + WebSocket  |
|  Plugin Pipeline      |
+----+-------------+---+
     |             |
     |             |  WebSocket broadcast
     v             v
Whitelist API   Dashboards / Clients
(MySQL)         (Realtime consumers)
```
- Ingest telemetry from external services via REST  
- Authenticate and validate incoming payloads  
- Process and enrich data using a configurable plugin pipeline  
- Broadcast processed data in real time via WebSocket  
- Expose whitelist and control APIs (MySQL/MariaDB backed)  
- Provide health checks, status endpoints, structured logging, and operational controls

## Data Flow

1. External service sends telemetry via `POST /update` (HTTPS + Bearer token)  
2. Middleware validates authentication and payload structure  
3. Payload passes through the configurable plugin pipeline for enrichment, analytics, anomaly detection, etc.  
4. Processed payload is broadcast in real time to all connected WebSocket clients  
5. Periodic health and status messages are emitted for monitoring

## Core Components

### 1. Telemetry Server

- **Stack**: Node.js, Express, HTTPS, ws (WebSocket)  
- REST ingestion endpoints  
- Real-time WebSocket distribution  
- Token-based authentication & validation  
- Plugin execution orchestration  
- Structured logging and fault handling  
- Health & status endpoints

### 2. Plugin Processing Pipeline

Modular plugin-based architecture where each plugin:

- Runs independently  
- Can validate, transform, enrich, or analyze payloads  
- Implements its own caching and fault handling  
- Can be enabled/disabled dynamically

**Example plugins:**

- Payload validation  
- Analytics & metrics enrichment  
- Basic anomaly detection  
- Domain-specific processors (environment, users, economy, state, …)

**Features:**

- Controlled execution order  
- Per-plugin fault isolation  
- Retry and cooldown mechanisms  
- Extensible design

### 3. Whitelist & Control API

REST API backed by MySQL/MariaDB providing:

- IP-based validation  
- User/identity lookup  
- Statistics and audit trails  
- Access control for dashboards and automation

## Security & Reliability

**Security Features**

- HTTPS with TLS certificates  
- Bearer token authentication (REST)  
- Token-based authentication (WebSocket via query string)  
- Rate limiting  
- Security headers  
- Centralized configuration validation

**Reliability Features**

- Plugin-level fault isolation  
- Retry logic for transient failures  
- Structured logging  
- Health & status endpoints  
- Connection limits and resource controls

## REST API – Main Endpoints

| Method | Endpoint     | Description                            |
|--------|--------------|----------------------------------------|
| POST   | `/update`    | Ingest telemetry payload               |
| GET    | `/health`    | Basic health check                     |
| GET    | `/status`    | Detailed status (plugins, connections) |
| POST   | `/command`   | Send commands to external service      |

**Authentication:** `Authorization: Bearer <TOKEN>`

## WebSocket

- **Path**: `/data/` (configurable)  
- **Authentication**: token passed via query string  
- **Message Types**:
  - `init`   – connection initialized  
  - `data`   – processed telemetry payload  
  - `health` – periodic middleware health status

## Configuration (Environment Variables – main ones)
```nginx
- `PORT`  
- `DATALOAD_ENDPOINT`  
- `DATALOAD_TOKEN`  
- `WEBSOCKET_PATH`  
- `SSL_CERT_PATH` / `SSL_KEY_PATH`  
- `WHITELIST_DB_HOST`, `WHITELIST_DB_PORT`, `WHITELIST_DB_USER`, `WHITELIST_DB_PASS`, `WHITELIST_DB_NAME`  
- `PLUGINS_ENABLED`  
- `HEALTH_INTERVAL`  
- `MAX_CONNECTIONS`
```
Config file: `.env`

## Runtime & Operations

- Process management with **PM2**  
- Start/stop scripts  
- Locally managed HTTPS certificates  
- Health checks and status endpoints for monitoring integration

## Tech Stack

- **Runtime**: Node.js 16+  
- **Frameworks**: Express, ws  
- **Database**: MySQL / MariaDB  
- **Process Manager**: PM2  
- **Security**: HTTPS, Bearer tokens, rate limiting  
- **Integration**: REST APIs + WebSocket  
- **Architecture**: Modular plugin pipeline + real-time streaming

## Engineering Concepts Demonstrated

- Telemetry & observability pipelines  
- Modular plugin architectures  
- Real-time data streaming  
- Fault-tolerant ingestion & processing  
- Secure API design  
- Distributed system integration  
- Operational monitoring and health checks

## My Role & Responsibilities

- Full system architecture and data flow design  
- Definition of plugin model and execution pipeline  
- Implementation of authentication and security model  
- Development of ingestion, processing, and real-time distribution layers  
- Design of reliability mechanisms and operational controls  
- AI-assisted development (with full production-grade validation of all components)

## Outcomes & Learnings

- Built a production-like observability pipeline from scratch  
- Practiced distributed systems design and integration  
- Implemented real-time telemetry and monitoring workflows  
- Designed fault-tolerant ingestion and processing pipelines  
- Strengthened platform, infrastructure, and reliability engineering skills

## Planned Future Improvements

- Message queue integration (Kafka / RabbitMQ)  
- Persistent storage for historical telemetry  
- Metrics export (Prometheus format)  
- OAuth / JWT authentication  
- Horizontal scaling with load balancing

## License

This project is intended for educational and portfolio purposes only.
