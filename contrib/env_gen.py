#!/usr/bin/env python
# python contrib/env_gen.py
"""
Django .env generator.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
SECRETY_KEY=%s
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1, 0.0.0.0
DATABASE_URL=postgres://postgres:postgres@db:5437/planilha

#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=planilha
""".strip() % get_random_string(
    50, chars
)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
