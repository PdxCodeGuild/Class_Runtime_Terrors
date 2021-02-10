from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import requests
import json
#from .models import Signin
#from .models import Greeting
#from Capitan_app.views import Location

def home(request):
    return render(request, 'pages/home.html')

def rover(request):

    
    sequence_img = []
    for sol in range (300, 301):
        url=f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&camera=NAVCAM&api_key=fwhYbiPcZTN6WlXZo10peJY5ywFTSumpb93DClFW"
        url_get = requests.get(url)
        data = url_get.json()
        # print (data)
        if (data['photos']):
            test_img = []
            for photo in data['photos']:
                image_link = photo['img_src']
                image_test = image_link.split('_')
                if image_test[2] not in test_img:
                    test_img.append(image_test[2])
                    print (image_test[2])                 
                    sequence_img.append({'sol': sol, 'image_link': image_link})
                    image_model = Image(sol = sol, image_link = image_link)
                    image_model.save()
        
        

    # for shot in sequence_img:
    #     print (shot)  
        
        # mars= shot

    context = {'sequence_img':sequence_img}
    # print(sequence_img)
    return render(request, 'pages/rover.html', context)



# def about(request):
#     return render(request, 'pages/about.html')

# def blog_posts(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs': blogs
#     }

#     return render(request, 'pages/posts.html', context)

#def Sign_in(request):
    #name = Signin.objects.filter('name')
    #if input name is in name list, 
    # capitan = name.objects.all()

#def Greeting(request):
    #name = Sign_in(capitan.name)

#def Location(request):
    #location = capitan.objects.location.filter(last)
    #location = capitan.(make capitan model)

