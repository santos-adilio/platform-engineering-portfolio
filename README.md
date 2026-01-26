⭐ Telemetry & Observability Middleware – Architecture Overview
1. Overview

This project implements a production-like telemetry and observability middleware designed to collect, process, and distribute real-time data from a Linux-based online service.

The system receives structured telemetry data via REST, processes and enriches the payload through a modular plugin pipeline, and broadcasts the processed data in real time to connected clients via secure WebSocket connections.
It also exposes a whitelist and control API backed by a relational database to support dashboards, monitoring, auditing, and automation workflows.

The platform is designed with a strong focus on modularity, reliability, security, and extensibility.

2. Architecture Summary

Core responsibilities:

Ingest telemetry data from external services via REST

Process and enrich data using a modular plugin pipeline

Distribute processed data in real time via WebSocket

Expose a secure whitelist API backed by MySQL/MariaDB

Provide health checks, status endpoints, logging, and operational controls

High-level architecture:

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

3. Data Flow

External service sends telemetry data via POST /update using HTTPS and Bearer token authentication.

The middleware validates authentication and performs structural validation.

The payload passes through a configurable plugin pipeline for enrichment, analytics, and anomaly detection.

The processed payload is broadcast in real time to connected WebSocket clients.

Periodic health and status messages are emitted for monitoring purposes.

4. Core Components
Telemetry Server

Node.js + Express + HTTPS

REST ingestion endpoints

WebSocket real-time distribution

Health checks and operational status

Responsibilities:

Authentication and request validation

Plugin execution orchestration

Broadcast to connected clients

Logging and fault handling

Plugin Processing Pipeline

Modular plugin-based architecture where each plugin:

Operates independently

Can validate, transform, enrich, or analyze the payload

Implements caching, fault handling, and execution control

Examples of plugins:

Payload validation

Analytics and metrics enrichment

Simple anomaly detection

Domain-specific processors (environment, users, economy, state)

The architecture supports:

Extensibility

Controlled execution order

Fault isolation

Retry and cooldown mechanisms

Whitelist & Control API

REST API backed by MySQL/MariaDB

Token-based authentication

Supports:

IP validation

User and identity lookup

Statistics and auditing

Access control

Used by dashboards, automation tools, and access validation services.

5. Security & Reliability

Security features:

HTTPS with TLS certificates

Bearer token authentication on REST endpoints

Token-based authentication for WebSocket connections

Centralized configuration validation

Rate limiting and security headers

Reliability features:

Plugin-level fault isolation

Retry logic for transient failures

Structured logging

Health and status endpoints

Connection limits and resource control

6. Technologies & Stack

Runtime: Node.js (16+)

Frameworks: Express, ws (WebSocket)

Database: MySQL / MariaDB

Process management: PM2

Security: HTTPS, Bearer tokens, rate limiting

Integration: REST APIs, WebSocket

Architecture: Modular plugin pipeline, real-time streaming

7. Key Engineering Concepts Demonstrated

Telemetry & observability pipelines

Modular plugin architectures

Real-time data streaming

Fault-tolerant ingestion

Secure API design

Distributed system integration

Operational monitoring and health checks

8. Role & Responsibilities

Designed the full system architecture and data flow

Defined the plugin model and execution pipeline

Implemented authentication and security model

Built ingestion, processing, and real-time distribution layers

Designed reliability mechanisms and operational controls

Used AI-assisted development to accelerate implementation, validating all components for production reliability

9. Outcomes & Learnings

Built a production-like observability pipeline from scratch

Practiced distributed system design and integration

Implemented real-time telemetry and monitoring workflows

Gained hands-on experience with reliability, security, and extensibility patterns

Strengthened platform and infrastructure engineering skills
