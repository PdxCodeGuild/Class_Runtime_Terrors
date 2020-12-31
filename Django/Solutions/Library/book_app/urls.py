from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('authors/', views.add_authors, name = 'add_authors'),
    path('list/', views.list, name = 'list'),
    path('books/', views.add_books, name = 'add_books')
]