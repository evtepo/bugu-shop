from django.contrib import admin
from article.models import Article, User


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...
