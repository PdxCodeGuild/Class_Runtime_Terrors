from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=5)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object' : obj
    }
    # return render(request,"product/detail.html",context)
    return render(request,"products/product_detail.html",context)