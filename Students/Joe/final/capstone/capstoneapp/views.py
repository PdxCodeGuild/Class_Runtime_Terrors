from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required


def hawaiiblog(request):
    posts = Post.objects.all()
    return render(request, "blogs/hawaiiblog.html", {'posts': posts})

@login_required
def add (request):
    form = PostForm()
    if request.method == 'GET':
        return render(request, "blogs/add.html", {'form' : form})
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            print(post.author)
            return redirect ('hawaiiblog')
        # return render (request, 'blogs/hawaiiblog.html', {'form' : form} )

@login_required
def update (request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # created_date =timezone.now()
            post.save()
            return redirect('hawaiiblog')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/update.html', {'form': form})

# def update (request, id):
#     # print('savepost')
#     # posting = Post.objects.get(id = id)
#     # print(posting)
#     # posting.delete()
#     form = PostForm()
#     # print('savepost')
#     if request.method == 'GET':
#         return render(request, "blogs/update.html", {'form': form})
#     elif request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             print('savepost')
#         return render (request, 'blogs/hawaiiblog.html', {'form': form})    

@login_required
def remove(request, id):
    posting = Post.objects.get(id = id)
    posting.delete()
    return redirect('hawaiiblog')


