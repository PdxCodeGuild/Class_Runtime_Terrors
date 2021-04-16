from django.urls import path
from . import views

app_name = 'Ushort_app'

urlpatterns = [
    path('', views.ushrink_list, name = 'list'),
    path('post', views.ushrink_post, name = 'post')
    
]