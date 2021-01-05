from django.shortcuts import render, redirect
from . models import URL_Shortener
from django.utils.crypto import get_random_string
from django.contrib import messages

def post_url(request):
    my_urls = URL_Shortener.objects.all()
    context = {
            "my_urls": my_urls
        }
    if request.method == 'GET':
        return render(request, 'post_url.html', context)
    elif request.method == 'POST':
        url = request.POST['url'] ##get url from form
        for x in url:
            if 'https://' in url:
                messages.warning(request, 'Remove HTTPS:// from the URL')
                return render(request, 'post_url.html', context)
            else:
                decoded_url = url.split('/')
                random = get_random_string(length=5) ## start creating a random string to add after the '/'
                ending_url = decoded_url[0] + x + '/' + random
                shortened = URL_Shortener.objects.create(url_name = url, shortened_url = ending_url)
                return render(request, 'post_url.html', context)