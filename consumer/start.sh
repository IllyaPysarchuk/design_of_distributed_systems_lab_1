#!/bin/bash
gunicorn --workers 3 --bind 0.0.0.0:5000 consumer:consumer_app
