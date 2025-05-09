#!/bin/bash
# Full deployment pipeline
set -e

# Backend deployment
echo "Deploying backend..."
render blueprint deploy infrastructure/render/backend.yaml

# Wait for DB to initialize
sleep 15  

# Run migrations
echo "Running migrations..."
render run predictstats-backend -- python manage.py migrate

# Deploy other services
render blueprint deploy infrastructure/render/celery-worker.yaml
render blueprint deploy infrastructure/render/frontend.yaml

echo "Deployment complete! Services:"
render services list
