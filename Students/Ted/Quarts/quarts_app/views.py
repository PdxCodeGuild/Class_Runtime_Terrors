from django.shortcuts import render
from .models import Album, Image


def index(request):
    return render(request, 'navigation/index.html')

def dashboard(request):
    return render(request, 'navigation/dashboard.html')

def createAlbum(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        album_cover = request.FILES.get('album_cover')
        user = request.user
        new_album = Album.objects.create(
            title = title, 
            album_cover = album_cover,
             user = user)

        albums = Album.objects.all()
        context = {
            "albums": albums,
        }
        return render(request, 'collections/view_collections.html', context)
    else:
        return render(request, 'collections/create_album.html')

def collectionDetails(request, id):
    cover = Album.objects.get(id=id)
    images = Image.objects.filter(album=cover.id)
    context = {
        'images': images,
        "cover": cover,
    }
    return render(request, 'collections/view_images.html', context)
