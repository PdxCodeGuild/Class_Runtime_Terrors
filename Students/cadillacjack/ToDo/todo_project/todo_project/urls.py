
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages_app.urls')),
    path('todo/', include('todo_app.urls')),
    path('admin/', admin.site.urls),
]
