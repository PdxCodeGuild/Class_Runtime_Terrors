from django.urls import path
from . import views

urlpatterns = [
    path('', views.ushrink_list, name = 'list'),
]