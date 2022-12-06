#!/bin/bash

cd "$(dirname "$0")"
source ~/.pyenv/versions/pycheck.es/bin/activate
exec gunicorn -b unix:/tmp/pycheck.es.sock main.wsgi:application
