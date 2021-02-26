from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

password_urls = [
    path('change/', views.change_password, name="pw-change"),
]

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.new_user, name='signup'),
    path('password/', include(password_urls)),
]