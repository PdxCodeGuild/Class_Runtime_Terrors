from django.contrib.auth import get_user_model
from django_filters import rest_framework as df_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets, filters, generics, mixins, status
from rest_framework.authentication import SessionAuthentication
from potty_spotter.core.api.pagination import GlobalPagination
from potty_spotter.apps.user.api import serializers as serializers_user
from potty_spotter.apps.user.permissions import IsSysAdmin

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    permission_classes = [IsSysAdmin]
    pagination_class = GlobalPagination
    authentication_classes = [SessionAuthentication]
    serializer_class = serializers_user.UserSerializer

    def get_queryset(self):
        return super().get_queryset().filter(username=self.request.user.username)
