from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('authors/', views.add_authors, name = 'add_authors'),
    path('list/', views.list, name = 'list'),
    path('books/', views.add_books, name = 'add_books'),
    path('details/<int:id>', views.book_details, name = 'details'),
    path('borrow/<int:id>', views.borrow_book, name = 'borrow'),
    path('mybooks/', views.borrowed_books_view, name = 'my_boorowed_books'),
    path('return/<int:id>', views.return_book, name = 'return'),
]