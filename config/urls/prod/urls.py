from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from config.urls.base import urlpatterns

# TODO: 環境切り分けテスト用の記入であるため、「 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)」は要修正
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
