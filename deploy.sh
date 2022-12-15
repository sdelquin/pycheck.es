#!/bin/bash

source ~/.pyenv/versions/pycheck.es/bin/activate
cd "$(dirname "$0")"
git pull
pip install -r requirements.txt
npm install --prefix assets/static/assets
python manage.py collectstatic --no-input
supervisorctl restart pycheck.es
