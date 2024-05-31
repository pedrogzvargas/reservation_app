#!/bin/sh

set -o errexit
set -o nounset

echo "================================================================================================================="
echo "Start app"
echo "================================================================================================================="

alembic upgrade head
python modules/shared/infraestructure/load_passenger_data_to_db.py || echo "Passenger file data already loaded"
uvicorn app.main_app:app --host 0.0.0.0 --reload --port 8000
