#!/usr/bin/bash

source ./.venv/bin/activate


PYTHONPATH="${PYTHONPATH}:$0/src/"
python3 src/app.py