Azure AKS Portfolio Demo – Cloud Native Todo App
Overview

This project demonstrates an end-to-end Azure cloud deployment using Kubernetes, CI/CD automation, container registry integration and monitoring.

Goal: prove practical Azure platform engineering skills rather than complex application logic.

Application

Simple Python Flask Todo API with browser UI.

Features:

REST API (/todos, /health)

Web UI for demo purposes

Containerized deployment

Public endpoint via AKS LoadBalancer

screenshots/app-ui.png




CI/CD Pipeline

GitHub Actions pipeline automatically:

Builds container image

Pushes image to Azure Container Registry (ACR)

Deploys updated image to AKS

screenshots/github-actions.png




Kubernetes Deployment (AKS)

Azure Kubernetes Service used for orchestration.

Key aspects:

Deployment + Service configuration

Public LoadBalancer exposure

Rolling updates via CI/CD

Container runtime inside managed cluster

screenshots/aks-workloads.png




Monitoring & Observability

Azure Monitor Container Insights enabled:

Pod/container metrics

Logs via Log Analytics

Cluster health visibility

screenshots/monitoring.png




Architecture Summary

GitHub → CI/CD Pipeline → Azure Container Registry → AKS Deployment → Public Endpoint → Azure Monitor

Skills Demonstrated

Azure:

Azure Kubernetes Service (AKS)

Azure Container Registry (ACR)

Azure Monitor / Log Analytics

DevOps:

GitHub Actions CI/CD

Container image automation

Cloud deployment lifecycle

Cloud Engineering:

Kubernetes operations

Observability setup

Production-style deployment flow

Author

Youssef Tayachi
Azure / Cloud Engineering Portfolio Project
