from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('external/', views.external, name = 'external'),
    path('r_script/', views.r_script),
    path('register/', views.register),
    path('login/', views.login, name='login'),
    path('scan/', views.scan, name='scan'),
    path('logout/', views.logout, name='logout'),
    path('ports/', views.ports, name='ports'),
]