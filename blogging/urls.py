from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("api/v1/profiles/", include("apps.profiles.urls", namespace="profiles")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/authors/", include("apps.authors.urls", namespace="authors")),
    path("api/v1/articles/", include("apps.articles.urls", namespace="articles")),
    path("api/v1/search/", include("apps.search.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
