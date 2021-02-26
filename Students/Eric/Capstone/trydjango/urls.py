"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from pages import views
# from products.views import product_detail_view
# from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from core import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', views.home_view, name='home'),
    path('get_events/',views.get_events,name='get_events'),
    
    #Upload Paths
    path('upload/', views.upload, name='upload'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('ask/upload/', views.upload_ask, name='upload_ask'),
    ## Delete Paths
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('ask/<int:pk>/', views.delete_book, name='delete_book'),
    
    
    # List Paths
    path('books/', views.book_list, name='book_list'),
    path('ask/', views.ask_list, name='ask_list'),


]
## If in debugs add a debuging view. 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
