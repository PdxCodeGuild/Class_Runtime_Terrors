from django.shortcuts import render
import requests
from .models import Album
# from .forms import ImageForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def home(request):
    albums = Album.objects.all()
    context = {
    'albums': albums
    }
    return render (request, 'info/hawaiiinfo.html', context)

@login_required
def createAlbum(request):
    if request.method == 'POST':
        album_cover=request.FILES['album_cover']
        author = request.user
        text = request.POST['text']
        # post.published_date = timezone.now()
        # created_date = timezone.now()
        new_album = Album.objects.create(album_cover = album_cover, author = author, text = text)
        return redirect ('home')
    else:
        return render(request, 'info/testimage.html')

@login_required
def details (request, id):
    images = get_object_or_404 (Album, id = id)
    return render (request, 'info/details.html', {'images': images})

def display (request):
    albums = Album.objects.all()
    new_album = albums[1]
    print(new_album)
    return render (request, 'info/details.html', {'images': new_album})

    # return JsonResponse ({'comments' : new_album})
    

@login_required
def search (request):
    print ('test')
    albums = Album.objects.all()
    author = request.GET.get('author')
    text = request.GET.get('text')
    # make a calendar for created_date?. Also, should this be separate from text or author searches since those are just text input fields?
    # created_date = request.GET.get('created_date')    
    if author != '' and author is not None:
        qs = albums.filter(author__username__icontains=author)
        print (qs)

    elif text != '' and text is not None:
        qs = albums.filter(text__icontains=text)
        print (qs)
    
    context = {'queryset' : qs}
    return render (request, 'info/testsearchresult.html', context)

# this works as of jan25 but trying out above vode 
# def createAlbum(request):
#     if request.method == 'POST':
#         album_cover=request.FILES['album_cover']
#         new_album = Album.objects.create(album_cover = album_cover)
#         albums = Album.objects.all()
#         context = {
#             'albums': albums
#         }
#         return render (request, 'info/hawaiiinfo.html', context)
#     else:
#         return render(request, 'info/testimage.html')


# def imagehome (request):
#     if request.method == 'POST':
#         form = ImageForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return render(request, "info/testimage.html", {'obj':obj})
#         else:
#             form=ImageForm()
#             img =Image.objects.all()
#             return render (request, 'info/testimage', {'img': img, 'form': form} )

