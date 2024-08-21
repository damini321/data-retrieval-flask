# Flask Data Retrieval and Processing System

## Overview

This Flask application simulates a data retrieval and processing system with two main API endpoints:

    'GET /fetch-data' : Simulates fetching data from an external service and processes it.
    'GET /get-processed-data' : Retrieves the processed data stored in memory.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/damini321/data-retrieval-flask>
   cd flask_app

2. **Set up a virtual environment:**
    python -m venv venv
    venv/bin/activate 

3. **Install dependencies:**
    pip install -r requirements.txt

4. **Run the application:**
    python run.py

5. **Access the API endpoints:**
    'GET /fetch-data' : Fetches and processes mock data.
    Example: http://127.0.0.1:5000/fetch-data
    GET /get-processed-data: Retrieves the processed data.
    Example: http://127.0.0.1:5000/get-processed-data

6. **Testing**
    Run the tests using:
    python -m unittest discover -s tests

