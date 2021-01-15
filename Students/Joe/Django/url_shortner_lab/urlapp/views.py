from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import URL_alter
from django.utils.crypto import get_random_string
from django.contrib import messages

def url_choice(request):
    return render(request, 'URL_stuff/input.html')

def show (request):
    url_list = URL_alter.objects.all()
    context = {
        "url_list": url_list
    }
    return render (request,'URL_stuff/add.html', context)

def add (request):
    if request.method=='GET':
        return render(request, 'URL_stuff/add.html')
    elif request.method == 'POST':
        inputter = request.POST['inputter']
        for i in inputter:
            splitter = inputter.split('/')
            random = get_random_string(length =5)
            new_one = splitter[0] + i + '/' + random
            print(new_one)
            shorts = URL_alter.objects.create( short_url = new_one, long_url =inputter )
            return redirect ('show')

def delete(request, id):
    objecto = URL_alter.objects.get(id = id)
    objecto.delete()
    return redirect('show')    



