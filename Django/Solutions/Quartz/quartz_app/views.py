from django.shortcuts import render, redirect
from .models import Album, Image
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'navigation/index.html')

@login_required
def dashboard(request):
    return render(request, 'navigation/dashboard.html')

@login_required
def createAlbum(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        album_cover = request.FILES.get('album_cover')
        user = request.user
        new_album = Album.objects.create(
            title=title,
            album_cover=album_cover,
            user=user
        )

        albums = Album.objects.filter(user=request.user)
        print(albums)
        context = {
            "albums": albums,
        }
        return render(request, 'collections/view_collections.html', context)
    else:
        return render(request, 'collections/create_album.html')

@login_required
def viewCollections(request):
    albums = Album.objects.filter(user=request.user)
    context = {
        'albums': albums,
    }
    return render(request, 'collections/view_collections.html', context)

@login_required
def collectionDetails(request, id):
    cover = Album.objects.get(id=id)
    images = Image.objects.filter(album=cover.id)
    context = {
        'images': images,
        'cover': cover,
    }
    return render(request, 'collections/view_images.html', context)

@login_required
def delete_album(request, id):
    albums = Album.objects.get(id=id)
    albums.delete()
    return redirect('view-collections')


# Image Model Logic
@login_required
def addImages(request, id):
    cover = Album.objects.get(id=id)
    images = Image.objects.filter(album=cover.id)
    if request.method == 'POST':
        for afile in request.FILES.getlist('image_file'):
            Image.objects.create(image=afile, album=cover, title = afile.name)
        
        context = {
            'images': images,
            'cover': cover,
        }
        return render(request, 'collections/view_images.html', context)

    else:
        context = {'cover': cover}
        return render(request, 'collections/add_images.html', context)
