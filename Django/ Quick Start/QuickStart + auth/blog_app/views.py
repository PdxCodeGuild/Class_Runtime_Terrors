from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def blog_posts(request):
    #  blogs = Blog.objects.all()
    blogs = Blog.objects.filter(user=request.user)
    context = {
        'blogs' : blogs
    }
    return render(request, 'posts.html', context)

@login_required
def add_post(request):
    if request.method =='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
            blog = form.cleaned_data.get('title')
            return redirect('posts')
    else:
        form = BlogForm()
    return render(request, 'add.html', {"form": form})

 

# def add_post(request):
#     if request.method == 'GET':
#         return render(request, 'add.html')
#     elif request.method =='POST':
#         title = request.POST['title']
#         text = request.POST['text']
#         pub_date = request.POST['pub_date']
#         # blogs = Blog.objects.create(title= title, text = text, pub_date = pub_date)
#         blogs = Blog.objects.create(title= title, text = text, pub_date = pub_date, user = request.user)
#         return redirect('posts')
    
@login_required
def see_details(request, id):
    blog = Blog.objects.get(id = id)
    context = {
        'blog' : blog
    }
    return render(request, 'details.html', context )
