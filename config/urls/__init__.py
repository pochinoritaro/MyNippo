import os

env = os.getenv("DJANGO_ENV", "local")  # デフォルトは local

match env:
    case "prod":
        from .prod import urlpatterns

    case "dev":
        from .dev import urlpatterns

    case "local":
        from .local import urlpatterns

    case _:
        raise
