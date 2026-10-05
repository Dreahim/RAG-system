#!/bin/bash
set -e

echo "Running database migrations..."
cd /app/models/db_schemes/ragsystem/
alembic upgrade head
cd /app

exec "$@"