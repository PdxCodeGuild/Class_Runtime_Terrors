from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verify_burrito(request):
    if request.method == 'POST':
        data = {
            'status': 'success',
            'username': request.POST['username'],
            'password': request.POST['password'],
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],            
            'dob': request.POST['dob'],            
            'ssn': request.POST['ssn'],
            'street': request.POST['street'],            
            'city': request.POST['city'],            
            'state': request.POST['state'],            
            'zip': request.POST['zip'],            
        }
        return JsonResponse(data)
    else:
        data = {'status': 'fail'}
        return JsonResponse(data)