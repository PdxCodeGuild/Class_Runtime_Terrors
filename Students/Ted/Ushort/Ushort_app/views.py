from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import Ushort
from django.contrib import messages

def ushrink_list(request):
    all_urls = Ushort.objects.all()
    context = {
        "all_urls": all_urls
    }

    if request.method == 'GET':
        return render(request, 'shrink/home.html',context)

def ushrink_post(request):
    url = request.POST['url']
    for x in url:
        if 'https://' in url:
            messages.warning(request, "please remove 'https://' from the URL")
            # return render(request, 'home.html', context)
            return redirect('Ushort_app:list')
        else:
            # full_url = url.split('/')
            random = get_random_string(length=5)
            short_url = x + '///' + random
            Ushort.objects.create(url_name = url, shortened_url = short_url)
            return redirect('Ushort_app:list') 

def udelete(request, id):
    print(request)
    post = Ushort.objects.get(id=id)
    print(post)
    post.delete()
    return redirect('Ushort_app:list')




