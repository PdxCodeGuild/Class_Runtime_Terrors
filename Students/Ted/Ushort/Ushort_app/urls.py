from django.urls import path
from . import views

app_name = 'Ushort_app'

urlpatterns = [
    path('post/', views.ushrink_post, name = 'post'),
    path('delete/', views.udelete, name = 'delete'),
    path('', views.ushrink_list, name = 'list'),
]