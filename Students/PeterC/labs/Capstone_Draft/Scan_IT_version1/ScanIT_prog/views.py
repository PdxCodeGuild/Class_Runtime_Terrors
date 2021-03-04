import sys
import requests
from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE


def button(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def output (request):
    return render(request,'pages/home.html',{'data':data})

def external(request):
    input= request.POST.get('run_script')
    out= run([sys.executable,'test.py',input],shell=False,stdout=PIPE)
    print(out)

    return render(request,'pages/home.html',{'data':out.stdout})