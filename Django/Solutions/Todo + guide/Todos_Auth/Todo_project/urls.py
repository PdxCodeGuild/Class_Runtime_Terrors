

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
    path('', include('pages_app.urls')),
    path('accounts/', include('accounts.urls')),
     path('api-auth/', include('rest_framework.urls'))
]
