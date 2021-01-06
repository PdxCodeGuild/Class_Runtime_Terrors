from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about')
]

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/, admin.sight.urls'),
    path('<path>/', include('blog_app.urls'))
]