from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('dashboard/', views.dashboard, name='dashboard'),
path('create-album/', views.createAlbum, name="create"),
path('view-collections/', views.viewCollections, name="view-collections"),
path('collection-details/<int:id>', views.collectionDetails, name ='collection-details' ),
path('delete_album/<int:id>', views.delete_album, name = 'delete_album'),
path('add-images/<int:id>', views.addImages, name = 'add-images'),

]