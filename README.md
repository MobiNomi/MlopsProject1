# 🚀 End-to-End MLOps Pipeline for IMDB Sentiment Analysis


A production-style Machine Learning project demonstrating an end-to-end MLOps workflow using DVC, MLflow, Docker, GitHub Actions, and AWS.


# 📖 Overview

This project demonstrates how a Machine Learning model moves from experimentation to production using modern **MLOps** practices.

The application predicts whether an **IMDB movie review** expresses **positive** or **negative** sentiment while showcasing a complete production pipeline that includes:

* Data Versioning
* Automated Machine Learning Pipeline
* Experiment Tracking
* Model Registry
* Model Promotion
* CI/CD Automation
* Docker Containerization
* Cloud Deployment on AWS

Rather than focusing only on model accuracy, this project emphasizes **building reproducible, scalable, and production-ready ML systems**.

---

# ⭐ Project Highlights

* End-to-End Machine Learning Pipeline
* Data Versioning using DVC
* Experiment Tracking with MLflow (DagsHub)
* Model Registry with Staging → Production workflow
* Automated Model Promotion
* Dockerized Flask Application
* Automated CI Pipeline using GitHub Actions
* Self-Hosted GitHub Runner on AWS EC2
* Cloud Storage using Amazon S3
* Container Registry using Amazon ECR
* Production Deployment on AWS EC2
* Fully Reproducible Workflow

---

# 🏗️ System Architecture

```text
                        +----------------------+
                        |     AWS S3 Dataset   |
                        +----------+-----------+
                                   |
                                   v
                        Data Ingestion (DVC)
                                   |
                                   v
                         Data Preprocessing
                                   |
                                   v
                       Feature Engineering
                                   |
                                   v
                           Model Training
                                   |
                                   v
                         Model Evaluation
                                   |
                                   v
                   MLflow Experiment Tracking
                          (Hosted on DagsHub)
                                   |
                                   v
                         Model Registration
                                   |
                                   v
                    Model Promotion to Production
                                   |
                                   v
                          Docker Image Build
                                   |
                                   v
                          Amazon ECR Repository
                                   |
                                   v
                    Self-Hosted GitHub Runner
                             (AWS EC2)
                                   |
                                   v
                        Flask Web Application
```

---

# 🔄 End-to-End Workflow

## 1. Data Ingestion

* Raw IMDB review dataset is stored in Amazon S3.
* The pipeline automatically downloads the latest dataset.
* DVC tracks every dataset version, ensuring complete reproducibility.

---

## 2. Data Preprocessing

The raw text undergoes several NLP preprocessing steps:

* Lowercase conversion
* HTML removal
* URL removal
* Number removal
* Punctuation removal
* Stopword removal
* Lemmatization

The result is a clean dataset ready for feature engineering.

---

## 3. Feature Engineering

The cleaned reviews are transformed into numerical features using **CountVectorizer (Bag-of-Words)**.

The fitted vectorizer is saved as an artifact to ensure identical preprocessing during inference.

---

## 4. Model Training

The processed data is used to train a sentiment classification model capable of predicting whether a review is:

* Positive
* Negative

Training is fully automated through the DVC pipeline.

---

## 5. Model Evaluation

The trained model is evaluated using standard classification metrics.

Examples include:

* Accuracy
* Precision
* Recall
* F1 Score

Evaluation results are automatically logged to MLflow.

---

## 6. Experiment Tracking

Every training run is recorded in MLflow, including:

* Hyperparameters
* Metrics
* Model Artifacts
* Training Timestamp
* Source Code Version

This makes every experiment completely reproducible.

---

## 7. Model Registry

After successful evaluation, the trained model is registered in the MLflow Model Registry.

The registry provides:

* Versioned Models
* Centralized Model Storage
* Lifecycle Management
* Production Governance

---

## 8. Model Promotion

Instead of automatically replacing the production model, the project follows a controlled promotion workflow.

```
Training
      │
      ▼
Registered Model
      │
      ▼
Staging
      │
      ▼
Production
```

This ensures only approved models reach production.

---

## 9. Docker Containerization

The Flask application is packaged into a Docker image.

Benefits include:

