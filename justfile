default: dev

[private]
[macos]
db:
    #!/bin/bash
    pid=$(ps aux | grep -v grep | grep -ci postgres)
    if [ $pid -eq 0 ]; then
        echo "Launching PostgreSQL..."
        open /Applications/Postgres.app
    fi

[private]
[no-exit-message]
[linux]
db:
    #!/bin/bash
    pid=$(ps aux | grep -v grep | grep -ci postgres)
    if [ $pid -eq 0 ]; then
        echo "PostgreSQL seems to be down!"
        exit 1
    fi

dev: db
    ./manage.py runserver

deploy:
    #!/bin/bash
    source ~/.pyenv/versions/pycheck.es/bin/activate
    git pull
    pip install -r requirements.txt
    npm install
    python manage.py migrate
    python manage.py collectstatic --no-input
    supervisorctl restart pycheck.es

run:
    #!/bin/bash
    source ~/.pyenv/versions/pycheck.es/bin/activate
    exec gunicorn -b unix:/tmp/pycheck.es.sock main.wsgi:application
