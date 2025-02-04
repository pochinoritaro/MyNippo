import datetime
from pathlib import Path
from config.settings.base import BASE_DIR, LOGGING

today = datetime.date.today().strftime('%Y%m%d')

LOGGING["handlers"] = {
    "file": {
        "level": "INFO",
        "class": "logging.handlers.RotatingFileHandler",
        "filename": Path(BASE_DIR, "logs", f"{today}.log"),
        "maxBytes": 1024 * 1024 * 100,
        "backupCount": 7,
        "formatter": "verbose"
    },
}

LOGGING["loggers"] = {
    "django": {
        "handlers": ["file"],
        "level": "INFO",
        "propagate": True,
    },
}
