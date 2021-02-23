from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Author, LibraryBook


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    context = {
        'books': books,
        'authors': authors
    }

    return render(request, 'index.html', context=context)


class BookListView(ListView):
    model = Book


class BookDetailView(ListView):
    model = Book
