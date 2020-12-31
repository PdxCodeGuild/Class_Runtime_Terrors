from django.shortcuts import render, redirect
from .models import Book, Author
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'pages/dashboard.html')

@login_required
def list(request):
    book = Book.objects.all()
    context = {'books': book}
    return render(request, 'pages/bookList.html', context)


def add_authors(request):
    if request.method == "GET":
        return render(request, 'pages/addAuthors.html')
    elif request.method == "POST":
        authors = Author.objects.all().filter(
            available_authors=request.POST['author']) ##filters the database and checks if there's an entry or not
        if not authors: ##if the name isn't in the database, go register it.
            Author.objects.create(available_authors=request.POST['author'])
            messages.success(request, 'Author added in the Database!')
            return redirect('dashboard')
        else: ## Otherwise print error and stay in the form view
            messages.warning(request, 'Author already in the database')
            return render(request, 'pages/addAuthors.html')


def add_books(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    if request.method == 'GET':
        return render(request, 'pages/addBooks.html', context)
    if request.method == 'POST':
        title = request.POST['title']
        pub_date = request.POST['pub_date']
        book = Book.objects.create(title=title,
                                   author=Author(id=request.POST['author']),
                                   pub_date=pub_date)
        return redirect('list')
    return render(request, 'pages/addBooks.html', context)