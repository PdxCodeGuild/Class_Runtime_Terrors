from django.urls import path, include
from . import views  

urlpatterns = [
    path('crystal/', views.CrystalList.as_view(), name='compendium-crystal-list'),
    path('crystal/create', views.CrystalCreate.as_view(), name='compendium-crystal-create'),
    path('crystal/<slug:slug>', views.crystal_detail, name='compendium-crystal-detail'),
    path('crystal/<slug:slug>/update/', views.CrystalUpdate.as_view(), name='compendium-crystal-update'),
    path('crystal/<slug:slug>/delete/', views.CrystalDelete.as_view(), name='compendium-crystal-delete'),
    path('tag/', views.TagList.as_view(), name='compendium-tag-list'),
    path('tag/create/', views.TagCreate.as_view(), name='compendium-tag-create'),
    path('tag/<slug:slug>', views.tag_detail, name='compendium-tag-detail'),
    path('tag/<slug:slug>/update', views.TagUpdate.as_view(), name='compendium-tag-update'),
    path('tag/<slug:slug>/delete', views.TagDelete.as_view(), name='compendium-tag-delete'),
    path('', include('django.contrib.flatpages.urls')),
]