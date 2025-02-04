import os
from django.core.wsgi import get_wsgi_application

env = os.getenv("DJANGO_ENV", "local")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.{env}')

application = get_wsgi_application()
