DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Optional: override DB settings or secret key if needed
# SECRET_KEY = 'your-dev-secret-key'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Enable debugging in local development
DEBUG = True
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Set allowed hosts for local development
ALLOWED_HOSTS = []  # You can leave this empty for development

# Optionally, you can override the database settings for local development if needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
