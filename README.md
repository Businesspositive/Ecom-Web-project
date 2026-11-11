
# E-commerce Web Application

A Django-based e-commerce application supporting product
browsing, category filtering, user registration, authentication,
shopping cart, customer profiles and order management.

## Technology Stack

- Python 3.10
- Django 4.0.6
- SQLite
- Pillow
- HTML, CSS, JavaScript
- Bootstrap

## Project Structure

- `Ecom/`: Django project configuration
- `app/`: Main application
- `app/models.py`: Database models
- `app/views.py`: Application views and business logic
- `app/forms.py`: Forms and validation
- `app/urls.py`: Application URL routing
- `app/templates/`: HTML templates
- `app/static/`: CSS, JavaScript and static images
- `app/migrations/`: Database migrations
- `media/`: Uploaded product images

## Prerequisites

- Python 3.10
- pip

## Local Setup

Create a virtual environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Run Django system checks:

```bash
python manage.py check
```

Start the development server:

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## Tests

Run the automated test suite:

```bash
python manage.py test
```

## Database

The application uses SQLite by default.

The database is created automatically when migrations are
applied. Existing product data can be loaded from fixtures
when provided.

## Development Notes

This repository preserves the existing application structure
and migration history.

Behavioural changes should be introduced through isolated
changes with corresponding regression tests.

The current dependency versions reproduce the legacy
development environment and are not a production deployment
recommendation.
