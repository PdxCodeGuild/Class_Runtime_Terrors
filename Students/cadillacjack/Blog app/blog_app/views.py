from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog_posts(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'templates/posts.html', context)

def add_posts(request):
    if request.method == 'GET':
        return render(request, 'pages/add.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        blogs = Blog.objects.create(title=title, text=text, pub_date=pub_date)
        return redirect('posts')

def see_details(request, id):
    post= Blog.objects.get(id=id)
    return render(request, 'templates/details.html', {"post": post})