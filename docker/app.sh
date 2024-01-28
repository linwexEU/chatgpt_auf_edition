#!/bin/bash

alembic upgrade head 

gunicorn main:app --workers=1 --timeout 1200 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