* Reproducible Environment
* Easy Deployment
* Consistent Runtime
* Platform Independence

---

## 10. Continuous Integration

Every push to the **main** branch automatically triggers GitHub Actions.

The CI pipeline performs:

* Checkout Source Code
* Install Dependencies
* Execute DVC Pipeline
* Train Model
* Evaluate Model
* Register Model
* Promote Model

This removes manual intervention and ensures reproducible builds.

---

## 11. Continuous Deployment

After a successful build:

* Docker image is pushed to Amazon ECR.
* The self-hosted GitHub Runner running on AWS EC2 pulls the latest image.
* The old container is stopped.
* A new container is started automatically.

This enables automated deployment with minimal manual effort.

---

# ⚙️ CI/CD Workflow

```text
Developer
      │
      ▼
git push
      │
      ▼
GitHub Actions
      │
      ▼
DVC Pipeline
      │
      ▼
Data Processing
      │
      ▼
Model Training
      │
      ▼
Evaluation
      │
      ▼
MLflow Logging
      │
      ▼
Model Registry
      │
      ▼
Model Promotion
      │
      ▼
Docker Build
      │
      ▼
Amazon ECR
      │
      ▼
Self-Hosted Runner
      │
      ▼
AWS EC2 Deployment
      │
      ▼
Live Flask Application
```

---

# 🛠️ Technology Stack

## Machine Learning

* Python 3.10
* Scikit-Learn
* NLTK
* Pandas
* NumPy

## MLOps

* DVC
* MLflow
* DagsHub

## Backend

* Flask

## DevOps

* Docker
* GitHub Actions

## Cloud

* AWS S3
* AWS ECR
* AWS EC2

---

# 📂 Project Structure

```text
MlopsProject1/
│
├── .github/
│   └── workflows/
│
├── flask_app/
│
├── scripts/
│
├── src/
│   ├── pipeline/
│   ├── features/
│   ├── model/
│   └── connections/
│
├── dvc.yaml
├── dvc.lock
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🚀 Running the Project Locally

## Clone Repository

```bash
git clone https://github.com/MobiNomi/MlopsProject1.git

cd MlopsProject1
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create the required environment variables:

```text
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

S3_BUCKET_NAME

CAPSTONE_TEST
```

---

## Execute the DVC Pipeline

```bash
dvc repro
```

---

## Run the Flask Application

```bash
cd flask_app

python app.py
```

The application will be available at:

```
http://localhost:5000
```

---

# 📊 MLOps Features Implemented

* Data Versioning
* Pipeline Orchestration
* Automated Model Training
* Automated Evaluation
* Experiment Tracking
* Model Registry
* Model Promotion
* Artifact Management
* Containerization
* CI Pipeline
* CD Pipeline
* Cloud Deployment
* Secret Management
* Reproducible ML Workflow

---

# 🎯 Skills Demonstrated

* Machine Learning Engineering
* Natural Language Processing
* MLOps
* Data Versioning
* CI/CD
* Docker
* AWS
* GitHub Actions
* MLflow
* DVC
* Flask
* Cloud Deployment
* Model Lifecycle Management

---

# 📸 Screenshots

> Replace these placeholders with actual screenshots.

### Web Application

```
images/web_app.png
```

### MLflow Experiments

```
images/mlflow_experiments.png
```

### Model Registry

```
images/model_registry.png
```

### GitHub Actions

```
images/github_actions.png
```

### AWS Deployment

```
images/aws_deployment.png
```

---

# 🔮 Future Improvements

* Add comprehensive unit and integration tests
* Implement data drift detection
* Add model performance monitoring
* Introduce automated rollback for failed deployments
* Migrate to MLflow Model Aliases
* Add Kubernetes-based deployment
* Integrate Prometheus and Grafana for monitoring

---

# 👨‍💻 Author

**Mubashir**

**AI Engineer | Machine Learning Engineer | MLOps Enthusiast**

Passionate about building scalable Machine Learning systems, production-ready MLOps pipelines, and cloud-native AI applications.

* GitHub: https://github.com/MobiNomi
* LinkedIn: *Add your LinkedIn profile*
* Portfolio: *Add your portfolio website*

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.
