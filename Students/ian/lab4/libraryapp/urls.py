from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "sign in for books"
admin.site.site_title = "Library login"
admin.site.index_title = "homei"
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]
