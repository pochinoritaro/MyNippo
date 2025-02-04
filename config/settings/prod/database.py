from pathlib import Path
from config.settings.base import BASE_DIR


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(BASE_DIR, "db.sqlite3"),
    }
}
