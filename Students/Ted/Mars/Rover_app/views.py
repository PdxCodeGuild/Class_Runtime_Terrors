from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
#from .models import Signin
#from .models import Greeting
#from Capitan_app.views import Location

def home(request):
    return render(request, 'pages/home.html')

def rover(request):
    return render(request, 'pages/rover.html')



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

