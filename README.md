# django_game_library

A small Django project for cataloging video games, studios, and user profiles. Includes an app `games` with models, views, templates, and media handling.

**Prerequisites**
- Python 3.10+ (or your project's Python version)
- pip
- virtualenv (recommended)

**Quick setup**
1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create and apply migrations:

```bash
python manage.py migrate
```

4. (Optional) Load seed data if available:

```bash
python manage.py loaddata
# or run any custom seed command if provided
```

**Run development server**

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

**Media & Static files**
- Static files are in the `static/` directory; run `collectstatic` for production:

```bash
python manage.py collectstatic
```

- Uploaded media is stored in `media/` during development.