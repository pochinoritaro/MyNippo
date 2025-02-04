from pathlib import Path
from config.settings.base import BASE_DIR, LOGGING


LOGGING["handlers"] = {
    "file": {
        "level": "INFO",
        "class": "logging.handlers.RotatingFileHandler",
        "filename": Path(BASE_DIR, "logs", "nippo_master.log"),
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
