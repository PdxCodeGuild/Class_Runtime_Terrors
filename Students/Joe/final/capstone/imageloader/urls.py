from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name ='home' ),
path('create', views.createAlbum, name ='create' ),
path ('details/<int:id>', views.details, name ='details'),
path ('search', views.search, name ='search'),
path ('display', views.display, name ='display')

]