#!/bin/bash

uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
streamlit run frontend/streamlit_app.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false

wait 