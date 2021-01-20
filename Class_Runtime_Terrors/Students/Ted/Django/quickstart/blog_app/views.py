from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def blog_posts(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'pages/posts.html')

def add_post(request):
    if request.method == 'GET':
        return render(request, 'pages/add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST[pub_date]

        blogs = Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')


def home(request):
    return render(request, 'pages/about.html')

def about(request):
    return render(request, 'pages/about.html')

def see_details(request, id):
    post = Blog.objects.get(id = id)
    return render(request, 'pages/details.html', {"post": post})

# Create your views here.
