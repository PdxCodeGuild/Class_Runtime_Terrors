from django.urls import path
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from potty_spotter.apps.user.views import (
    UserPasswordResetView
)

app_name = "user"

urlpatterns = [
    path("password-reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path(
        "reset/<slug:uidb64>/<slug:token>/",
        PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_confirm.html",
            success_url=reverse_lazy("user:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "reset/done/",
        PasswordResetDoneView.as_view(
            template_name="auth/password_reset_done.html"),
        name="password_reset_done",
    ),
]
