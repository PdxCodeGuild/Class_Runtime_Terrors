"""crystal_project URL Configuration

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
from django.views.generic.base import RedirectView, TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='blog-post-list'), name='root'),
    path('compendium/', include('compendium.urls')),
    path('blog/', include('blog.urls')),
    path('rockhound/', include('rockHound.urls')),
    path('rockshop/', include('shophound.urls')),
    path('about/', TemplateView.as_view(template_name='site/about.html'), name='about-site'),
    path('user/', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Crystal Compendium Admin'
admin.site.site_title = 'Crystal Compendium Site Admin'