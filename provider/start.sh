#!/bin/bash
gunicorn --workers 3 --bind 0.0.0.0:5001 provider:provider_app

