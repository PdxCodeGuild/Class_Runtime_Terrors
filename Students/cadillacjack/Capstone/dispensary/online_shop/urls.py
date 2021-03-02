from django.urls import path
from . import views

app_name = 'online_shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('menu', views.product_list, name='product_list'),
    path('categories/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('varieties/<slug:variety_slug>/', views.product_list, name='variety_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]