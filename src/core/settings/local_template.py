"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = ":Q'c5Rz`Vz9#sw6W+kW/MTB$0Dzd<6B);[hMjKywU,OoPdOp1C^77r_sjSGz"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoecomm',
        'USER': 'djangoecomm',
        'PASSWORD': 'djangoecomm',
    }
}

ALLOWED_HOSTS = ["*"]
