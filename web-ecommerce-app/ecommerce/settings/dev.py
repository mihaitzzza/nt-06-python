from ecommerce.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

LOCALHOST_DOMAIN = 'http://localhost:8000'
