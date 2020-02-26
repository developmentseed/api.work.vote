#!/bin/bash
set -e
cmd="$@"

touch config/env/.local

function postgres_ready(){
python << END
import sys
import psycopg2
from urllib.parse import urlparse
try:
    result = urlparse("$DATABASE_URL")
    conn = psycopg2.connect(database=result.path[1:], user=result.username, password=result.password, host=result.hostname)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - trying again..."
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
exec $cmd
