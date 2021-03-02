from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from potty_spotter.apps.user.api import views


router = routers.DefaultRouter(trailing_slash=True)
router.register(r"", views.UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
