from django.urls import path
from . import views
# from Api import views

urlpatterns = [
    
    path('', views.rover, name = 'rover'),
    
    
]