from django.urls import path

from article.api.v1 import views


urlpatterns = [
    path("user/", views.UserRegistrationView.as_view()),
    path("article/", views.ArticleListCreateView.as_view()),
    path("article/<int:pk>", views.ArticleRetrieveUpdateDestroyView.as_view()),
]
