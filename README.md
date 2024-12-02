# Deploying-Machine-Learning-Models-in-Cloud-Docker-Kubernetes-
This project demonstrates how to train a machine learning model, containerize it using Docker, and deploy it as a REST API with Flask. It is designed to showcase the practical application of machine learning in real-world scenarios by providing a scalable and easily deployable solution.


# ML Model API Deployment

## Features
- Train a simple linear regression model.
- Serve predictions via a REST API.
- Containerized using Docker for scalability and easy deployment.

## File Structure
- `app.py`: Main application file for the Flask API.
- `model.py`: Script to train the ML model.
- `model.pkl`: Pre-trained model file.
- `requirements.txt`: List of dependencies.
- `Dockerfile`: Configuration file for building the Docker image.

## Prerequisites
- Python 3.9+
- Docker installed on your system
- Basic knowledge of Flask and Docker

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
