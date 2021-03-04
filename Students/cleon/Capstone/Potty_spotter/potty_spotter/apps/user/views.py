from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetView,
)
from django.views.generic import TemplateView
from potty_spotter.core.mixins import GoogleRecaptchaMixin

from django.contrib.auth import get_user_model

User = get_user_model()


class AuthLoginView(GoogleRecaptchaMixin, auth_views.LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True


class UserPasswordResetView(GoogleRecaptchaMixin, PasswordResetView):
    template_name = "auth/password_reset_form.html"
    email_template_name = "auth/password_reset_email.html"
    success_url = reverse_lazy("user:password_reset_done")
    on_success_message = ""
