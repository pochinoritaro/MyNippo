import os

env = os.getenv("DJANGO_ENV", "local")  # デフォルトは local

match env:
    case "prod":
        from .prod import *

    case "dev":
        from .dev import *

    case "local":
        from .local import *

    case _:
        raise
