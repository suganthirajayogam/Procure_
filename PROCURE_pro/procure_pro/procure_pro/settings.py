import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # Use SQLite for testing or PostgreSQL for production
        "NAME": os.getenv("DB_NAME", "procore_db"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

INSTALLED_APPS = [
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom apps
    "projects",
]

# Add your SECRET_KEY and other settings
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your_default_secret_key")
DEBUG = True
ALLOWED_HOSTS = []
