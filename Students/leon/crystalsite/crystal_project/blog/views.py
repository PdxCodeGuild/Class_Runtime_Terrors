from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, ListView, View
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView, YearArchiveView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm

@login_required(login_url='/user/login/')
@permission_required('blog.add_post')
def post_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog-post-list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
        

def post_edit(request, year, month, slug):
    pass    

class PostCreate(CreateView):
    form_class = PostForm
    model = Post

class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

class OldPostList(View):

    def get(self, request):
        return render(
        request,
        'blog/post_list.html',
        {'post_list': Post.objects.all()}
    )

def post_list(request):
    return render(
        request,
        'blog/post_list.html',
        {'post_list': Post.objects.all()}
    )

def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug
        )
    return render(request, 'blog/post_detail.html', {'post': post})

class OldPostCreate(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form': bound_form})


class PostUpdate(LoginRequiredMixin, View):
    login_url = '/user/login/'
    form_class = PostForm      
    model = Post      
    template_name = 'blog/post_form_update.html'

    def get_object(self, year, month, slug):
        return get_object_or_404(
            self.model,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug)

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        context = {
            'form': self.form_class(instance=post), 
            'post': post, 
            }
        return render(request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {
                'form': bound_form,
                'post': post,
            }
            return render(request, self.template_name, context)

class PostDelete(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug
            )
        return render(request, 'blog/post_confirm_delete.html', {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug
            )
        post.delete()
        return redirect('blog_post_list')

class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True

class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'
