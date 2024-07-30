from django.contrib.auth.password_validation import validate_password
from django.db.utils import IntegrityError
from django.forms import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response

from article.models import Article, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "password2", "is_author", "is_subscriber")

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError({"Error": "Password mismatch."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get("email"),
            is_author=validated_data.get("is_author"),
            is_subscriber=validated_data.get("is_subscriber"),
        )

        user.set_password(validated_data.get("password"))
        user.save()

        return user


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["author"]

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = self.__get_current_user()
        article = Article.objects.create(author=user, **validated_data)

        return article

    def to_internal_value(self, data):
        wrong_fields = []
        internal_value = super().to_internal_value(data)
        for field in internal_value.keys():
            if field not in data:
                wrong_fields.append(field)

        for field in wrong_fields:
            internal_value.pop(field)

        return internal_value

    def __get_current_user(self):
        return self.context.get("request").user
