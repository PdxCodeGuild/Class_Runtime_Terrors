from django.urls import path
from . import views

urlpatterns = [
    path("", views.shorten_url, name="index"),
    path("u/<str:slugs>", views.urlRedirect, name="redirect")

]
