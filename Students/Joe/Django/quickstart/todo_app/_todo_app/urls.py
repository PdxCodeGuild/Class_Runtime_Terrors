from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages_app.urls')),
    path('todos/', include('todo_app.urls')),
    path('admin/', admin.site.urls),
]