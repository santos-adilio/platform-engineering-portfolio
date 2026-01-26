# 🧰 Personal Cloud & Home Lab Platform
### Hybrid On-Prem & Cloud Infrastructure

## 🏗 Overview

This environment simulates production-like infrastructure using virtualization, container platforms, networking, automation, and developer tooling.

## 📌 Architecture

```lua
                    +-------------------+
                    |     Internet      |
                    +---------+---------+
                              |
                        OpenWrt Router
                              |
                     +--------+--------+
                     |      Core LAN   |
                     +--------+--------+
                              |
                   +----------+----------+
                   |      Arista Switch  |
                   |   7050TX-64 (L2/L3) |
                   +----------+----------+
                              |
            +-----------------+-----------------+
            |                                   |
     +------+-------+                   +-------+------+
     |   Proxmox     |                   |  Bare Metal   |
     | Virtualization|                   |  Ubuntu Linux |
     +------+-------+                   +-------+------+
            |                                   |
     +------+-------+                   +-------+------+
     | LXC / QEMU   |                   | Containers /  |
     |   Services   |                   | Native Apps   |
     +------+-------+                   +-------+------+
            |
     +------+-----------------------------------+
     |        Automation · CI · SCM · IoT       |
     +------------------------------------------+

```

---

## Core Objectives

- Simulate production-like infrastructure in a controlled environment  
- Practice virtualization, containerization, and automation workflows  
- Experiment with networking, security, and overlay networking  
- Host internal developer tooling and automation services  
- Validate behavior differences between bare metal and containerized workloads  
- Build a foundation for platform engineering and SRE practices  

---

## Infrastructure Components

### Virtualization Platform

**Hypervisor:** Proxmox (QEMU + LXC)  

- QEMU virtual machines for full OS environments  
- LXC containers for lightweight services  
- High-availability configuration tested previously (currently single-node)  
- Snapshot and rollback workflows used for testing  

---

### Bare Metal Test Host

Dedicated Ubuntu Linux system used to:

- Run services directly on bare metal  
- Compare behavior against containerized deployments  
- Validate performance and system discrepancies  
- Support production-related experiments and client workloads  

Used primarily for professional experimentation and production simulations.

---

## Platform Services

### 🖨 OctoPrint (LXC Container)

- Remote management and monitoring of 3D printer  
- Network-based job submission and control  
- Used to validate device access and service isolation in containers  

---

### 🏠 Home Assistant OS (QEMU VM)

Central automation and IoT control platform:

- Smart plugs, lights, and environmental sensors  
- Temperature and humidity monitoring  
- Infrared remote control integration  
- Automation workflows and device orchestration  
- Real-time state tracking and remote control  

---

### 🔌 Tasmota / TasmoAdmin (LXC Container)

Firmware and device management platform:

- Centralized management of Tasmota-based IoT devices  
- Firmware updates and configuration orchestration  
- Device inventory and lifecycle management  

---

### 🔁 n8n Automation Platform (LXC Container)

Workflow automation and integration engine:

- Event-driven automations  
- Webhook processing  
- Device and service orchestration  
- Integration testing between services  

---

### 🔧 OneDev (LXC Container)

Self-hosted CI / SCM platform:

- Git repository hosting  
- Version control for RedM server scripts and platform tooling  
- CI experimentation and automation pipelines  
- Internal developer platform simulation  

---

## Networking & Security

### Core Network

- **Core switch:** Arista 7050TX-64  
  - High-performance L2/L3 switching  
  - VLAN segmentation and traffic control  

- **Edge router:** Buffalo WXR-5950AX12  
  - Custom firmware based on OpenWrt  
  - NAT, firewall and routing control  

- **Internal router:** Buffalo WRX-1900DHP  
  - Local DHCP and DNS services  
  - Internal service discovery and name resolution  

---

### Overlay Networking (Tailscale)

All critical devices and services are connected via **Tailscale**:

- Servers, desktops, laptops, smartphones, media devices  
- Secure overlay mesh network  
- Always-on remote access independent of physical location  
- Simplified service exposure without public NAT  

Used to:

- Access internal services remotely  
- Test zero-trust networking models  
- Secure management plane access  

---

## Device Ecosystem

Connected devices include:

- Servers and virtualization hosts  
- Bare metal Linux systems  
- Developer workstations  
- Smartphones and tablets  
- Media devices (FireTV, Chromecast)  
- IoT sensors and actuators  

All devices integrated into a unified secure network fabric.

---

## Engineering Concepts Demonstrated

- Hybrid on-prem infrastructure design  
- Virtualization with QEMU and LXC  
- Bare metal vs containerized workload validation  
- Internal developer platform (OneDev)  
- Automation workflows (n8n, Home Assistant)  
- IoT lifecycle and firmware management  
- Advanced networking and routing  
- Overlay networking and zero-trust access  
- Service isolation and resource control  

---

## Role & Responsibilities

In this project I was responsible for:

- Designing the full infrastructure topology  
- Deploying and maintaining virtualization and container platforms  
- Implementing automation and IoT orchestration services  
- Designing networking, routing and segmentation  
- Integrating overlay networking for secure remote access  
- Hosting internal developer tooling and CI experimentation  
- Performing reliability and performance validation across environments  

---

## Outcomes & Learnings

- Built and maintained a production-like hybrid infrastructure  
- Practiced platform engineering and internal tooling deployment  
- Gained hands-on experience with virtualization and container orchestration  
- Implemented automation and IoT management workflows  
- Strengthened networking, security and remote access skills  
- Validated reliability patterns and operational practices  

---

## Future Improvements

- Multi-node Proxmox cluster reintroduction  
- Centralized monitoring and metrics collection  
- Backup automation and disaster recovery testing  
- VLAN segmentation refinement  
- Service mesh and ingress experimentation  
- GitOps-based automation pipelines  

---

## License

This project is intended for educational and professional portfolio purposes.
