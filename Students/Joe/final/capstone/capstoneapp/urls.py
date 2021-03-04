from django.urls import path
from . import views
# from .views import hawaiiblog, add


# urlpatterns = [
#     path('', views.hawaiiblog, name='hawaiiblog'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
#     path('delete/<int:id>', views.remove, name = 'remove')
    
# ]

urlpatterns = [
# path('', hawaiiblog.as_view(), name ='hawaiiblog'),
# path('add', add.as_view(), name ='add'),
path('', views.hawaiiblog, name ='hawaiiblog' ),
path('add', views.add, name ='add' ),
path('update/<int:id>', views.update, name ='update' ),
path('delete/<int:id>', views.remove, name ='remove' ),

]