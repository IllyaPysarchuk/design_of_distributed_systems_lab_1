#!/bin/bash
gunicorn --workers 3 --bind 0.0.0.0:5001 provider:provider_app &
gunicorn --workers 3 --bind 0.0.0.0:5000 consumer:consumer_app &
wait # Keep the container running

