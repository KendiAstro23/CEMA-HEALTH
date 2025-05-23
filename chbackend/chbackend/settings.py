import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'chbackend.urls'


SECRET_KEY = 'e4qat&r5+@*exb6t66ar&0-82xp#%ndp^)j^=l6jul9z-*s6rt'

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # for React communication
    'api',          # my custom app
    "rest_framework_api_key",

]

ALLOWED_HOSTS = ['cema-health-1g0x.onrender.com']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",  
]

DATABASES = {
    'default': dj_database_url.config(default='postgresql://cema_health_pgdb_user:0eV4wWJpi4ABlPegF5DsYlYiKpDZX7Hx@dpg-d073nchr0fns738668ug-a.oregon-postgres.render.com/cema_health_pgdb')
}

DEBUG = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



# TEMPLATES configuration for Django Admin and other templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Optional, if you want to add custom templates
        'APP_DIRS': True,  # Automatically look for templates in each app's 'templates' folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
