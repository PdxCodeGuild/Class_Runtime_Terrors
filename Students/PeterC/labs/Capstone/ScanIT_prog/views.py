# import sys
# import requests
# from django.shortcuts import render
# from django.http import HttpResponse
# from subprocess import run,PIPE
# from . models import Scanner

# def button(request):
#     return render(request,'pages/home.html')

# def about(request):
#     return render(request, 'pages/about.html')

# def output (request):
#     return render(request,'pages/home.html',{'data':data})

# def external(request):
#     scan_text = Scanner.objects.all()
#     context = {"scan_text":scan_text}
#     if request.method == "GET":
#         return render(request,'pages/home.html')
#     elif request.method == "POST":
#         text = request.post['run_script']
#         new_text = Scanner.objects.create(text=text)
#         return render(request,'pages/home.html',context)


    # inp= request.POST.get('run_script')
    # print(inp)
    # out= run([sys.executable,'test.py',inp],shell=False,stdout=PIPE)
    # print(out)

    # return render(request,'pages/home.html',{'data':out.stdout})

