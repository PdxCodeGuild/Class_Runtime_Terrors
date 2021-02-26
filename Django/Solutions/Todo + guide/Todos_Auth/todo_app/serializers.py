from rest_framework import serializers
from .models import Todo

class TodoSerializer (serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
      return obj.user.username
    class Meta:
        model= Todo
        fields = ['title', 'text','status', 'id', 'user']