# xbi_analytics

description

## Install
Prerequisities:

- PostgreSQL
- Django

Install all required packages

```bash
pip install -r requirements.txt
```

Pupulate the database from CSV files:
```bash
python manage.py populate_db
```

## Start application
Start app:

```bash
python manage.py runserver
```
Open url http://127.0.0.1:8000/dashboard/ in browser.
