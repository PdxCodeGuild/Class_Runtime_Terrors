from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.rockhound_list, name='rockhound-site-list'),
    path('site/<slug:slug>', views.site_detail, name='rockhound-site-detail'),
    path('create/', views.createSite, name='rockhound-create'),
]