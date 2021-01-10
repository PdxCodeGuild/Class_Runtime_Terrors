from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_url, name = 'add_url'),
]