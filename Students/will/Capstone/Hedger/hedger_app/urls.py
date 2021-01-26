from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('signup/', views.user_register, name="signup"),
    path('login/', views.login, name="login")
]