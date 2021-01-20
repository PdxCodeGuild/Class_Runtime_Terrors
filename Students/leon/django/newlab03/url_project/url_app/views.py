from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages
from .models import URL_Shortener
import string
import random

def index(request):
    my_urls = URL_Shortener.objects.all()
    context = {
             "my_urls": my_urls,
            }
    if request.method == "GET":
        return render(request, "index.html", context)

    elif request.method == "POST":
        link = request.POST.get("url_name") 

        for x in link:
            if 'https://' in link:
                messages.warning(request, 'Remove HTTPS:// from url')
                return render(request, 'index.html', context)

        for i in my_urls:
            if link == i.url_name:
                messages.warning(request, "That link already exists")
                return render(request, "index.html", context)
        
        slug = get_random_string(length=12)
        print(slug)
        new_url = URL_Shortener(url_name=link, shortened_url=slug)
        new_url.save()
        my_urls = URL_Shortener.objects.all()
        context = {
             "my_urls": my_urls,
            }
        
        return render(request, "index.html", context)

    
        