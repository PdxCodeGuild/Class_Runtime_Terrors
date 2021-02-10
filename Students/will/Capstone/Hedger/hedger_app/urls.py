from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('signup/', views.user_register, name="signup"),
    path('initial_login/', views.initial_login, name="initial_login"),
    path('login/', views.user_login, name="login"),
    path('api/', views.api, name = 'api'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('rebalance/', views.rebalance, name = 'rebalance'),
    path('logout/', views.user_logout, name = 'logout'),

]