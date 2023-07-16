#!/bin/bash

PROCESS_TYPE=$1

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server)"
    exit 1
fi

if [ "$PROCESS_TYPE" = "server" ]; then
    python manage.py runserver \
        0.0.0.0:8000 \
        --no-color
fi
