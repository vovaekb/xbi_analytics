# xbi_analytics
Django application with dashboard for XBI Analytics. For dashboard [devexpress widgets](https://js.devexpress.com) are used.

## Install
Prerequisities:

- PostgreSQL
- Django

Install all required packages

```bash
pip install -r requirements.txt
```
### Prepare database
First apply the migration from data model:

```bash
python manage.py migrate
```

Then populate the database from CSV files:
```bash
python manage.py populate_db
```

## Start application
Start app:

```bash
python manage.py runserver
```
Open url http://127.0.0.1:8000/dashboard/ in browser.

## Demo on Heroku
Demo application available on Heroku: https://xbianalytics.herokuapp.com/dashboard/
