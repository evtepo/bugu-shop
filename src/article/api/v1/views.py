from django.db import IntegrityError
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from article.api.v1 import serializers
from article.models import Article
from article.permissions import IsAuthor


@extend_schema_view(
    post=extend_schema(
        summary="Create User account",
        description="Create a new user",
    ),
)
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = [AllowAny]


class ArticleMixin:
    serializer_class = serializers.ArticleSerializer


@extend_schema_view(
    get=extend_schema(
        summary="List Articles",
        description="Retrieve a list of all articles",
    ),
    post=extend_schema(
        summary="Create Article",
        description="Create a new article",
    ),
)
class ArticleListCreateView(ArticleMixin, generics.ListAPIView, generics.CreateAPIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAuthor()]

        return [AllowAny()]

    def get_queryset(self):
        query_filter = {"is_public": True}
        user = self.request.user
        if user.is_authenticated:
            is_subscriber = self.request.user.is_subscriber
            if is_subscriber:
                query_filter = {}

        return Article.objects.filter(**query_filter)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response(
                {"detail": "Error creating article. It may be due to a unique constraint."},
                status=status.HTTP_400_BAD_REQUEST,
            )


@extend_schema_view(
    get=extend_schema(
        summary="Retrieve Article",
        description="Retrieve a specific article",
    ),
    put=extend_schema(
        summary="Update Article",
        description="Update a specific article",
    ),
    patch=extend_schema(
        summary="Partially Update Article",
        description="Partially update a specific article",
    ),
    delete=extend_schema(
        summary="Delete Article",
        description="Delete a specific article",
    ),
)
class ArticleRetrieveUpdateDestroyView(ArticleMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        article_id = self.kwargs.get("pk")
        return Article.objects.filter(id=article_id, author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"msg": "The article has been successfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )
