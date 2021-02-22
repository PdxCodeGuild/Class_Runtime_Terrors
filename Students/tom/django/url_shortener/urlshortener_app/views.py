from django.shortcuts import render, redirect
from .models import Short_URL
from django.utils.crypto import get_random_string
import string


def about(request):
    return render(request, 'about.html')


def home(request):
    generated_urls = Short_URL.objects.all()
    data = {
        'generated_urls': generated_urls
    }

    if request.method == 'GET':  # if its a GET request, just display the add.html template
        return render(request, 'home.html')
    elif request.method == 'POST':
        original_url = request.POST['original_url']
        random_url = get_random_string(10)
        url = Short_URL.objects.create(original_url=original_url, short_url=random_url)
        return redirect('home', data)
