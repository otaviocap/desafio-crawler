#!/usr/bin/bash

source ./.venv/bin/activate

PYTHONPATH="$(dirname "$0")/src"

python3 src/app.py --prepare-database