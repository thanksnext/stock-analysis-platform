#!/bin/bash

INITIALIZED='.initialized'
# ENV_VARS_FILE="/root/.env.sh"

case "$1" in ('uwsgi')
        if [ ! -f ${INITIALIZED} ]; then
            echo "Waiting for database..."
            while ! nc -z $POSTGRESQL_HOST $POSTGRESQL_PORT; do
            sleep 0.1
            done
            echo "Database started"

            echo "Initial steps"

            # collect static files into staticfile directory
            echo "Collect static files"
            ./manage.py collectstatic --no-input

            echo "Django is migrating the database"
            ./manage.py migrate --no-input

            # mark as initialized

            # echo "Dumping env variables into ${ENV_VARS_FILE}"
            # printenv | sed 's/^\(.*\)$/export \1/g' > ${ENV_VARS_FILE}
            # chmod +x ${ENV_VARS_FILE}

            # echo "Start crontab"
            # crontab /app/cronfile
            # cron

            echo "Setting Celery"
            celery -A finance worker -B

            echo "Mark as initialized"
            touch ${INITIALIZED}
        fi
        ;;
esac

exec "$@"
