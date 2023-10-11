#!/usr/bin/bash

# Before running the app preparing database if needed
python3 /app/src/app.py --prepare-database

# Running the app
python3 /app/src/app.py --csv --json