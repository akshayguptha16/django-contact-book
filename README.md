# Django Contact Book

A full-stack contact management web application built with Django and PostgreSQL.

## Live Demo
https://django-contact-book.onrender.com

## Features
- Add, view, edit, and delete contacts
- REST API endpoints for all CRUD operations
- Bootstrap responsive UI
- PostgreSQL database
- Django admin panel
- Deployed on Render

## Tech Stack
- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL
- Bootstrap 5
- Gunicorn
- Whitenoise
- Render (deployment)

## API Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/contacts/ | List all contacts |
| POST | /api/contacts/ | Create new contact |
| GET | /api/contacts/<id>/ | Get single contact |
| PUT | /api/contacts/<id>/ | Update contact |
| DELETE | /api/contacts/<id>/ | Delete contact |

## Local Setup
```bash
git clone https://github.com/akshayguptha16/django-contact-book.git
cd django-contact-book
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## What I learned
- Django MVT architecture
- Django ORM and database migrations
- Django REST Framework and API development
- PostgreSQL integration
- Production deployment with Gunicorn and Whitenoise
