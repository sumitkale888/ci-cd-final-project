# Accounts Microservice

![Build Status](https://github.com/sumitkale888/ci-cd-final-project/actions/workflows/ci-build.yaml/badge.svg)

IBM DevOps and Software Engineering Capstone project implementing a RESTful Accounts microservice with TDD, CI, security headers, CORS, Docker, Kubernetes, and Tekton.

## REST API
- POST /accounts
- GET /accounts
- GET /accounts/{id}
- PUT /accounts/{id}
- DELETE /accounts/{id}

## Run
```bash
python -m pip install -r requirements.txt
python app.py
```

The service listens on port 8080.

## Test
```bash
nosetests --with-coverage --cover-package=service -v
```
