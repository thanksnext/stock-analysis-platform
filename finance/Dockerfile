FROM python:3.8
LABEL maintainer "Kent Chen <N96061216@gs.ncku.edu.tw>"
ENV PYTHONUNBUFFERED 1

WORKDIR /app

EXPOSE 8000

# ENTRYPOINT ["./docker-entrypoint-init.sh"]
ENTRYPOINT ["./docker-entrypoint.sh"]

# Setting uwsgi with config file
CMD ["uwsgi", "--ini", "uwsgi.ini"]

# copy and install packages
COPY . .


# Installing dependencies
RUN apt-get update -y \
    && apt-get install cron -y -qq\
    && apt-get install -y gettext \
    && apt-get install -y netcat \
    && pip install --upgrade pip pipenv \
    && pipenv install --system --deploy \
    && rm -rf /var/cache/apt \
    && rm -rf ${HOME}/.cache/
