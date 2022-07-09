from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("api/v1/profiles/", include("apps.profiles.urls", namespace="profiles")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
