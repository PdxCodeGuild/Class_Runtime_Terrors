from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/', views.TodoView, basename="ApiTodos")

urlpatterns = [
    path('api/', views.TodoView.as_view()),
    path('add/', views.add_todo, name="add"),
    path('details/<int:id>', views.details, name="details"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.remove_todo, name="remove"),
    path('', views.todo_list, name="list"),
]