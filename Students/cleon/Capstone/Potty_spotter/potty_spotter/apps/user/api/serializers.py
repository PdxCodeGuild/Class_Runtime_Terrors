from django.contrib.auth import get_user_model
from rest_framework import serializers
from potty_spotter.core.api.serializers import DynamicFieldsModelSerializer

User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "email", "css_theme_preference"]
