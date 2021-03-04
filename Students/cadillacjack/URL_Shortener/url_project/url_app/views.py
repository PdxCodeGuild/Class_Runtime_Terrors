from django.shortcuts import render, redirect
from . models import URL_Shortener
from django.utils.crypto import get_random_string
from django.contrib import messages

def post_url(request):
    my_urls = URL_Shortener.objects.all()
    context = {
        'my_urls': my_urls
    }
    if request.method == 'GET':
        return render(request, 'post_url.html', context)
    elif request.method == 'POST':
        url = request.POST['url']
        for x in url:
            if 'https://' in url:
                messages.warning(request, 'remove HTTPS:// from URL')
                return render(request, 'post_url.html', context)
            else:
                decoded_url = url.split('/')
                random = get_random_string(length=5)
                end_url = decoded_url[0] + x + '/' + random
                short = URL_Shortener.objects.create(url_name = url, short_url = end_url)
                return render(request, 'post_url.html', context)


