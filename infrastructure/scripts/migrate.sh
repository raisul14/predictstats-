#!/bin/bash
# Manual migration runner
render run predictstats-backend -- python manage.py migrate
