#!/usr/bin/env python
"""
Django and Db .env generator.
"""
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

DJANGO_ENVS = """
SECRET_KEY=%s
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1, 0.0.0.0
DATABASE_URL=postgres://postgres:postgres@db:5432/planilha

#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
""".strip() % get_random_string(
    50, chars
)

DB_ENVS = """\
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=planilha
"""

# Writing our configuration file to '.env'
with open('.env', 'w') as env_django:
    env_django.write(DJANGO_ENVS)

# Writing our configuration file to '.env'
with open('db.env', 'w') as env_db:
    env_db.write(DB_ENVS)
