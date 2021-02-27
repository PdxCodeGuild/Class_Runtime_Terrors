import base64
from datetime import timedelta
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Count, Q, Sum
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django_tables2 import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from potty_spotter.apps.object import tables as tables_object
from potty_spotter.core.mixins import (
    SearchMixin, FilterMixin, MiscListViewMixin, AjaxTemplateMixin
)
from potty_spotter.core.utils import get_local_time
from potty_spotter.apps.object import models as models_object
from potty_spotter.apps.object import forms as forms_object


class RestroomListView(
    MiscListViewMixin,
    FilterMixin, SearchMixin, LoginRequiredMixin,
    SingleTableMixin, PermissionRequiredMixin, ListView
):
    permission_required = 'object.view_restroom'
    template_name = 'member/object/restroom/list.html'
    model = models_object.Restroom
    table_class = tables_object.RestroomTable
    paginate_by = 20
    search_fields = {
        'name': 'icontains',
        'restroom_id': 'icontains'
    }
    filter_fields = (
        'customer_type',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["html_title"] = "Restroom | TT Finder"
        context["page_title"] = "RESTROOM MANAGMENT"
        context["status_choices"] = models_object.Restroom.StatusChoices.choices
        context["btn_create_url"] = reverse(
            'object:restroom_create')
        context["btn_create_title"] = "ADD RESTROOM"
        # context["btn_import_customer_data"] = True
        context['listview_data'] = {
            "total_object": self.object_list.count(),
            "total_approved": self.object_list.filter(
                status=models_object.Restroom.StatusChoices.APPROVED).count(),
            "total_pending": self.object_list.filter(
                status=models_object.Restroom.StatusChoices.PENDING).count(),
            "total_rejected": self.object_list.filter(
                status=models_object.Restroom.StatusChoices.REJECTED).count(),
        }
        return context


class RestroomCreateView(
    AjaxTemplateMixin, LoginRequiredMixin,
    PermissionRequiredMixin, CreateView
):
    permission_required = 'object.add_restroom'
    ajax_template_name = "member/includes/ajax/form_lg.html"
    template_name = "member/includes/ajax/form_lg.html"
    model = models_object.Restroom
    form_class = forms_object.RestroomCreateForm

    def get_success_url(self):
        return reverse('object:restroom_list')

    def get_context_data(self, *args, **kwargs):
        context = super(RestroomCreateView, self).get_context_data(**kwargs)
        context["form_title"] = _(f"RESTROOM CREATE")
        return context


class RestroomUpdateView(
    AjaxTemplateMixin, LoginRequiredMixin,
    PermissionRequiredMixin, UpdateView
):
    permission_required = 'object.change_restroom'
    ajax_template_name = "member/includes/ajax/form_lg.html"
    template_name = "member/includes/ajax/form_lg.html"
    model = models_object.Restroom
    form_class = forms_object.RestroomUpdateForm

    def get_context_data(self, *args, **kwargs):
        context = super(RestroomUpdateView, self).get_context_data(**kwargs)
        context["form_title"] = _(f"RESTROOM UPDATE")
        return context

    def get_success_url(self):
        return reverse('object:restroom_list')


class RestroomDetailView(LoginRequiredMixin,
                         PermissionRequiredMixin, DetailView):
    permission_required = 'object.view_restroom'
    template_name = "member/includes/ajax/map_detail.html"
    model = models_object.Restroom

    def get_context_data(self, *args, **kwargs):
        context = super(RestroomDetailView, self).get_context_data(**kwargs)
        context["html_title"] = _(f"Restroom Detail - TT Finder")
        return context
