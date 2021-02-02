from django.urls import path
from . import views

urlpatterns = [
   path('', views.todo_list, name = 'list'),
   path('add/', views.add_todo, name = 'add'),
   path('details/<int:id>', views.details, name = 'details'),
   ]