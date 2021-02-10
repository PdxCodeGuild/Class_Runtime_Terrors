from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def whatever(request):
    if request.method == 'POST':
        import subprocess
        output = subprocess.run(["python", "script.py"])
        return HttpResponse(output, content_type='text/plain')