from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def blog_posts(request):
    blogs = Blog.objects.all()  # gets all of the blog posts from the database and store them in a variable
    print(blogs)
    # create the context dictionary to send the blog posts to the template
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

def see_details(request, id):
    post = Blog.objects.get(id = id)
    return render(request, 'pages/details.html', {"post": post})
