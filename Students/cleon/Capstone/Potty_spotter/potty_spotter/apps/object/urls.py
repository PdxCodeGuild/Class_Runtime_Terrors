from django.urls import path, include
from potty_spotter.apps.object import views as views_object
from potty_spotter.apps.object import ajax

app_name = "object"

urlpatterns = [
    path("restroom/", views_object.RestroomListView.as_view(), name="restroom_list"),
    path("restroom/create/", views_object.RestroomCreateView.as_view(),
         name="restroom_create"),
    path("restroom/update/<int:pk>/", views_object.RestroomUpdateView.as_view(),
         name="restroom_update"),
    path("restroom/<int:pk>/", views_object.RestroomDetailView.as_view(),
         name="restroom_detail"),
    path("ajax/restroom-status-update/", ajax.update_restroom_status,
         name="ajax_restroom_status_update"),
]
