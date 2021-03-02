from django.shortcuts import render, redirect
from .models import Blog, Image
from django.contrib.auth.decorators import login_required
from .forms import BlogForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def blog_posts(request):
    blogs = Blog.objects.filter(user=request.user)
    context = {
        'blogs' : blogs,
    }
    return render(request, 'posts.html', context)

@login_required
def add_post(request):
    # if request.method == 'POST':
    #     form = BlogForm(request.POST)
    #     if form.is_valid():
    #         profile= form.save(commit = False)
    #         profile.user = request.user
    #         profile.save()
    #         blog = form.cleaned_data.get('title')
    #         return redirect('posts')
    # else:
    #     form = BlogForm()
    #     return render(request, 'add.html', {"form": form})

    user = request.user
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method =='POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        blogs = Blog.objects.create(title= title, text = text, pub_date = pub_date, user=user)
        for afile in request.FILES.getlist('my_image'):
             Image.objects.create(image=afile, blog_post=blogs)
        return redirect('posts')
    
@login_required
def see_details(request, id):
    blog = Blog.objects.get(id = id)
    image = Image.objects.filter(blog_post=blog.id)

    context = {
        'blog' : blog,
        'image': image
    }
    return render(request, 'details.html', context )
