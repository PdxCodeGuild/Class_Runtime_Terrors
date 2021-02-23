from django.shortcuts import render
from .models import Urlss
from base64 import b64encode
from uuid import uuid4


def url_home(request):
    shortUrl = ""
    if request.method == "POST":
        try:
            uurl = request.POST['uurl']
            if uurl:
                shortUrl = b64encode(
                    (str(uuid4()).split('-')[0]).encode()).decode()[0:5]
                newUrl = Urlss(fullUrl=uurl, shortUrl=shortUrl)
                newUrl.save()
                print('added ', newUrl)

        except Exception as err:
            print(err)

    return render(request, "urlshortener/index.html", {"short_url": shortUrl})


def url_gen(request, uurl):
    shortUrl = ""
    if uurl:
        shortUrl = b64encode(str(uuid4()).split('-')[0])
        # newUrl =
    return render(request, "urlshortener/index.html", {"short_url": shortUrl})


def url_get(request, suurl):
    longUrl = ""
    try:
        if suurl:
            print(suurl)
            longUrl = Urlss.objects.get(shortUrl=suurl).fullUrl
    except Exception as err:
        print(err)
    return render(request, "urlshortener/index.html", {"long_url": longUrl})


def url_delete(request):
    pass
