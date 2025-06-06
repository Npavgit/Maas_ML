# ML Inference API with Flask, Docker, and GitHub Actions

This project deploys a machine learning model using a Flask API, containerized with Docker, and uses GitHub Actions for CI/CD.

## Usage

- POST to `/predict` with JSON:
```json
{ "features": [5.1, 3.5, 1.4, 0.2] }
```

## Run Locally
```bash
docker build -t maas-ml-api .
docker run -p 5000:5000 maas-ml-api
```