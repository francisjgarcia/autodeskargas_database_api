#!/bin/bash

# Bash options
set -o errexit
set -o pipefail
set -o nounset

# Run migrations
python manage.py makemigrations database
python manage.py migrate
python manage.py loaddata initial_data.json

# Run server
exec "$@"
