# mlopsclassactivity1
Building and Orchestrating a Simple ML Pipeline with Docker, Airflow, and Kubernetes


This repository contains a minimal Machine Learning workflow with Docker, designed to help you practice the basics of MLOps, Airflow, and Kubernetes.
Project Structure
mlops-starter/
│── preprocess.py        # Data preprocessing (Iris dataset → CSV)
│── train.py             # Model training (Logistic Regression)
│── app.py               # FastAPI app to serve predictions
│── requirements.txt     # Python dependencies
│── Dockerfile.train     # Dockerfile for preprocessing + training
│── Dockerfile.serve     # Dockerfile for serving the model

**Step 1: Preprocess & Train with Docker
**
Build training image
docker build -f Dockerfile.train -t ml-train .

Run training container
docker run -v $(pwd):/app ml-train

This generates:

cleaned_iris.csv

model.pkl

**Step 2: Serve Model with FastAPI
**
Build serving image
docker build -f Dockerfile.serve -t ml-api .

Run serving container
docker run -p 8000:8000 ml-api


FastAPI server will start at → http://localhost:8000

**Step 3: Test API Endpoint
**
Send a test request:

curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features":[5.1, 3.5, 1.4, 0.2]}'


Expected output:

{"prediction": 0}

**Step 4: Airflow Integration
**
Later, you will write an Airflow DAG (ml_pipeline.py) to automate:

Run preprocess.py

Run train.py

Deploy app.py

The DAG will orchestrate these steps instead of running them manually.

**Step 5: Kubernetes Deployment
**
Once trained, deploy app.py in Kubernetes:

kubectl apply -f k8s-deployment.yaml
kubectl get pods

**Learning Outcomes
**
By using this repo, you will:

Build & run Docker containers for ML workflows

Serve ML models via REST API

Orchestrate pipelines with Airflow

Deploy workloads to Kubernetes
