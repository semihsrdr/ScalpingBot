#!/bin/bash

# --- DEBUGGING START ---
echo "--- DEBUG: Checking environment ---"
echo "--- DEBUG: Python path ---"
which python3
echo "--- DEBUG: Pip path ---"
which pip3
echo "--- DEBUG: Listing installed packages ---"
pip3 list
echo "--- DEBUG: End of environment check ---"
# --- DEBUGGING END ---

# Gunicorn web sunucusunu arka planda başlat
echo "Starting Gunicorn web server in the background..."
gunicorn app:app --bind 0.0.0.0:$PORT &

# Worker sürecini ön planda başlat
echo "Starting worker process in the foreground..."
python3 -u worker.py
