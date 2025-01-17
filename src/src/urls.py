from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("admin/", admin.site.urls),
    path("api/", include("article.api.urls")),
]
