from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name = 'list'),
    path('add/', views.add_todo, name = 'add'),
    path('details/<int:id>', views.details, name = 'details'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.remove_todo, name = 'remove')
]
