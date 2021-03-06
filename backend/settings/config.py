""" Settings """
import os
import dj_database_url
from decouple import config, Csv

os.environ.setdefault("DJANGO_DEBUG", "0")
os.environ.setdefault("DJANGO_ALLOWED_HOSTS", "*")
os.environ.setdefault("DJANGO_SECRET_KEY", "DevSecret")

# Set DATABASE_URL in env to override (tests, heroku)
docker_db = "postgres://postgres@db:5432/recordbindb"
os.environ.setdefault("DATABASE_URL", docker_db)

# See Docker for defaults
DEBUG = config("DJANGO_DEBUG", cast=bool)
SECRET_KEY = config("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())

# DATABASE
DATABASE_URL = config("DATABASE_URL")
db_config = dj_database_url.config(default=DATABASE_URL)
DATABASES = {"default": db_config}  # Django DATABASES

# CORS
CORS_ORIGIN_ALLOW_ALL = config("DJANGO_CORS_ORIGIN_ALLOW_ALL", cast=bool, default=False)
CORS_ORIGIN_WHITELIST = [
    'recordbin.co',
    'www.recordbin.co',
    *config("DJANGO_CORS_ORIGIN_WHITELIST", cast=Csv(), default='')
]

if DEBUG:
    CORS_ORIGIN_WHITELIST.append('localhost:8080')

# Security
# https://github.com/rdegges/django-sslify
if not DEBUG:
    SECURE_SSL_REDIRECT = config('DJANGO_SECURE_SSL_REDIRECT', cast=bool, default=True)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# print(f"------------------------------------")
# print(f"DEBUG IS: {DEBUG}")
# print(f"ALLOWED_HOSTS IS: {ALLOWED_HOSTS}")
# print(f"SECRET_KEY IS: {SECRET_KEY[:5]}... (truncated)")
# print("DATABASE CONFIG: {USER}@{HOST}:{PORT}/{NAME} ".format(**db_config))
# print(f"------------------------------------")
