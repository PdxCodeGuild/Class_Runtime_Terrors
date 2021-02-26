from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.shophound_list, name='shophound-shop-list'),
    path('shop/<slug:slug>', views.shop_detail, name='shophound-shop-detail'),
    path('create/', views.createShop, name='shophound-create'),
]