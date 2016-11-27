"""
Django settings for frontend project.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 's#erk%h1$2+4$(e@as_#c7ap2!fithwcq!^$y)wg5@7$@wk)-g'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['django.contrib.staticfiles']
ROOT_URLCONF = 'frontend.urls'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend', 'static')]
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'frontend', 'templates')],
}]
WSGI_APPLICATION = 'frontend.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False
STATIC_URL = '/static/'
