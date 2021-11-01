#!/bin/bash

python manage.py collectstatic
python manage.py migrate
python manage.py loaddata ./fixtures/fixtures.json

exec "$@"