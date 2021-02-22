from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm, AskForm
from .models import Book, Event, Ask
from django.http import JsonResponse

# from .models import *

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html",{})

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sm_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def get_events(request):
    events= Event.objects.all()
    events_json=[]
    for event in events:
        events_json.append({
                'title': event.title,
                'start': event.start_time,
                'end': event.end_time
               
        })
    print('test')
    return JsonResponse({
        'events':events_json
    })

def ask_list(request):
    ask = Ask.objects.all()
    return render(request, 'ask_list.html', {
        'books':ask
    })


def upload_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST, request.FILES)
        if form.is_valid():  # Save Form if Valid
            form.save()
            return redirect('ask_list') # Go to SM if Good
    else:
        form = AskForm()
    return render(request, 'upload_ask.html', {
        'form':form
    })

def delete_book(request, pk):
    if request.method == 'POST':
        ask = Ask.objects.get(pk=pk)
        ask.delete()
    return redirect('ask_list')