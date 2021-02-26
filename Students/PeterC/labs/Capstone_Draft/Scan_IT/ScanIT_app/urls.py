from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('blabla/', views.whatever, name='hello'),
    # url(r'^blabla$', views.whatever, name='hello'),
]