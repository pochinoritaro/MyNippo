from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from config.urls.base import urlpatterns

urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
