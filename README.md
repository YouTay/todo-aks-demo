# Azure AKS Portfolio Demo – Todo App

## Overview

This project demonstrates a cloud-native application deployed end-to-end on Microsoft Azure using Kubernetes, CI/CD automation and monitoring.

The goal was not application complexity, but showcasing practical Azure platform engineering skills including containerization, Kubernetes operations and DevOps automation.

---

## Architecture

* Python Flask Todo API with simple web UI
* Containerized application (Docker)
* Azure Container Registry (ACR) for image storage
* Azure Kubernetes Service (AKS) for orchestration
* GitHub Actions CI/CD pipeline
* Azure Monitor / Log Analytics for observability

Deployment flow:

GitHub → Container Build → ACR → AKS Deployment → Public LoadBalancer Endpoint

---

## Key Azure Skills Demonstrated

### Kubernetes / AKS

* Deployment and service configuration
* Rolling updates via CI/CD
* Public service exposure (LoadBalancer)
* Cluster monitoring and diagnostics

### DevOps / CI-CD

* GitHub Actions pipeline:

  * Automated container build
  * Push to Azure Container Registry
  * Automated AKS deployment

### Observability

* Azure Monitor Container Insights enabled
* Centralized container logging
* Metrics visibility for pods and nodes

### Cloud Architecture

* Managed container registry integration
* Kubernetes workload operation
* Infrastructure lifecycle management

---

## Live Application

The app exposes:

* Todo REST API endpoints
* Simple browser UI
* Health endpoint for monitoring readiness

Designed primarily as a Kubernetes/Azure operations showcase.

---

## Lessons Learned

* Azure AKS operational workflows
* CI/CD automation for container workloads
* Monitoring and troubleshooting Kubernetes applications
* Cloud resource cost awareness and lifecycle management

---

## Author

Youssef Tayachi
Azure / Cloud Engineering Portfolio Project
