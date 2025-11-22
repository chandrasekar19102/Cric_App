from .base import * # <--- This imports all the common stuff from base.py
from decouple import config # it handles Booleans (True/False) much better than os.getenv
# 1. SECURITY: Insecure key for local work
SECRET_KEY = config('SECRET_KEY')

# 2. SECURITY: Show me all the errors!
DEBUG = config('DEBUG', default=False, cast=bool)

# 3. Allow running on localhost
ALLOWED_HOSTS = ['*']

# 4. Use the simple file-based database for local work
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

