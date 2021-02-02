from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import API
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import sys
import time
import base64
import hashlib
import hmac
import json 
import urllib.request as urllib2
from plotly.offline import plot
from plotly.graph_objs import Scatter

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def user_register(request):
    if request.method == 'POST':
        users = User.objects.all().filter(username=request.POST['username']).exists()
        if users:
            messages.warning(request, 'User already exists!')
        else:
            new_user = User(
                username = request.POST['username'],
                email = request.POST['email'],
                # first_name = request.POST['first_name'],
                # last_name = request.POST['last_name']
        )
            new_user.set_password(request.POST['password'])
            new_user.save()
            messages.success(request, 'User registered!')
            return redirect('initial_login')
    return render(request, 'pages/signup.html')

def initial_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('api')
        else:
            return redirect('signup')
    return render(request, 'pages/initial_login.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('signup')
    return render(request, 'pages/login.html')

@login_required
def api(request):
    if request.method == 'GET': 
        return render(request, 'pages/api.html')
    elif request.method == 'POST': 
        user = request.user
        api_key = request.POST['api_key']
        secret_api = request.POST['secret_api']
        register_date = timezone.now()
        apiKeys = API.objects.create(user = user, api_key = api_key, secret_api = secret_api, register_date = register_date )
        return redirect('dashboard')


def dashboard(request):
    # API data get
    api = API.objects.filter(user=request.user)
    callList = {'Balance': ''}
    for x, y in callList.items():
        for key in api:
            api_key = key.api_key
            secret_api = key.secret_api
        api_domain = "https://api.kraken.com"
        api_method = x
        api_data = y
        api_path = "/0/private/"
        api_nonce = str(int(time.time()*1000))
        try:
            api_key = api_key
            api_secret = base64.b64decode(secret_api)
        except:
            print("API public key and/or API private (secret) key are not unlocking")
            sys.exit(1)
        api_postdata = api_data + "&nonce=" + api_nonce
        api_postdata = api_postdata.encode('utf-8')
        api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_postdata).digest()
        api_hmacsha512 = hmac.new(api_secret, api_path.encode('utf-8') + api_method.encode('utf-8') + api_sha256, hashlib.sha512)
        api_request = urllib2.Request(api_domain + api_path + api_method, api_postdata)
        api_request.add_header("API-Key", api_key)
        api_request.add_header("API-Sign", base64.b64encode(api_hmacsha512.digest()))
        api_request.add_header("User-Agent", "Kraken REST API")
        api_reply = urllib2.urlopen(api_request).read()
        api_reply = api_reply.decode()
        api_reply = json.loads(api_reply)
        api_reply = api_reply['result']
        print(api_reply)
    bitcoinBalance = api_reply['XXBT']
    etherBalance = api_reply['XETH']
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    
    context = {
        'api': api,
        'api_reply': api_reply,
        'bitcoinBalance':bitcoinBalance,
        'etherBalance':etherBalance,
        'plot_div': plot_div,
    }
    return render(request, 'pages/dashboard.html', context)



@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

