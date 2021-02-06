from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import API, Balances
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

def kraken_API_balances(api, user):
    for key in api:
                api_key = key.api_key
                secret_api = key.secret_api
    api_public = {"Time", "Assets", "AssetPairs", "Ticker", "OHLC", "Depth", "Trades", "Spread"}
    api_private = {"Balance"}
    api_trading = {"AddOrder"}
    api_domain = "https://api.kraken.com"
    getDict = {'Ticker':'pair=PAXGXBT', 'Balance': ''}
    callList = []
    for x, y in getDict.items():
        api_data = ""
        api_method = x
        api_data = y
        if api_method in api_private or api_method in api_trading:
                api_path = "/0/private/"
                api_nonce = str(int(time.time()*1000))
                try:
                    api_key = api_key
                    api_secret = base64.b64decode(secret_api)
                except:
                    print("API public key and API private (secret) key must be in text files called API_Public_Key and API_Private_Key")
                    sys.exit(1)
                api_postdata = api_data + "&nonce=" + api_nonce
                api_postdata = api_postdata.encode('utf-8')
                api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_postdata).digest()
                api_hmacsha512 = hmac.new(api_secret, api_path.encode('utf-8') + api_method.encode('utf-8') + api_sha256, hashlib.sha512)
                api_request = urllib2.Request(api_domain + api_path + api_method, api_postdata)
                api_request.add_header("API-Key", api_key)
                api_request.add_header("API-Sign", base64.b64encode(api_hmacsha512.digest()))
                api_request.add_header("User-Agent", "Kraken REST API")
        elif api_method in api_public:
            api_path = "/0/public/"
            api_request = urllib2.Request(api_domain + api_path + api_method + '?' + api_data)
            api_request.add_header("User-Agent", "Kraken REST API")
        try:
            api_reply = urllib2.urlopen(api_request).read()
        except Exception as error:
            print("API call failed (%s)" % error)
            sys.exit(1)
        api_reply = json.loads(api_reply)
        api_reply = api_reply['result']
        callList.append(api_reply)
    balances = callList[1]
    BTC_balance = float(balances['XXBT'])
    PAX_balance = float(balances['PAXG'])
    PAX_price = float(callList[0]['PAXGXBT']['c'][0])
    PAX_value = float("{:.5f}".format(PAX_balance*PAX_price))
    Account_value = float("{:.5f}".format(PAX_value+BTC_balance))
    date_time = timezone.now()
    Balances.objects.create(user = user, BTC_balance = BTC_balance, PAX_balance = PAX_balance, PAX_price=PAX_price, PAX_value=PAX_value, Account_value=Account_value, date_time = date_time)
    
    return BTC_balance, PAX_balance, Account_value

def kraken_API_rebalance(api, user):
    for key in api:
                api_key = key.api_key
                secret_api = key.secret_api
    balances = Balances.objects.filter(user=user).order_by('date_time').reverse()[0]
    BTC_balance = float(balances.BTC_balance)
    PAX_value = float(balances.PAX_value)
    PAX_price = float(balances.PAX_price)
    PAX_order_min = 0.004
    api_public = {"Time", "Assets", "AssetPairs", "Ticker", "OHLC", "Depth", "Trades", "Spread"}
    api_private = {"Balance"}
    api_trading = {"AddOrder"}
    if BTC_balance > PAX_value:
        order_type = 'buy'
    else:
        order_type = 'sell'
    
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(balances.id, balances.date_time)
    BTC_order_volume = abs(float("{:.8f}".format(BTC_balance-PAX_value)))/2
    PAX_order_volume = float("{:.5f}".format(BTC_order_volume/PAX_price))
    print('BTC balance:', BTC_balance)
    print('PAX balance', PAX_value)
    print('Volume to balance', order_type, PAX_order_volume)
    api_domain = "https://api.kraken.com"
    if PAX_order_volume < PAX_order_min:
        status = 'hold'
        print(status)
    else:
        api_method = 'AddOrder'
        api_data = f'pair=PAXGXBT&type={order_type}&ordertype=market&volume={PAX_order_volume}&oflags=fciq'
        if api_method in api_private or api_method in api_trading:
            api_path = "/0/private/"
            api_nonce = str(int(time.time()*1000))
            for key in api:
                api_key = key.api_key
                secret_api = key.secret_api
            try:
                api_key = api_key
                api_secret = base64.b64decode(secret_api)
            except:
                print("API public key and API private (secret) key must be in text files called API_Public_Key and API_Private_Key")
                sys.exit(1)
            api_postdata = api_data + "&nonce=" + api_nonce
            api_postdata = api_postdata.encode('utf-8')
            api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_postdata).digest()
            api_hmacsha512 = hmac.new(api_secret, api_path.encode('utf-8') + api_method.encode('utf-8') + api_sha256, hashlib.sha512)
            api_request = urllib2.Request(api_domain + api_path + api_method, api_postdata)
            api_request.add_header("API-Key", api_key)
            api_request.add_header("API-Sign", base64.b64encode(api_hmacsha512.digest()))
            api_request.add_header("User-Agent", "Kraken REST API")
        elif api_method in api_public:
            api_path = "/0/public/"
            api_request = urllib2.Request(api_domain + api_path + api_method + '?' + api_data)
            api_request.add_header("User-Agent", "Kraken REST API")
        try:
            api_reply = urllib2.urlopen(api_request).read()
        except Exception as error:
            print("API call failed (%s)" % error)
            sys.exit(1)
        api_reply = json.loads(api_reply)
        api_reply = api_reply['result']
        print(api_reply)

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

@login_required
def dashboard(request):
    ############################################ API data get balances ###############################
    api = API.objects.filter(user=request.user)
    user = request.user
        
    callList = kraken_API_balances(api, user)
    BTC_balance = callList[0]
    PAX_balance = callList[1]
    Account_value = callList[2]
    context = {
        'api': api,
        'BTC_balance':BTC_balance,
        'PAX_balance':PAX_balance,
        'Account_value': Account_value,
    }
    return render(request, 'pages/dashboard.html', context)

@login_required
def rebalance(request):
    api = API.objects.filter(user=request.user)
    user = request.user
    kraken_API_balances(api, user)
    kraken_API_rebalance(api, user)


    callList = kraken_API_balances(api, user)
    BTC_balance = callList[0]
    PAX_balance = callList[1]
    Account_value = callList[2]
    context = {
        'api': api,
        'BTC_balance':BTC_balance,
        'PAX_balance':PAX_balance,
        'Account_value': Account_value,
    }
    return render(request, 'pages/rebalance.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

