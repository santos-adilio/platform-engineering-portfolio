# 🚀 Identity Validation & Access Control Platform  
### Distributed Authentication & Connection Authorization System

---

## Overview

This project implements a distributed identity validation and access control platform designed to securely authorize client connections before allowing access to a multi-user online service.

The system combines:

- External identity providers (Discord)  
- Network identity (IP address)  
- Optional platform identity (Steam ID)  

to enforce a strong binding between user identity and network location before granting access.

The platform is designed with a focus on:

- Secure authentication workflows  
- Distributed validation across multiple services  
- Protection against unauthorized access and session hijacking  
- Real-time authorization before connection admission  
- Observability and security event logging  

---

## Architecture Summary

High-level system architecture:

```yaml
User (Discord)
|
| Authentication & IP registration
v
+------------------------+
| Discord Bot & Panel |
| Token-based workflow |
+-----------+------------+
|
| Store & query IP bindings
v
+------------------------+
| Whitelist API Layer |
| Token authenticated |
| SQLite / MySQL store |
+-----------+------------+
|
| Validation requests
v
+------------------------+
| Connection Queue & |
| Authorization Layer |
| (Pre-admission gate) |
+-----------+------------+
|
| Authorized / rejected
v
Online Service

```

---

## Core Responsibilities

- Authenticate users via external identity provider (Discord)  
- Generate short-lived authorization tokens for IP registration  
- Bind user identity to one or more allowed IP addresses  
- Validate identity + IP binding before admitting connections  
- Enforce queue-based admission control  
- Log and monitor security events and anomalies  

---

## Authentication & Authorization Flow

### High-Level Connection Flow

```yaml
Client connects
-> Collect identifiers (IP, Discord ID, optional Steam ID)
-> Validate IP against whitelist API
-> Validate Discord identity and registered IPs
-> Confirm IP is bound to the connecting Discord account
-> Enter queue and wait for available slot
-> Authorized to connect or rejected
```


---

### Discord Registration Flow

1. User clicks a Discord bot button to request access.  
2. Bot generates a short-lived registration token (5 minutes).  
3. Bot sends the user a secure panel link containing the token and role context.  
4. User opens the panel and registers the current IP address.  
5. IP and identity are persisted in the whitelist database.  
6. The IP becomes eligible for future connection authorization.  

---

## Core Components

### 1. Connection Queue & Authorization Layer

**Responsibilities:**

- Collect client identifiers (IP, Discord ID, Steam ID, license)  
- Enforce mandatory identity requirements  
- Query whitelist API for authorization checks  
- Control admission using queue scoring and prioritization  
- Block unauthorized clients before connection establishment  
- Emit structured security and audit logs  

**Security features:**

- Rate limiting per IP  
- Brute-force detection  
- Emergency bypass controls  
- Priority roles and VIP handling  

---

### 2. Whitelist & Validation API

REST API responsible for:

- Validating IP authorization  
- Listing registered IPs per user  
- Performing identity-to-IP binding checks  
- Providing auditing and statistics endpoints  

**Authentication model:**

- Token-based authentication  
- Rotation-based API tokens with time tolerance  
- Shared secret between services  

**Data store:**

- SQLite for fast local persistence  
- Optional MySQL / MariaDB backend  
- Schema includes:
  - User identity  
  - IP bindings  
  - Expiration timestamps  
  - Token rotation metadata  

---

### 3. Discord Bot & Registration Panel

Provides the user-facing authentication experience:

- Generates short-lived authorization tokens  
- Creates secure registration links  
- Allows IP registration via web panel  
- Notifies completion events  
- Enforces role-based access control  

---

## Security & Reliability

### Security Features

- Multi-factor identity binding (Discord + IP, optional Steam ID)  
- Short-lived registration tokens  
- Token rotation for API authentication  
- Mandatory identity requirements  
- Rate limiting and brute-force detection  
- Security event logging designed to support external intrusion detection integration  
- Emergency bypass and role-based priority  

---

### Reliability Features

- Distributed validation across independent services  
- Graceful handling of API failures  
- Queue-based admission control  
- Timeout and retry handling  
- Consistent authorization model across services  

---

## Technologies & Stack

- **Runtime:** Lua (server resource), Node.js (API & bot)  
- **Frameworks:** RedM scripting environment, Express  
- **Database:** SQLite (local), MySQL / MariaDB (optional backend)  
- **Authentication:** Token-based, rotation tokens  
- **Integration:** REST APIs, Discord APIs  
- **Security:** IP binding, rate limiting  

---

## Engineering Concepts Demonstrated

- Identity & access management (IAM)  
- Distributed authentication workflows  
- Pre-admission authorization gates  
- Token-based security models  
- Queue-based admission control  
- Brute-force protection and rate limiting  
- Security observability and audit logging  
- Distributed systems integration  

---

## Role & Responsibilities

In this project I was responsible for:

- Designing the full authentication and authorization architecture  
- Defining identity binding and validation workflows  
- Implementing token generation and rotation mechanisms  
- Designing queue-based admission control  
- Integrating Discord authentication and web registration panel  
- Implementing rate limiting, audit logging, and anomaly detection  
- Using AI-assisted development as an acceleration tool, with full ownership of architecture and security design  

---

## Outcomes & Learnings

- Designed a distributed identity validation platform from scratch  
- Implemented secure pre-admission authorization gates  
- Practiced IAM design in a multi-service environment  
- Built token rotation and short-lived credential workflows  
- Gained hands-on experience with security engineering and access control  
- Strengthened platform, reliability, and distributed systems skills  

---

## Future Improvements

- OAuth / OpenID Connect integration  
- JWT-based access tokens  
- Centralized identity provider  
- Persistent audit log storage  
- Metrics export for authorization events  
- High-availability API replication  

---

## License

This project is intended for educational and professional portfolio purposes.


