from config.settings.base import LOGGING


LOGGING["handlers"] = {
    "console": {
        "level": "DEBUG",
        "class": "logging.StreamHandler",
        "formatter": "verbose"
    }
}

LOGGING["loggers"] = {
    "django": {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": True
    },

    "account": {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": True
    },
    
    "task": {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": True
    },
}
