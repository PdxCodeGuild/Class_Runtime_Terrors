from django.urls import path, include
from potty_spotter.apps.member import views as views_member

app_name = "member"

urlpatterns = [
    path("dashboard/", views_member.DashboardView.as_view(), name="dashboard"),
]
