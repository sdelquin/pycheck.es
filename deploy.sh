#!/bin/bash

source ~/.pyenv/versions/pycheck.es/bin/activate
cd "$(dirname "$0")"
git pull
pip install -r requirements.txt
supervisorctl restart pycheck.es
