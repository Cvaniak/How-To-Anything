#!/bin/sh
python -m pip install debugpy
python -m debugpy --log-to "/temp/logs/" --listen 0.0.0.0:5678 -m uvicorn app-name.app:app --reload --port 8000 --host 0.0.0.0 --workers 1

