from django.urls import path
from . import views
# from Api import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('locale/', views.locale, name = 'locale'),
    path('roverlook/', views.rover, name = 'rover')
    # path('about/', views.about, name = 'about'),
    # path('posts/', views.about, name = 'about'),
    # path('add/', views.add_post, name = 'add_posts'),
    
]