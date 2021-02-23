from django.urls import path
from . import views

urlpatterns = [
    path("", views.url_home, name="url_home"),
    path("gen/<str:uurl>", views.url_gen, name="url_gen"),
    path("get/<str:suurl>", views.url_get, name="url_get"),
    path("delete/<str:uurl>", views.url_delete, name="url_delete"),
]
