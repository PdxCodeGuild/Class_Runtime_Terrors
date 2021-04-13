from django.urls import path, include
from . import views
app_name = 'tododjangoAPP'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/', views.add, name = 'item')
    path('detail/<int:todo_item_id>/', views.detail, name='detail')
]