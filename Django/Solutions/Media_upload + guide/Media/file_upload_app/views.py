from django.shortcuts import render, redirect
from . models import Image


def addImage(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    if request.method == 'GET':
        return render(request, 'pages/file.html', context)
    elif request.method == 'POST':
        for afile in request.FILES.getlist('my_image'):
            Image.objects.create(my_image=afile)
        return redirect('add_image')
