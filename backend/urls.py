from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .api import api

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('accounts/', include('backend.accounts.urls')),  # sem namespace
    path('call/', include('backend.call.urls', namespace='call')),
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
