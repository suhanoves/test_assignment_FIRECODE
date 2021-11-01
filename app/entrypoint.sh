#!/bin/bash

python manage.py migrate
python manage.py loaddata ./fixtures/fixtures.json

exec "$@"