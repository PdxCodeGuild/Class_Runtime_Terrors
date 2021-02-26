from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponse
from django.views.generic import TemplateView, View
from django.urls import reverse, reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Crystal, Tag
from .forms import CrystalForm, TagForm
from .utils import ObjectCreateMixin, ObjectDeleteMixin, ObjectUpdateMixin

class CrystalList(View):
    page_kwarg = 'page'
    paginate_by = 5
    template_name = 'compendium/crystal_list.html'

    def get(self, request):
        crystals = Crystal.objects.all()
        paginator = Paginator(crystals, self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try: 
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'prvious_page_url': prev_url,
            'crystal_list': page
        }
        return render(request, self.template_name, context)

def crystal_detail(request, slug):
    crystal = get_object_or_404(
        Crystal, slug__iexact=slug
    )
    return render(
        request,
        'compendium/crystal_detail.html',
        {'crystal': crystal}
    )

class TagList(View):
    page_kwarg = 'page'
    paginate_by = 5
    template_name = 'compendium/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        paginator = Paginator(tags, self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try: 
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'tag_list': page
        }
        return render(request, self.template_name, context)

def tag_list(request):
    return render(
        request,
        'compendium/tag_list.html',
        {'tag_list': Tag.objects.all()}
    )

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    context = {
        'tag': tag,
    }
    return render(request, 'compendium/tag_detail.html', context)

class TagCreate(LoginRequiredMixin, CreateView):
    login_url = '/user/login/'
    form_class = TagForm
    template_name = 'compendium/tag_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template_name, {'form': bound_form})

class TagUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/user/login/'
    form_class = TagForm
    model = Tag
    template_name = ('compendium/tag_form_update.html')

class TagDelete(LoginRequiredMixin, DeleteView):
    login_url = '/user/login/'
    model = Tag
    success_url = reverse_lazy('compendium-tag-list')
    template_name = ('compendium/tag_confirm_delete.html')

class CrystalCreate(LoginRequiredMixin, TemplateView):
    login_url = '/user/login/'
    form_class = CrystalForm
    template_name = 'compendium/crystal_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST, request.FILES)
        if bound_form.is_valid():
            new_crystal = bound_form.save()
            return redirect(new_crystal)
        else:
            return render(request, self.template_name, {'form': bound_form})

class CrystalUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/user/login/'
    form_class = CrystalForm
    model = Crystal
    template_name = ('compendium/crystal_form_update.html')

class CrystalDelete(LoginRequiredMixin, DeleteView):
    login_url = '/user/login/'
    model = Crystal
    success_url = reverse_lazy('compendium-crystal-list')
    template_name = ('compendium/crystal_confirm_delete.html')        
