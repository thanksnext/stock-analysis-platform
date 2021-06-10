# Fianacial Platform

## About
A platform analyzing Stock market in Taiwan. So far we have some crawler, such as:
* Listed company crawler
* Taiex index crawler
* Balance sheet crawler
* Comprehensive income crawler
* Individual stocks crawler(900+ companies)

## Project
* /data
    * Raw data
    * Logs
* /deployment
    * Docker-compose file
    * Docker file
    * Make file
* /documents
    * Swagger file: Record api spec
* /finance
    * main apps: Django framwork
## Beginners Guide
### User
If you are a user, please install [Docker](https://www.docker.com/) for deploying the system.
### Developer
If you are a developer, you need to install the software as follow:
* Python 3.8
## Deployment
In **/depolyment**,
Initializing the develop environment.
```bash=
make init
```
Deploying the system.
```bash=
make start
```
Stopping the system and delete all dependency.
```bash=
make stop
```
Entry ssh-backend
```bash=
make ssh-backend
```
Entry ssh-database
```bash=
make ssh-database
```

## Crawler
If you want to trigger crawler manually, here is the method of crawling in **/finance**.
### Taiex crawler
```bash=
python manage.py runscript start_taiex_crawler
```
### Listed company crawler
```bash=
python manage.py runscript start_company_crawler
```
### Balance sheet crawler
```bash=
python manage.py runscript start_fundamentals_crawler --script-args Balance
```
### Comprehensive income crawler
```bash=
python manage.py runscript start_fundamentals_crawler --script-args Income
```
### Individual stocks crawler
```bash=
python manage.py runscript start_stock_crawler
```

## Django
### Create super user
```bash=
python manage.py createsuperuser --email <email> --username <name>
```
### Run Server
```bash=
python manage.py runserver
```
###### tags: `finance` `stock` `python` `django`
