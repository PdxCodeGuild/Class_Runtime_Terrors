from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('get_events/',views.get_events,name='get_events')
]