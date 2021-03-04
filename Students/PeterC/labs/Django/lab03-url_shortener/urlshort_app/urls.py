from django.urls import path
from . import views

urlpatterns = [
path('', views.url_choice, name = 'choice'),
path('show', views.show, name = 'show'),
path('add', views.add, name = 'add'),
path('delete/<int:id>', views.delete, name = 'delete')
]