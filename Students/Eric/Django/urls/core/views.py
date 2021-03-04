from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner

# Create your views here.
def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'base.html', {'form':form,'a':a})

def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)