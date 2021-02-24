

from django.contrib import admin
from django.urls import path,include
from todo_app import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('', views.TodoView, basename='ApiTodos')

urlpatterns = [
    path('api-data/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
    path('', include('pages_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
