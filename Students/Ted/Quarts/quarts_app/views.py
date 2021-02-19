from django.shortcuts import render

def index(request):
    return render(request, 'navigation/index.html')

def dashboard(request):
    return render(request, 'navigation/dashboard.html')

def createAlbum(request):
    if request.method == 'POST':
        title = request.POST('title')
        album_cover = request.FILES('album_cover')
        user = request.user
        new_album = Album.objects.create(title = title, album_cover =, user = user)
        albums = Album.objects.all()
        context = {
            "albums": slbums,
        }
        return render(request, 'collections/view_collections.html, context')
