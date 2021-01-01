from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author, LandBook 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'pages/dashboard.html')


def book_details(request, id):
    book = Book.objects.get(id = id)
    context = {
        "book": book
    } 
    return render(request, 'pages/details.html', context)

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
    elif request.method == 'POST':
        book = Book.objects.all().filter(title=request.POST['title'])
        if not book:
            title = request.POST['title']
            quantity = request.POST['quantity']
            pub_date = request.POST['pub_date']
            book = Book.objects.create(title=title,
                                   author=Author(id=request.POST['author']),
                                   pub_date=pub_date, quantity = quantity)
            messages.success(request, 'Book added in the Database!')
            return redirect('dashboard')
        else: ## Otherwise print error and stay in the form view
            messages.warning(request, 'Book already in the database')
            return render(request, 'pages/addBooks.html', context)

def borrow_book(request, id):
    book = Book.objects.get(id = id)
    context = {
        "book": book
    } 
    if request.method == 'GET':
        return render(request, 'pages/details.html', context)
    elif request.method == "POST":
        amount = int(request.POST['amount'])
        if amount > book.quantity:
            messages.warning(request, 'Not enough quantity')
            return render(request, 'pages/details.html', context)
        else:
        #     user = request.user
        #     status = 'no'
        #     landed = LandBook.objects.create(book=book, user=user, status = "Book is out")
        #     return render(request, 'pages/details.html', context)
              return render(request, 'pages/borrow/borrowView.html', context)



