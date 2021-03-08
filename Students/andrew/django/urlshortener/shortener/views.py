from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url_Shortener
import random
import string

from .forms import Url


def shorten_url(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)for x in range(10))
            data = form.cleaned_data["url"]
            new_url = Url_Shortener(url=data, slug=slug)
            new_url.save()
    else:
        form = Url()
    url_data = Url_Shortener.objects.all()
    context = {
        'form': form,
        'data': url_data,
    }
    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    link = Url_Shortener.objects.get(slug=slugs)
    return redirect(link.url)


def index(request):
    return HttpResponse("Hello from Django!")
