#!/bin/bash

INITIALIZED='.initialized'
ENV_VARS_FILE="/root/.env.sh"

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

            #load initial data
            echo "Django is loading initial data"
            sh scripts/loaddata.sh

            echo "Setting constance config"
            ./manage.py runscript init_constance

            echo "Crawling latest data for taiex"
            ./manage.py runscript start_taiex_crawler

            echo "Crawling latest data for company"
            ./manage.py runscript start_company_crawler

            echo "Crawling latest data for fundamentals-comprehensive income"
            ./manage.py runscript start_fundamentals_crawler --script-args Income

            echo "Crawling latest data for fundamentals-balance"
            ./manage.py runscript start_fundamentals_crawler --script-args Balance

            echo "Crawling latest data for stock"
            ./manage.py runscript start_stock_crawler

            echo "Crawling latest data for holiday"
            ./manage.py runscript start_holiday_crawler

            echo "Dump data from database"
            sh scripts/dumpdata.sh
            # mark as initialized
            echo "Dumping env variables into ${ENV_VARS_FILE}"
            printenv | sed 's/^\(.*\)$/export \1/g' > ${ENV_VARS_FILE}
            chmod +x ${ENV_VARS_FILE}

            echo "Start crontab"
            crontab /app/cronfile
            cron

            echo "Mark as initialized"
            touch ${INITIALIZED}
        fi
        ;;
esac

exec "$@"
