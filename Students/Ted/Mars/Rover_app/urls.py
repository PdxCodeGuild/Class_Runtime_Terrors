from django.urls import path
from . import views
# from Api import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('roverlook/', views.rover, name = 'rover'),
    
    
]