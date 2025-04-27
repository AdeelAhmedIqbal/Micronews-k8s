# Micronews - Kubernetes-Based News Aggregation and Summarization Platform

Micronews is a microservices-based application deployed on Kubernetes. It collects the latest news articles, generates short summaries, and presents them through a simple web interface.

## Project Structure
- **Aggregator Service**: Fetches news articles from NewsAPI.
- **Summarizer Service**: Summarizes article content using Python's Sumy library.
- **Frontend Service**: Displays headlines and summaries to users.
- **Kubernetes Manifests**: YAML files for deploying all services and database.

## Deployment Details
- Kubernetes cluster running on Ubuntu VM.
- Docker images are stored on DockerHub.
- Communication between services is handled through ClusterIP Services.
- Secrets are used to securely manage API keys.

## Repository
This repository contains:
- Source code for aggregator, summarizer, and frontend.
- Dockerfiles for containerization.
- Kubernetes deployment and service manifests.

## Live Testing
Port-forward the frontend service to access the application:
```
kubectl port-forward service/frontend-service 8080:8002
```
Then open [http://localhost:8080](http://localhost:8080) in your browser.
