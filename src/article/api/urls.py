from django.urls import include, path


urlpatterns = [
    path("v1/", include("article.api.v1.urls")),
]
