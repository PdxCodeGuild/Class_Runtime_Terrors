from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy, include
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth import views as auth_views
from potty_spotter.apps.user.views import (
    AuthLoginView,
    UserPasswordResetView
)
from potty_spotter.root import views as views_root

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", AuthLoginView.as_view(), name="user-login"),
    path("logout/", auth_views.LogoutView.as_view(), name="user-logout"),

    path("member/", include("potty_spotter.apps.member.urls")),
    path("object/", include("potty_spotter.apps.object.urls")),

    # Register apps url
    path("user/", include("potty_spotter.apps.user.urls", namespace="user")),

    path("", views_root.HomePageView.as_view(), name="home-page"),
]

# Media and Static 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        )
    ]
