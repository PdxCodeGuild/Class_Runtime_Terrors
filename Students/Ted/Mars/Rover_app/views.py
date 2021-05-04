from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import requests
import json
from django.core import serializers


def home(request):
    return render(request, 'pages/home.html')

def cleanup(stuff):
    junk = [27550, 2523, 27530, 27509, 27514, 27521, 1890, 27500, 1889, 27496, 1886, 1893,
     27474, 27484, 1885, 27460, 27461, 27468, 27429, 27434, 27440, 1887, 27535, 27516]
    for image in stuff:
        if image.num in junk:
            image.delete()

def rover(request):   
    sequence_img = []
    stuff = Image.objects.all()
    
    if not stuff:
        for sol in range (300, 310):
            url=f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&camera=NAVCAM&api_key=fwhYbiPcZTN6WlXZo10peJY5ywFTSumpb93DClFW"
            url_get = requests.get(url)
            data = url_get.json()
            stuff = Image.objects.all()
            url_list = []
            
            for things in stuff:
                url_list.append(things.num)
            
            if (data['photos']):
                test_img = []           
                    #to stop redundant loading
                for photo in data['photos']:
                    num = photo['id']
                    image_link = photo['img_src']
                    
                    if num not in url_list:
                        image_test = image_link.split('_')
                        if image_test[2] not in test_img:#filters out duplicates
                            if '543M' not in image_test[2] and '505M' not in image_test[2]:
                            #filters out sky shots
                                if 'D' not in image_test[2]:
                                    test_img.append(image_test[2])
                                    image_model = Image(sol = sol, num = num, image_link = image_link)
                                    image_model.save()                        
                                    

    stuff = Image.objects.all()
    cleanup(stuff)
    stuff = Image.objects.all()
    first = Image.objects.all()[0]
    serialized_image = serializers.serialize('json',Image.objects.all())
    context = {'serialized_image': serialized_image}
    print(serialized_image)
    return render(request, 'pages/rover.html', context)
