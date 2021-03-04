from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def blog_posts(request):
    blogs = Blog.objects.all()  # gets all of the blog posts from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def add_post(request):
    if request.method == 'GET': # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST': # if it's a POST request ..
        title = request.POST['title']   # get the title from the POST submission, this comes from a form
        text = request.POST['text']     # get the text from the POST submission, this comes from a form
        pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us so we
        # don't need a separate call to the save() method
        blogs = Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')
