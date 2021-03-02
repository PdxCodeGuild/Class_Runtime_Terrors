from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from potty_spotter.root.api import views


router = routers.DefaultRouter(trailing_slash=True)

router.register(r"update-logo", views.UpdateLogoViewSet,
                basename="update_logo")
router.register(
    r"update-general-settings",
    views.UpdateGeneralSettingsViewSet,
    basename="update_general_settings",
)


urlpatterns = [
    path("", include(router.urls)),
]
