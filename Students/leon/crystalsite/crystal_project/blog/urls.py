from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-post-list'),
    path('<int:year>/<int:month>/<slug:slug>', views.post_detail, name='blog-post-detail'),
    path('create/', views.post_new, name='blog-post-create'),
    path('<int:year>/<int:month>/<slug:slug>/update', views.PostUpdate.as_view(), name='blog-post-update'),
    path('<int:year>/<int:month>/<slug:slug>/delete', views.PostDelete.as_view(), name='blog-post-delete'),
    path('<int:year>/', views.PostArchiveYear.as_view(), name='blog-post-archive-year'),
    path('<int:year>/<int:month>/', views.PostArchiveMonth.as_view(), name='blog-post-archive-month'),
]
