import os
from django.core.asgi import get_asgi_application

env = os.getenv("DJANGO_ENV", "local")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.{env}')

application = get_asgi_application()
