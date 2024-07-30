from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)
    is_subscriber = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        unique_together = ("title", "author")
