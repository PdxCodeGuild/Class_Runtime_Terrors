from django.shortcuts import render, redirect
from django.utls.crypto import get_random_string
from . models import Ushort
from django.contrib import messages

def ushrink_list(request):
    all_urls = Ushort.objects.all()
    context = {
        "all_urls": all_urls
    }

    if request.method == 'GET':
        return render(request, 'home.html',context)
    elif request.method == 'POST':
        url = request.POST['url']
        for x in url:
            if 'https://' in url:
                messages.warning(request, "please remove 'https://' from the URL")
                return render(request, 'home.html', context)
            else:
                full_url = url.split('/')
                random = get_random_string(length=5)
                short_url = full_url[0] + x + '///' + random
                shortened = Ushort.objects.create(url_name = url, shortened_url = short_url)
                return render(request, 'home.html', context)




