from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def blog_posts(request):
    blogs = Blog.objects.all()  
    print(blogs)
    context = {
       'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def add_post(request):
    if request.method == 'GET': 
        return render(request, 'pages/add.html')
    elif request.method == 'POST':
        title = request.POST['title']  
        text = request.POST['text']    
        pub_date = request.POST['pub_date']
        blogs = Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')
