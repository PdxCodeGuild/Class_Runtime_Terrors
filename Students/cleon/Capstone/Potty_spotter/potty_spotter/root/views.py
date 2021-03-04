from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, View


class HomePageView(TemplateView):
    template_name = "base/home.html"
