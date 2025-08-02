#  Web Media File Management System

A Python-based system to upload, manage, clean up, and analyze media files (image, video, audio) with security-first design.

---

##  Features

- Upload/download/delete files via REST API (FastAPI)
- Metadata extraction using Visitor pattern
- File cleanup via Strategy pattern (Oldest, Large, etc.)
- STRIDE threat modeling applied for security
- Kubernetes-ready deployment

---

##  Architecture Overview

>  See full documentation in `docs/`

### Class Diagram

![Class Diagram](images/class-diagram.png)

### C4 Container View

![C4 Diagram](images/c4-container-diagram.png)

---

##  Documentation

| Section | Link |
|--------|------|
| Business Requirements | [docs/business-requirements.md](docs/business-requirements.md) |
| Class Diagram | [docs/class-diagram.md](docs/class-diagram.md) |
| C4 Diagrams | [docs/c4-diagram.md](docs/c4-diagram.md) |
| STRIDE Threat Model | [docs/stride-threat-model.md](docs/stride-threat-model.md) |

---

##  How to Run This Web Media File Management System

This section describes how to run the application in various environments:

---

###  1. Local Development (Uvicorn + FastAPI)

####  Prerequisites

- Python 3.10+
- pip
- `virtualenv` (optional but recommended)

#### ▶ Steps

```bash
# 1. (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the FastAPI app
uvicorn main:app --reload
```

Now visit: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs

---

### 🐳 2. Run with Docker
Prerequisites
Docker installed and running

▶ Steps
```bash
# 1. Build Docker image
docker build -t web-media-app .

# 2. Run the container
docker run -d -p 8000:8000 web-media-app
```
Then go to: http://localhost:8000

---

### ☸️ 3. Run with Kubernetes
Prerequisites
Kubernetes cluster (e.g., Minikube or Docker Desktop)

kubectl configured

Docker image built and pushed to DockerHub or used locally with Minikube

▶ Steps
```bash
# 1. (Optional) Enable Minikube Docker environment
minikube start
eval $(minikube docker-env)

# 2. Build Docker image (for local Kubernetes)
docker build -t web-media-app .

# 3. Apply Kubernetes manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml  # Optional if using Ingress
```
Access the app
```bash
minikube service web-media-service
#or
kubectl get svc
#Check your PORT(S) then access http://127.0.0.1:{your_PORT}/docs
```

---
