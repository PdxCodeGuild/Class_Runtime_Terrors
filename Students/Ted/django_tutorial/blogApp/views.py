
from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

posts = [
    {
       'author': 'Ted O',
       'title': 'Blog first post',
       'content': 'The first, dummy post',
       'date_posted': 'Jan 22 , 2021', 
    },
     {
       'author': 'Yoyo Ma',
       'title': 'Blog second post',
       'content': 'The second, dummy post',
       'date_posted': 'Jan 22 , 2021', 
    },
     {
       'author': 'Ziggy Stardust',
       'title': 'Blog third post',
       'content': 'The third, dummy post',
       'date_posted': 'Jan 22 , 2021', 
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})


    
